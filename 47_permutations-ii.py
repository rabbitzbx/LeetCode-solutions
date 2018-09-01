class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not len(nums):
            return []

        result = [[nums[0]]]

        for i in range(1, len(nums)):
            insertedNum = nums[i]
            tmpResult = []
            for arr in result:
                continued = True
                for j in range(len(arr) + 1):
                    if continued:
                        tmpArr = arr[:]
                        tmpArr.insert(j, insertedNum)
                        tmpResult.append(tmpArr)
                    if j < len(arr) and insertedNum == arr[j]:
                        continued = False
            result = tmpResult

        return result
