# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not len(preorder):
            return None

        tree = TreeNode(preorder[0])
        if len(preorder) == 1:
            return tree

        inx = inorder.index(preorder[0])

        tree.left = self.buildTree(preorder[1:1+inx], inorder[:inx])
        tree.right = self.buildTree(preorder[1+inx:], inorder[inx+1:])

        return tree
