# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, None, None)

    def helper(self, node, m, n):
        if node == None:
            return True

        if (m == None or node.val > m) and (n == None or node.val < n):
            return self.helper(node.left, m, node.val) and self.helper(node.right, node.val, n)

        return False
        