class Solution:

    def recursive(self, i, j):
        c = self.d.get(i*100+j, -1)
        if c != -1:
            return c
        c = 0
        if i < self.m - 1:
            c += self.recursive(i+1, j)
        if j < self.n - 1:
            c += self.recursive(i, j+1)
        if i == self.m - 1 and j == self.n - 1:
            c = 1
        self.d[i*100+j] = c
        return c

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        self.m, self.n, self.d = m, n, {}
        return self.recursive(0, 0)


if __name__ == "__main__":
    print(Solution().uniquePaths(23, 12))
