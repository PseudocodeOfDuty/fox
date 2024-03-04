import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import cv2


class reconstructor:
    def matching_degree(self, x, y):

        similarity_r = cosine_similarity([x[:, -1, 0]], [y[:, 0, 0]])
        similarity_g = cosine_similarity([x[:, -1, 1]], [y[:, 0, 1]])
        similarity_b = cosine_similarity([x[:, -1, 2]], [y[:, 0, 2]])

        print((similarity_r[0][0] + similarity_b[0][0] + similarity_g[0][0]) / 3)
        return (similarity_r[0][0] + similarity_b[0][0] + similarity_g[0][0]) / 3

    def matching_degree1(self, x, y):
        """
        Calculate the matching degree between two RGB vectors x and y.
        """
        num_pixels = x.shape[0]

        # Compute the sum of absolute differences for each color channel
        diff_r = np.sum(np.abs(x[:, -1, 0] - y[:, 0, 0]))
        diff_g = np.sum(np.abs(x[:, -1, 1] - y[:, 0, 1]))
        diff_b = np.sum(np.abs(x[:, -1, 2] - y[:, 0, 2]))

        # Compute the numerator and denominator for the matching degree
        numerator = num_pixels - (diff_r + diff_g + diff_b) / 255  # Normalize by 255
        denominator = 3 * num_pixels
        # print(numerator)
        if denominator == 0:
            return 0
        else:
            print(numerator / denominator)
            return numerator / denominator

    def find_best_match(self, x, pieces):
        """
        Find the piece with the highest matching degree with the given left edge x.
        """
        best_match_idx = -1
        max_matching_degree = -1

        for i, y in enumerate(pieces):
            degree = self.matching_degree(x, y)
            if degree > max_matching_degree:
                max_matching_degree = degree
                best_match_idx = i
        print(max_matching_degree)
        print("0=..........................................................")
        return best_match_idx

    def reconstruct_paper(self, pieces):
        """
        Reconstruct the original paper from shredded pieces.
        """
        reconstructed_paper = []
        remaining_pieces = pieces.copy()
        idx_map = [i for i in range(1, len(pieces))]

        current_piece_idx = 0
        reconstructed_paper.append(remaining_pieces.pop(current_piece_idx))
        res = [0]
        while remaining_pieces:
            current_piece = reconstructed_paper[-1]

            # Find the best match for the right edge of the current piece
            next_piece_idx = self.find_best_match(current_piece, remaining_pieces)

            # Add the next piece to the reconstructed paper and remove it from the remaining pieces
            next_piece = remaining_pieces.pop(next_piece_idx)
            reconstructed_paper.append(next_piece)
            res.append(idx_map[next_piece_idx])
            idx_map.pop(next_piece_idx)

        return res

    def solve(self, img):
        chunks = []
        chunk_width = 64
        for i in range(0, img.shape[1], chunk_width):
            chunk = img[:, i : i + chunk_width, :]
            chunks.append(chunk)
            cv2.imwrite(f"./riddles/cv/easy/chunks/chunk_{i//64}.jpg",chunk)

        print(chunks[-1].shape)
        print(len(chunks))
        reconstructed_paper = self.reconstruct_paper(chunks)
        print("Reconstructed paper order:", reconstructed_paper)
