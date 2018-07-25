class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 共有两种情况，rob house 0 或者 not rob house 0
        # helper(nums) = max(nums[0] + helper(nums[2:]), helper(nums[1:]))
        self.cache = {}
        return self.helper(nums)
    
    def helper(self, nums):
        if not len(nums):
            return 0
        if len(nums) is 1:
            return nums[0]
        if len(nums) in self.cache:
            return self.cache[len(nums)]
        self.cache[len(nums) - 2] = self.helper(nums[2:])
        self.cache[len(nums) - 1] = self.helper(nums[1:])
        return max(nums[0] + self.cache[len(nums) - 2], self.cache[len(nums) - 1])