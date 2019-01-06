# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict

class Solution:
    def recursive(self, s, e):
        if s > e:
            return [None]
        if (s, e) in self.d:
            return self.d[(s, e)]
        for i in range(s, e+1):
            for l in self.recursive(s, i-1):
                for r in self.recursive(i+1, e):
                    root = TreeNode(i)
                    root.left, root.right = l, r
                    self.d[(s,e)].append(root)
        return self.d[(s, e)]

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """ 
        if n == 0:
            return []
        self.d = defaultdict(list)
        return self.recursive(1, n)

if __name__ == "__main__":
    Solution().generateTrees(6)