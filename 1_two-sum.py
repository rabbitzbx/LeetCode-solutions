class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                print [dict[nums[i]], i]
                return [dict[nums[i]], i]
            else:
                 dict[target-nums[i]] = i

a = Solution()
nums = [2, 7, 8, 12]
a.twoSum(nums, 9)
a.twoSum(nums, 15)
a.twoSum(nums, 20)