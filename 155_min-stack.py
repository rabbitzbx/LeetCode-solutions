class MinStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.mins:
            self.mins.append(min(self.mins[-1], x))
        else:
            self.mins.append(x)
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.mins.pop()
        return self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
