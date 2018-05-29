class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # 简单的计算出每两个数字相加的结果，即 a/b+c/d = (a*d+b*c)/(b*d)，得到最后结果 m/n
        # 计算m和n的最大公约数g，最终结果为(m/g)/(n/g)
        a = b = c = d = None
        mark = 0

        for i in range(len(expression)):
            e = expression[i]
            # 计算两个数字相加
            if i != 0 and (e == '+' or e == '-' or i == len(expression) - 1):
                d = int(expression[mark + 1:i if i != len(expression) - 1 else i + 1])
                a = a * d + b * c if a or a == 0 else c
                b = b * d if b else d
                mark = i
            # 记录第二个数字的分子
            elif e == '/':
                c = int(expression[mark:i])
                mark = i

        if a == 0:
            return '0/1'
        g = self.gcd(abs(a), abs(b))
        result = str(int(a / g)) + '/' + str(int(b / g))
        return result

    # 辗转相除法
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        n = a % b
        if n == 0:
            return b
        else:
            return self.gcd(b, n)

