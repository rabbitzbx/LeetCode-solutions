class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        return self.stack

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        result = self.stack[-1]
        self.stack = self.stack[:-1]
        return result
        
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.stack)
        