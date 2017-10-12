class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = []
        for i in range(m):
            arr.append([])
            for j in range(n):
                if i == 0 or j == 0:
                    arr[i].append(1)
                else:
                    arr[i].append(arr[i - 1][j] + arr[i][j - 1])
        return arr[m - 1][n - 1]

