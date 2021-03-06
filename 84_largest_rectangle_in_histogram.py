class Solution(object):
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
            
        return result; 