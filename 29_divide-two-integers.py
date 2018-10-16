class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 0x7fffffff

        isMinus = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        m, n = divisor, 1
        res = 0

        while m <= dividend:
            if m == dividend:
                res += n
                break
            if m + m > dividend:
                dividend -= m
                res += n
                m, n = divisor, 1
            else:
                m += m
                n += n

        return -res if isMinus else res
