import copy


class Solution:

    def recursive(self, n, k, ret=[], pre=[], s=1):
        if n == 0 or k == 0:
            return ret

        if k == 1:
            for i in range(s, n+1):
                pre.append(i)
                ret.append(copy.copy(pre))
                pre.pop()
            return ret

        for i in range(s, n-k+2):
            pre.append(i)
            self.recursive(n, k-1, ret, pre, i+1)
            pre.pop()

        return ret

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        ret = []
        return self.recursive(n, k, ret)


if __name__ == "__main__":
    print(Solution().combine(4, 4))
