class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(len(nums) - 1)):
            if nums[i] < nums[i + 1]:
                k = i + 1
                for j in range(i + 2, len(nums)):
                    if nums[j] > nums[i] and nums[j] < nums[k]:
                        k = j
                nums[i], nums[k] = nums[k], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])
                return
        nums.reverse()
        return
