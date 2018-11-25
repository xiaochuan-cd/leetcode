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

        f, s, fi, si = head, head, 0, 0

        while f:
            f = f.next
            fi += 1
            if fi - n > si + 1:
                si += 1
                s = s.next

        if s == head and n == fi-si:
            head = head.next
        elif n < fi-si:
            s.next = s.next.next

        return head
