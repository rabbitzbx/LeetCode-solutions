class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp = 1.0

        while tmp:
            tmp = (x / tmp + tmp) / 2
            num = int(tmp)
            if num ** 2 <= x and (num + 1) ** 2 > x:
                return num
