class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        arrs = matrix[:]
        result = 0
        for i, arr in enumerate(matrix):
            for j, item in enumerate(arr):
                arrs[i][j] = int(arrs[i][j])
                if i and j and arrs[i][j]:
                    arrs[i][j] = min(arrs[i - 1][j], arrs[i][j - 1], arrs[i - 1][j - 1]) + 1
                result = max(result, arrs[i][j] ** 2)
        return result