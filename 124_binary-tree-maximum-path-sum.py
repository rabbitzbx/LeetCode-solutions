# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #     node
        #    /    \
        #  left   right
        # 如上图所示，取两个变量a、b。
        # a 为 max(node.val, node.val + left.val, node.val + right.val)
        # 表示该树整体作为一个节点对于其他节点的最大值
        # b 为 max(left.val, right.val, node.val + left.val + right.val)
        # 表示该树与其他节点没有关联时的最大值

        a, b = self.helper(root)
        return max(a, b)

    def helper(self, node):
        if not node:
            return -float('inf'), -float('inf')
        if not node.left and not node.right:
            return node.val, node.val
        a1, b1 = self.helper(node.left)
        a2, b2 = self.helper(node.right)
        a = max(node.val, node.val + a1, node.val + a2)
        b = max(a1, a2, node.val + a1 + a2, b1, b2)
        return a, b
