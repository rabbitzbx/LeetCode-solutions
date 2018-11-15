class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = int((start + end) / 2)
            if target == nums[mid]:
                return mid
            if nums[start] > nums[mid]:
                if target < nums[start] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1
