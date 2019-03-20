class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j, k = -1, -1, -1
        for num in nums:
            k += 1
            nums[k] = 2
            if num < 2:
                j += 1
                nums[j] = 1
            if num == 0:
                i += 1
                nums[i] = 0
