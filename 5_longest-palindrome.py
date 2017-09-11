class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0
        for i in range(len(s)):
            if i >= maxLen and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen = maxLen + 1
            if i >= maxLen + 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1: i + 1][::-1]:
                start = i - maxLen - 1
                maxLen = maxLen + 2
        return s[start:start + maxLen]

a = Solution()
a.longestPalindrome('cbbd')
a.longestPalindrome('babad')
