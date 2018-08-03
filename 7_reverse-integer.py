class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 如果 x 是正数，x 末尾数字为 x % 10，然后计算 x = int(x / 10)
        # 重复上面步骤，直到 x 为 0
        # 如果 x 是负数，则先将它取反, 计算出结果再取反
        result = 0
        isNegitive = False
        if x < 0:
            x = -x
            isNegitive = True
        while x > 0:
            tmp = x % 10
            result = 10 * result + tmp
            x = int(x / 10)
        if isNegitive:
            result = -result
        if result > 2 ** 31 or result < -2 ** 31 - 1:
            return 0
        return result
