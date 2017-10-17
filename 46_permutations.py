class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not len(nums):
            return []

        result = [[nums[0]]]

        for i in range(1, len(nums)):
            num = nums[i]
            tmp = []
            for arr in result:
                for j in range(len(arr) + 1):
                    tmpArr = arr[:]
                    tmpArr.insert(j, num)
                    tmp.append(tmpArr)
            result = tmp

        return result


