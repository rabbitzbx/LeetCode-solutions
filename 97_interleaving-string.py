class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)

        if l1 + l2 != len(s3):
            return False

        s = [[False for i in range(l2 + 1)] for j in range(l1 + 1)]

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0 and j == 0:
                    s[i][j] = True
                elif i == 0:
                    s[i][j] = s[i][j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    s[i][j] = s[i - 1][j] and s1[i - 1] == s3[i - 1]
                else:
                    s[i][j] = (s[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (s[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return s[l1][l2]