# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        i = k - 1
        tail = head
        move = head

        while i:
            i = i - 1
            if tail.next:
                tail = tail.next
            else:
                return head

        while move != tail:
            move.next, tail.next, move = tail.next, move, move.next

        head.next = self.reverseKGroup(head.next, k)

        return tail
