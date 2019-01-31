class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return

        result = nums[0]
        current = nums[0]
        for num in nums[1:]:
            current = max(current, 0) + num
            result = max(result, current)

        return result
