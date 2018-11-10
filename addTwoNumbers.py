# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _l3 = ListNode(0)
        l3 = _l3
        f = 0
        while True:
            v1 = l1 if l1 else None
            v2 = l2 if l2 else None
            if f == 0 and not v1 and not v2:
                break

            l3.next = ListNode(0)
            l3 = l3.next
            s = (v1.val if v1 else 0) + (v2.val if v2 else 0) + f
            l3.val = s % 10
            f = int(s/10)

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return _l3.next
