class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0

        area = 0
        left = 0

        while left < len(height) - 1 and height[left] <= height[left + 1]:
            left += 1

        while left < len(height) - 1:
            right = left + 1
            tmp = left + 1
            while tmp < len(height) and height[left] > height[tmp]:
                if height[tmp] > height[right]:
                    right = tmp
                tmp += 1
            if tmp != len(height):
                right = tmp
            area += min(height[left], height[right]) * (right - left - 1) - sum(height[left + 1: right])
            left = right

        return area
