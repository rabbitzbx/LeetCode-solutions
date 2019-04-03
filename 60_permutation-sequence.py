import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = [i for i in range(1, n + 1)]
        result = ''

        while n:
            num = math.factorial(n - 1)
            i = int(math.ceil((k - 1) / num))
            result += str(arr[i])
            del arr[i]
            k = k % num
            n -= 1

        return result
