class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)

        for i in range(len(s)):
            if not int(s[-i-1]):
                continue
            if i == 0:
                dp[i] = 1
            if i == 1:
                dp[i] = dp[i-1] + (1 if int(s[-2:]) < 27 else 0)
            if i > 1:
                dp[i] = dp[i-1] + (dp[i-2] if int(s[-i-1:-i+1]) < 27 else 0)

        return dp[len(s) - 1]
