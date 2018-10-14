class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0

        for num in nums:
            if i == 0 or num != nums[i - 1]:
                nums[i] = num
                i += 1

        return i
