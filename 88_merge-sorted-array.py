class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = m, n

        while j > 0:
            if i > 0 and nums1[i - 1] > nums2[j - 1]:
                nums1[i + j - 1] = nums1[i - 1]
                i -= 1
            else:
                nums1[i + j - 1] = nums2[j - 1]
                j -= 1
