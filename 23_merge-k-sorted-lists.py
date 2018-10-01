# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not len(lists):
            return None

        if len(lists) is 1:
            return lists[0]

        i, j = 0, len(lists) - 1

        while j > 1:
            i = 0
            while i < j:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1

        return self.mergeTwoLists(lists[0], lists[1])

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l3 = ListNode(l1.val)
            l3.next = self.mergeTwoLists(l1.next, l2)
        else:
            l3 = ListNode(l2.val)
            l3.next = self.mergeTwoLists(l1, l2.next)

        return l3
