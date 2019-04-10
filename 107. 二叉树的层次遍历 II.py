# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        if not root:
            return res

        q = []
        q.append(root)

        while q:
            onelevl = []
            for _ in range(len(q)):
                node = q[0]
                del q[0]
                onelevl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.insert(0, onelevl)

        return res
