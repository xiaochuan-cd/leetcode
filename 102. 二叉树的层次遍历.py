# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        ret = []
        if root:
            q = [root]
            while q:
                lvlret = []
                lvlq = []
                while q:
                    n = q[0]
                    del q[0]
                    lvlret.append(n.val)
                    if n.left:
                        lvlq.append(n.left)
                    if n.right:
                        lvlq.append(n.right)
                q = lvlq
                ret.append(lvlret)
        return ret
        