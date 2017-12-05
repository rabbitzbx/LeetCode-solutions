class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for num in nums:
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
            
        return False

a = Solution()
print(a.increasingTriplet([5, 1, 5, 5, 2, 5, 4]))
print(a.increasingTriplet([0, 4, 2, 1, 0, -1, -3]))

