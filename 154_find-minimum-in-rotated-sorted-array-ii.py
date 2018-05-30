class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [a0, a1, a2, ..., am, ... , an]
        # 假设 am 为最小数，那么必定满足 a0 < a1 < ... > am 和 am < am+1 < ... < an
        # 遍历数组，如果存在 a0 > am, 那么第一个 am 即为最小数。如果不存在，那么 a0 即为最小数。
        result = nums[0]

        for num in nums[1:]:
            if result > num:
                return num
        
        return result