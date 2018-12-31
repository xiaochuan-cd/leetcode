class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        h = ListNode(0)
        h.next = head
        revt, revh, prev = None, None, h
        while m > 1 or n >= 0:
            if m == 1:
                revt, revh = head, head
            if n == 0:
                revt.next = head
                prev.next = revh
                break
            if m < 1 and n > 0:
                rev2 = head
                head = head.next
                rev2.next = revh
                revh = rev2
            else:
                if m == 2:
                    prev = head
                head = head.next
            m, n = m - 1, n - 1
        return h.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseBetween(head, 2, 4))
