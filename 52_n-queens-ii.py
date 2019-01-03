class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper([], n)

    def helper(self, result, n):
        if len(result) == n:
            return 1

        count = 0
        for i in range(n):
            if self.isValid(result, i):
                count += self.helper(result + [i], n)
        return count

    def isValid(self, result, num):
        for i, item in enumerate(result):
            if item == num or (i + item) == (len(result) + num) or (i - item) == (len(result) - num):
                return False
        return True
