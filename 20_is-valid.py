class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        matchObj = {
            '}':'{',
            ']':'[',
            ')':'(',
        }
        for val in s:
            if len(arr) and (val in matchObj) and matchObj[val] == arr[-1]:
                arr.pop()
            else:
                arr.append(val)
        return not len(arr)

