class Solution:

    def recursive(self, mark, cur, ret):

        if cur == len(mark):
            ret[0] += 1
            return

        for i in range(len(mark)):
            mark[cur], down = i, True
            for j in range(cur):
                if mark[j] == i or abs(i-mark[j]) == cur - j:
                    down = False
                    break
            if down:
                self.recursive(mark, cur+1, ret)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        ret = [0]
        self.recursive([None]*n, 0, ret)
        return ret[0]


if __name__ == "__main__":
    print(Solution().totalNQueens(4))
