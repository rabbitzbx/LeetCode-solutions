class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        result = 0

        while start <= end:
            mid = int((start + end) / 2)
            if target > nums[mid]:
                result = mid + 1
                start = mid + 1
            else:
                end = mid - 1

        return result
