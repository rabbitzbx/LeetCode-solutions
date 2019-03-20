class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(nums) + [[]]

    def helper(self, nums):
        if not len(nums):
            return []
        if len(nums) == 1:
            return [nums]
        arr = self.helper(nums[1:])
        return [[nums[0]]] + [[nums[0]] + item for item in arr] + arr
