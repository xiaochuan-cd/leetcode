class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        import math
        u, k0 = [-1] * n, 0

        for i in range(n):
            for j in range(n):
                if j+1 not in u:
                    _k0 = k0 + math.factorial(n-i-1)
                    if _k0 >= k:
                        u[i] = j + 1
                        break
                    else:
                        k0 = _k0
        return ''.join([str(x) for x in u])


if __name__ == "__main__":
    print(Solution().getPermutation(4, 9))
