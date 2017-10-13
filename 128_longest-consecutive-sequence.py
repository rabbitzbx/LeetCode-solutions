class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dict = {}
        result = 0
        
        for num in nums:
            if num not in dict:
                if num - 1 in dict: 
                    left = dict[num - 1] 
                else: 
                    left = 0
                if num + 1 in dict: 
                    right = dict[num + 1] 
                else: 
                    right = 0

                total = left + right + 1
                result = max(result, total)

                dict[num] = total
                dict[num - left] = total
                dict[num + right] = total

        return result 
                
