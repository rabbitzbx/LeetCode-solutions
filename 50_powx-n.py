class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n > 0:
            return self.helper(x, n)
        else:
            return 1 / self.helper(x, -n)
        
    def helper(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        return (x if n % 2 else 1) * self.myPow(x * x, n // 2)
