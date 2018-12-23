# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        st, h, dup, fin = [], head, 0, 0
        while h or (fin and dup):
            if not fin and st and st[-1].val == h.val:
                dup = 1
            else:
                if dup:
                    dup = 0
                    st.pop()
                    if st:
                        st[-1].next = h
                    else:
                        head = h
                    if fin:
                        return head
                st.append(h)
                while len(st) > 2:
                    del st[0]
            h = h.next
            fin = not h
        return head


if __name__ == "__main__":
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(2)
    # h.next.next.next = ListNode(2)
    # h.next.next.next.next = ListNode(3)
    # h.next.next.next.next.next = ListNode(4)
    # h.next.next.next.next.next.next = ListNode(5)
    h2 = Solution().deleteDuplicates(h)
    print(1)
