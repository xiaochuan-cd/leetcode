# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
# class Solution:

#     def recursive(self, node, ret):
#         if node.left:
#             self.recursive(node.left, ret)
#         ret.append(node.val)
#         if node.right:
#             self.recursive(node.right, ret)

#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """

#         if not root:
#             return []

#         ret = []
#         self.recursive(root, ret)
#         return ret


class Solution:

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ret, st, n = [], [], root

        while n or st:
            while n:
                st.append(n)
                n = n.left
            n = st.pop()
            ret.append(n.val)
            n = n.right
        return ret
