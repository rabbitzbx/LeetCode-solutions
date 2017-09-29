class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash = {}
        missing = len(t)
        start = end = tmp = 0

        for c in t:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1

        for i, c in enumerate(s):
            if c in hash:
                if hash[c] > 0:
                    missing -= 1
                hash[c] -= 1
                if not missing:
                    while tmp < i and (s[tmp] not in hash or hash[s[tmp]] < 0):
                        if s[tmp] in hash:
                            hash[s[tmp]] += 1
                        tmp += 1
                    if not end or i + 1 - tmp < end - start:
                        start, end = tmp, i + 1
        
        return s[start: end]

a = Solution()
a.minWindow('ADOBECODEBANC', 'ABC')
a.minWindow('aaaaaaa', 'aaaaa')
a.minWindow('aa', 'aaaaa')
a.minWindow("cabwefgewcwaefgcf", "cae")
