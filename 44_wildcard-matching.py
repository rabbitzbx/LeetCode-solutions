class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j, m, n = 0, 0, -1, -1

        while i < len(s):
            if j == len(p) - 1 and p[j] == '*':
                return True
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                j += 1
                m, n = i + 1, j
            elif m != -1:
                i, j = m, n
                m, n = i + 1, j
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
