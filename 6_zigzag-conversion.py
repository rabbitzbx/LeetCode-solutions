class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        arr = [''] * numRows
        tmp = 0
        flag = 1
        for c in s:
            arr[tmp] += c
            tmp += flag
            if tmp == numRows - 1:
                flag = -1
            if tmp == 0:
                flag = 1
        return ''.join(arr)
