class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        end = 0
        furthest = 0

        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            if i == end:
                end = furthest
                jumps += 1

        return jumps
