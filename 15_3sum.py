class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                if start > i + 1 and nums[start] == nums[start - 1]:
                    start += 1
                    continue
                s = nums[i] + nums[start] + nums[end]
                if s == 0:
                    result += [[nums[i], nums[start], nums[end]]]
                if s > 0:
                    end -= 1
                else:
                    start += 1

        return result
