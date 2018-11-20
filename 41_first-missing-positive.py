class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            num = nums[i]
            while num > 0 and num <= n and nums[num - 1] != num:
                tmp = nums[num - 1]
                nums[num - 1] = num
                num = tmp

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        return n + 1
