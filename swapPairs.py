# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        hd = ListNode(0)
        hd.next = head
        head = hd
        prev = hd
        hd = hd.next

        while hd and hd.next:

            next = hd.next
            prev.next = next
            hd.next = next.next
            next.next = hd

            prev = hd
            hd = hd.next

        return head.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    print(Solution().swapPairs(head))
