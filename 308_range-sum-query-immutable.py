class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        sums = []
        for num in nums:
            if len(sums):
                sums.append(sums[-1] + num)
            else:
                sums.append(num)
        self.sums = sums
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]
