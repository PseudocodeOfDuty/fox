import collections


class Hard:
    def paths(self, x: int, y: int) -> int:
        dp = [0] * (y)
        # you have one way to reach [0,0]
        dp[0] = 1

        # calculate no. of ways for every(x,y)
        for _ in range(x):
            for j in range(1, y):
                dp[j] += dp[j - 1]

        return dp[-1]
