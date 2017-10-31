class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not len(nums):
            return []

        dict = {-1: set()}
        result = []

        for num in sorted(nums):
            dict[num] = max((dict[d] for d in dict if num % d == 0), key=len) | {num}

        result = list(max(dict.values(), key=len))
        return result
