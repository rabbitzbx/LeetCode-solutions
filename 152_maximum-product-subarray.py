class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmax = nums[0]
        tmin = nums[0]
        result = tmax
        for num in nums[1:]:
            a = tmax * num
            b = tmin * num
            tmax = max(a, b, num)
            tmin = min(a, b, num)
            result = max(tmax, result)
        return result
