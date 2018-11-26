# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        hd = ListNode(0)
        hd.next = head
        head = hd
        prev = hd
        hd = hd.next

        while hd:
            st = []

            for _ in range(k):
                if hd:
                    st.append(hd)
                    hd = hd.next
                else:
                    return head.next

            for i in range(len(st)):
                if i != len(st) - 1:
                    st[len(st)-1-i].next = st[len(st)-1-i-1]

            prev.next = st[-1]
            prev = st[0]
            st[0].next = hd

        return head.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print(Solution().reverseKGroup(head, 5))
