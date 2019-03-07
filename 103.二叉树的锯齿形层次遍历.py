class Solution(object):
    def zigzagLevelOrder(self, root):
        ret = []
        if root:
            q = [root]
            d = True
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
                if not d:
                    lvlret = lvlret[::-1]
                d = not d
                q = lvlq
                ret.append(lvlret)
        return ret