class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            area = max(area, self.calArea(height, l, r))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area

    def calArea(self, height, l, r):
        area = min(height[l], height[r]) * (r - l)
        return area
