# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        cur = root

        while cur or len(stack):
            while cur:
                stack += [cur]
                cur = cur.left
            cur = stack.pop()
            res += [cur.val]
            cur = cur.right

        return res
