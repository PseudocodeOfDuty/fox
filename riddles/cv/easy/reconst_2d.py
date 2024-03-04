import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import cv2


class reconstructor:
    def matching_degree(self, x, y):

        similarity_r = cosine_similarity([x[:, -1, 0]], [y[:, 0, 0]])
        similarity_g = cosine_similarity([x[:, -1, 1]], [y[:, 0, 1]])
        similarity_b = cosine_similarity([x[:, -1, 2]], [y[:, 0, 2]])

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

        print(chunks[-1].shape)
        print(len(chunks))
        sim = self.get_2d_sim(chunks)
        for i in sim:
            print(sum(i)," -- ", i.index(max(i)), max(i)," -- ", i.index(min(i)), min(i))

        print(".......................................................................................")
        num_cols = len(sim[0])  # Assuming all rows have the same number of columns
        for col_index in range(num_cols):
            column = [row[col_index] for row in sim]
            print("Column", col_index, ":", sum(column), " -- ", column.index(max(column)), " -- ", max(column), " -- ", column.index(min(column)), " -- ", min(column))
