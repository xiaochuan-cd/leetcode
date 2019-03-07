# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        st, n = [], root
        prev, p, q = TreeNode(None), None, None

        while n or st:
            while n:
                st.append(n)
                n = n.left
            n = st.pop()
            if prev.val != None and n.val < prev.val:
                if None == p:
                    p = prev
                q = n
            prev = n
            n = n.right
        p.val, q.val = q.val, p.val
