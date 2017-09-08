class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalLen = len(nums1) + len(nums2)
        isEven = not totalLen % 2
        index1 = 0
        index2 = 0
        for i in range(totalLen):
            if index2 >= len(nums2) or index1 < len(nums1) and nums1[index1] < nums2[index2]:
                num = nums1[index1]
                index1 = index1 + 1
            else:
                num = nums2[index2]
                index2 = index2 + 1
            if isEven:
                if i == totalLen / 2 - 1:
                    totalNum = num
                if i == totalLen / 2:
                    return (totalNum + num) / 2
            elif i == (totalLen - 1) / 2:
                print(num)
                return num


a = Solution()
a.findMedianSortedArrays([1], [])
a.findMedianSortedArrays([1, 3], [2])
a.findMedianSortedArrays([1, 2], [3, 4])
a.findMedianSortedArrays([1, 3], [2, 4])
