class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = 0

        for c1 in num1:
            tmp = 0
            for c2 in num2:
                tmp = tmp * 10 + int(c1) * int(c2)
            product = 10 * product + tmp

        return str(product)
