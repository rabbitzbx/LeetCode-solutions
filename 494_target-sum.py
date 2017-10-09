class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = float(sum(nums) - S) / 2
        dict = {total: 1, 0: 0}

        if total < 0 or total * 2 % 2:
            return 0

        if total == 0:
            return 2 ** nums.count(0)

        for num in nums:
            if num <= total:
                for key, val in dict.copy().items():
                    if num <= key:
                        target = key - num
                        if target in dict:
                            dict[target] += val 
                        else:
                            dict[target] = val 
        
        return dict[0] 

