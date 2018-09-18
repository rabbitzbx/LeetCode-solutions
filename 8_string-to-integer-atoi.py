class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        isFirst = True
        isMinus = False
        result = 0

        for c in str:
            if isFirst:
                isFirst = False
                if c == ' ':
                    isFirst = True
                elif c == '-':
                    isMinus = True
                elif c.isdigit():
                    result = int(c)
                elif c != '+':
                    return 0
            else:
                if c.isdigit():
                    result = 10 * result + int(c)
                else:
                    return self.getResult(result, isMinus)
        return self.getResult(result, isMinus)

    def getResult(self, result, isMinus):
        if isMinus:
            if -result < (-2 ** 31):
                return -2 ** 31
            return -result
        else:
            if result > (2 ** 31 - 1):
                return 2 ** 31 - 1
            return result
