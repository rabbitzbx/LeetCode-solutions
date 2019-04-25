# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Floyd判圈算法
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        t = head
        h = head

        while h and h.next:
            h = h.next.next
            t = t.next
            if h == t:
                return True
            
        return False
