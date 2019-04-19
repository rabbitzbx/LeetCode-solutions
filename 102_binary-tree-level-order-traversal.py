# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        values = []
        current = [root]
        children = []

        while len(current) or len(children) or len(values):
            if not len(current):
                current = children[:]
                children = []
                result.append(values)
                values = []
            node = current.pop(0)
            if node:
                values.append(node.val)
                children += [node.left, node.right]

        return result
