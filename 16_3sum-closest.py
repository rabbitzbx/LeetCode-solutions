class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        nums.sort()
        result = nums[0] + nums[1] + nums[2] - target

        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            rest = target - nums[i]

            while start < end:
                s = nums[start] + nums[end]
                if abs(result) > abs(s - rest):
                    result = s - rest
                if s > rest:
                    end -= 1
                else:
                    start += 1

        return target + result
