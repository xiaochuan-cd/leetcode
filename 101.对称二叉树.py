# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSame(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val \
        and self.isSame(left.left, right.right) \
        and self.isSame(left.right, right.left)
        
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSame(root.left, root.right)

        