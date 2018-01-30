class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        stack = []
        result = 0
        signal = 1
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += signal * num
                continue
            if c == '+':
                signal = 1
            if c == '-':
                signal = -1
            if c == '(':
                stack.append(result)
                stack.append(signal)
                result = 0
                signal = 1
            if c == ')':
                result = stack.pop() * result + stack.pop()
            i += 1
        return result
