class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = 0

        while m < int(n / 2):
            for i in range(m, n - m - 1):
                tmp = matrix[m][i]
                matrix[m][i] = matrix[n - 1 - i][m]
                matrix[n - 1 - i][m] = matrix[n - 1 - m][n - 1 - i]
                matrix[n - 1 - m][n - 1 - i] = matrix[i][n - 1 - m]
                matrix[i][n - 1 - m] = tmp
            m += 1

