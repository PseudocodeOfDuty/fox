import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import cv2


class reconstructor:
    NEG_INF = -1

    def matching_degree(self, x, y):

        similarity_r = cosine_similarity([x[:, -1, 0]], [y[:, 0, 0]])
        similarity_g = cosine_similarity([x[:, -1, 1]], [y[:, 0, 1]])
        similarity_b = cosine_similarity([x[:, -1, 2]], [y[:, 0, 2]])

        return (similarity_r[0][0] + similarity_b[0][0] + similarity_g[0][0]) / 3

    def find_matches(self, x, pieces):
        """
        Find the piece with the highest matching degree with the given left edge x.
        """
        matches = []

        for y in pieces:
            degree = self.matching_degree(x, y)
            matches.append(degree)
        return matches

    def get_2d_sim(self, pieces):
        """
        Reconstruct the original paper from shredded pieces.
        """
        res = []

        for piece in pieces:
            row = self.find_matches(piece, pieces)
            res.append(row)
        return res

    def solve(self, img):
        chunks = []
        chunk_width = 64
        for i in range(0, img.shape[1], chunk_width):
            chunk = img[:, i : i + chunk_width, :]
            chunks.append(chunk)

        # print(chunks[-1].shape)
        # print(len(chunks))
        self.chunks_count = len(chunks)
        self.sim = np.array(self.get_2d_sim(chunks))
        return self.get_order()
    
    def chunk_sum(self):
        return self.chunks_count * (self.chunks_count - 1) / 2 - 1 
    
    def reached_final_order(self,arr):
        arr_np = np.array(arr)
        # print(f"sum: {sum(arr_np)}")
        return sum(arr_np) == self.chunk_sum()
    
    def get_best_pair(self):
        max_row = np.argmax(self.sim)
        max_row, max_col = np.unravel_index(max_row,self.sim.shape)
        self.sim[max_row, :] = self.NEG_INF
        self.sim[:, max_col] = self.NEG_INF
        return max_row,max_col
    
    def remove_first_col(self):
        self.sim[:, 0] = self.NEG_INF
    
    def get_order(self):
        left_to_right = [self.NEG_INF] * self.chunks_count
        count = 0
        self.remove_first_col()
        while not self.reached_final_order(left_to_right):
            max_row, max_col = self.get_best_pair()
            # print(f"pair: {max_row},{max_col}")
            left_to_right[max_row] = max_col
            if count ==20:
                break
            else:
                count += 1

        res = [0]
        next_piece_idx = 0
        while left_to_right[next_piece_idx] != self.NEG_INF:
            next_piece_idx = left_to_right[next_piece_idx]
            res.append(next_piece_idx)

        return res