class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digits = int(digits)
        mapping = ['', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = list(mapping[digits % 10])
        digits = digits / 10

        while digits >= 1:
            tmp = []
            num = int(digits % 10)
            charStr = mapping[num]

            for item in result:
                for char in charStr:
                    tmp.append(char + item)

            result = tmp
            digits = digits / 10

        return result

