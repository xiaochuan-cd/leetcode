# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not len(postorder):
            return None

        tree = TreeNode(postorder[-1])
        if len(postorder) == 1:
            return tree

        inx = inorder.index(postorder[-1])

        tree.left = self.buildTree(inorder[:inx], postorder[:inx])
        tree.right = self.buildTree(inorder[inx+1:], postorder[inx:-1])

        return tree
