class Solution(object):
    _dp = [0]

    def numSquares(self, n):
        dp = self._dp
        i = len(dp)
        while i <= n:
            dp += [min(dp[- i * i] + 1 for i in range(1, int(i**0.5) + 1))]
            i += 1
        return dp[n]
