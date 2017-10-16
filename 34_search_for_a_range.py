import math

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not len(nums):
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1
        start = len(nums) 
        end = -1 
        flag = 1

        while left <= right:
            mid = left + math.ceil((right - left) / 2) 
            num = nums[mid]

            if num > target:
                right = mid - 1
            if num < target:
                left = mid + 1
            if num == target:
                if flag:
                    start = min(start, mid)
                    right = mid - 1 
                else:
                    end = max(end, mid)
                    left = mid + 1 

            if left > right and flag: 
                flag = 0
                right = len(nums) - 1

        if end == -1:
            return [-1, -1] 
        else:
            return [start, end]
