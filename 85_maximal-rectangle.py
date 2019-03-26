class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        result = 0
        heights = []
        for row in matrix:
            if not heights:
                heights = [int(num) for num in row]
            else:
                heights = [heights[i] + 1 if int(num) else 0 for i, num in enumerate(row)]
            result = max(result, self.largestRectangleArea(heights))
        return result

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        heights.append(-1)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                if stack:
                    length = i - stack[-1] - 1
                else:
                    length = i
                result = max(heights[index] * length, result)
            stack.append(i)

        return result
