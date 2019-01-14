# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        self.st = None
        def recursive(root):
            if not root:
                return True
            if root.left:
                if not recursive(root.left):
                    return False
            if self.st != None and self.st >= root.val:
                return False
            self.st = root.val
            if root.right:
                if not recursive(root.right):
                    return False
            return True
        return recursive(root)

root = TreeNode(0)
root.right = TreeNode(-1)
print(Solution().isValidBST(root))




