import numpy as np

def matching_degree1(x, y):
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