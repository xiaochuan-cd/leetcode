class Solution:

    def recursive(self, i, j):
        c = self.d[i][j]
        if c != -1:
            return c
        c = 0
        if i < self.m - 1 and not self.ob[i][j]:
            c += self.recursive(i+1, j)
        if j < self.n - 1 and not self.ob[i][j]:
            c += self.recursive(i, j+1)
        if i == self.m - 1 and j == self.n - 1 and not self.ob[i][j]:
            c = 1
        self.d[i][j] = c
        return c

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        self.m, self.n, self.ob, self.d = len(
            obstacleGrid), len(obstacleGrid[0]), obstacleGrid, []
        self.d = [[-1 for _ in range(self.n)] for _ in range(self.m)]
        return self.recursive(0, 0)


if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles([[0, 0]]))
