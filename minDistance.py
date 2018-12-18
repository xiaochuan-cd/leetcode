class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m, n = len(word1)+1, len(word2)+1
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][0] = i
        for i in range(n):
            dp[0][i] = i

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] +
                               (0 if word1[i-1] == word2[j-1] else 1))

        return dp[m-1][n-1]


if __name__ == "__main__":
    print(Solution().minDistance("horse", "aaahorse"))
