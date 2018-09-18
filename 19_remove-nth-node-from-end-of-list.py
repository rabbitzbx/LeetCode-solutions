# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return []

        index = 0
        node = head
        node2 = None

        while node.next:
            index += 1
            if node2:
                node2 = node2.next
            if index == n:
                node2 = head
            node = node.next

        if not node2:
            return head.next

        node2.next = node2.next.next

        return head
