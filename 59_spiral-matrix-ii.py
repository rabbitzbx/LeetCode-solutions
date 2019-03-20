class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []

        result = [[0] * n for _ in range(n)]
        current = 1

        for i in range(n / 2):
            for j in range(i, n - i):
                result[i][j] = current
                current += 1
            for j in range(i + 1, n - i - 1):
                result[j][n - 1 - i] = current
                current += 1
            for j in reversed(range(i, n - i)):
                result[n - 1 - i][j] = current
                current += 1
            for j in reversed(range(i + 1, n - i - 1)):
                result[j][i] = current
                current += 1

        if n % 2:
            i = n / 2
            for j in range(i, n - i):
                result[i][j] = current
                current += 1

        return result
