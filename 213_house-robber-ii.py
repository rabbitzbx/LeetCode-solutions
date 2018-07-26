class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 共有两种情况，rob house 0 或者 not rob house 0
        # rob(nums) = max(nums[0] + helper(nums[2:-1]), helper(nums[1:]))
        # 参考 Q198: helper(nums) = max(nums[0] + helper(nums[2:]), helper(nums[1:]))
        if not len(nums):
            return 0
        return max(nums[0] + self.helper(nums[2:-1], {}), self.helper(nums[1:], {}))

    def helper(self, nums, cache):
        if not len(nums):
            return 0
        if len(nums) is 1:
            return nums[0]
        if len(nums) in cache:
            return cache[len(nums)]
        cache[len(nums) - 2] = self.helper(nums[2:], cache)
        cache[len(nums) - 1] = self.helper(nums[1:], cache)
        return max(nums[0] + cache[len(nums) - 2], cache[len(nums) - 1])
