class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not len(matrix) or not len(matrix[0]):
            return []

        result = []
        m, n = len(matrix), len(matrix[0])

        for i in range(min(m, n) / 2):
            for j in range(i, n - i):
                result.append(matrix[i][j])
            for j in range(i + 1, m - i - 1):
                result.append(matrix[j][n - 1 - i])
            for j in reversed(range(i, n - i)):
                result.append(matrix[m - 1 - i][j])
            for j in reversed(range(i + 1, m - i - 1)):
                result.append(matrix[j][i])

        if min(m, n) % 2:
            i = min(m, n) / 2
            if m > n:
                for j in range(i, m - i):
                    result.append(matrix[j][n - 1 - i])
            else:
                for j in range(i, n - i):
                    result.append(matrix[i][j])
                
        return result
