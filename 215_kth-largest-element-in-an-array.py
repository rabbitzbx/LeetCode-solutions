class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        left  = [l for l in nums if l < pivot]
        right = [r for r in nums if r > pivot]
        equal = [e for e in nums if e == pivot]
        if k <= len(right):
            return self.findKthLargest(right,  k)
        if k <= len(right) + len(equal):
            return pivot
        return self.findKthLargest(left, k - len(right) - len(equal))
