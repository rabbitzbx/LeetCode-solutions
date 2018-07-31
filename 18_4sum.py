class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # fourSum(nums, target) = fourSum(nums[1:], target), threeSum(nums[1:], target - nums[0])
        # threeSum(nums, target) = threeSum(nums[1:], target), twoSum(nums[1:], target - nums[0])
        # twoSum(nums, target) = twoSum(nums[1:], target), (target - nums[0])
        nums.sort()
        return self.helper(nums, target, 4)

    def helper(self, nums, target, length):
        if len(nums) < length:
            return []
        if nums[0] > target / length:
            return []
        if nums[-1] < target / length:
            return []
        if length == 1:
            if target in nums:
                return [[target]]
            return []
        # not include nums[0]
        a = self.helper(nums[nums.count(nums[0]):], target, length)
        # include nums[0]
        b = self.helper(nums[1:], target - nums[0], length - 1)
        for i in range(len(b)):
            b[i] = b[i] + [nums[0]]
        return a + b