class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # numTrees[n] = numTrees[n - 1] + numTrees[1] * numTrees[n - 2] + numTrees[2] * numTrees[n - 3] + ...
        # numTrees[1] = 1
        self.cache = [1, 1]
        if n > 1:
            self.cache = self.cache + [0] * (n - 1)
        return self.helper(n)

    def helper(self, n):
        if self.cache[n]:
            return self.cache[n]

        for i in range(n):
            self.cache[n] += self.helper(i) * self.helper(n - 1 - i)

        return self.cache[n]
