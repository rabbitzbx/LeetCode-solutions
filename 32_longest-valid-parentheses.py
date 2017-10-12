class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [] 
        maxLen = 0

        for i, val in enumerate(s):
            if val == ')' and len(stack) and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        stack.insert(0, -1)
        stack.append(len(s))

        for i in range(len(stack) - 1):
            maxLen = max(maxLen, stack[i + 1] - stack[i] - 1)

        return maxLen

