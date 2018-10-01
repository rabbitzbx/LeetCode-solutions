# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head

        head1 = head.next
        head.next = head1.next
        head1.next = head

        if head.next:
            head.next = self.swapPairs(head.next)

        return head1
