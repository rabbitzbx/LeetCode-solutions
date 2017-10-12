class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        start = 0
        maxLen = 0
        for i in range(len(s)):
            if s[i] in dict:
                start = max(dict[s[i]] + 1, start)
            maxLen = max(i - start + 1, maxLen)
            dict[s[i]] = i
        return maxLen
