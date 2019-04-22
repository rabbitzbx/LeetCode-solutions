# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        node.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return node
