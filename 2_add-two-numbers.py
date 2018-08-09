# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp, result = 0, ListNode(0)
        self.helper(l1, l2, tmp, result)
        return result

    def helper(self, l1, l2, tmp, result):
        total = 0

        if not l1 and not l2:
            return
        if not l1:
            total = l2.val + tmp
        elif not l2:
            total = l1.val + tmp
        else:
            total = l1.val + l2.val + tmp

        current = total % 10
        tmp = int(total / 10)
        result.val = current
        
        if (l1 and l1.next) or (l2 and l2.next):
            result.next = ListNode(0)
            self.helper(l1 and l1.next, l2 and l2.next, tmp, result.next)
        elif tmp:
            result.next = ListNode(tmp)
