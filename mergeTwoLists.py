# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def less(self, a, b):
        if a.val < b.val:
            return a
        else:
            return b

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l3 = ListNode(0)
        rl3 = l3

        while l1 or l2:

            if not l1 or not l2:
                l3.next = l1 if l1 else l2
                break

            l3.next = self.less(l1, l2)
            if l3.next == l1:
                l1 = l1.next
            else:
                l2 = l2.next

            l3 = l3.next

        return rl3.next
