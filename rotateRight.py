# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        h, size = head, 1
        while h.next:
            h = h.next
            size += 1
        h.next = head

        h = head
        for _ in range(size-k % size-1):
            h = h.next
        head = h.next
        h.next = None

        return head


if __name__ == "__main__":

    head = ListNode(1)
    h = head
    for i in range(2, 6):
        h.next = ListNode(i)
        h = h.next

    print(Solution().rotateRight(head, 2))
