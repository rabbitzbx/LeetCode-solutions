class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        arr = [0]
        length = 1
        prevIndex = 0

        for i in range(1, num + 1):
            arr.append(1 + arr[prevIndex])
            prevIndex += 1
            if prevIndex == length:
                length = len(arr)
                prevIndex = 0
                
        return arr
