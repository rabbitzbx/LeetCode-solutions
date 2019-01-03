class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        return self.helper([], n)

    def helper(self, result, n):
        if len(result) == n:
            return [self.format(result)]

        results = []
        for i in range(n):
            if self.isValid(result, i):
                results += self.helper(result + [i], n)
        return results

    def isValid(self, result, num):
        for i, item in enumerate(result):
            if item == num or (i + item) == (len(result) + num) or (i - item) == (len(result) - num):
                return False
        return True

    def format(self, result):
        arr = []
        for i in result:
            arr.append('.' * i + 'Q' + '.' * (len(result) - i - 1))
        return arr
