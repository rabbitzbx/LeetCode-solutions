class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        n = 0
        m = x

        while(m >= 1):
            n = n * 10 + m % 10
            m = int(m / 10)

        return n == x
