class Solution:

    def recursive(self, i, j):

        cache = self.d[i][j]
        if cache != -1:
            return cache

        cur0, cur1, cur = -1, -1, 0

        if i < self.m - 1:
            cur0 = self.recursive(i+1, j) + self.grid[i][j]
        if j < self.n - 1:
            cur1 = self.recursive(i, j+1) + self.grid[i][j]
        if i == self.m - 1 and j == self.n - 1:
            cur0 = self.grid[i][j]

        if cur0 != -1 and cur1 != -1:
            cur = min(cur0, cur1)
        elif cur0 != -1:
            cur = cur0
        elif cur1 != -1:
            cur = cur1

        self.d[i][j] = cur
        return cur

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.m, self.n, self.grid, self.d = len(grid), len(grid[0]), grid, []
        self.d = [[-1 for _ in range(self.n)] for _ in range(self.m)]
        return self.recursive(0, 0)


if __name__ == "__main__":
    print(Solution().minPathSum([[1, 2, 5], [3, 2, 1]]))
