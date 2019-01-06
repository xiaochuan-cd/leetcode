class Solution:
    def recursive(self, n):
        if self.d[n]:
            return self.d[n]
        if n <= 1:
            return 1
        s = 0
        for i in range(1, n+1):
            s += self.recursive(i-1) * self.recursive(n-i)
        self.d[n] = s
        return s

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.d = [0 for _ in range(n+1)]
        return self.recursive(n)

if __name__ == "__main__":
    print(Solution().numTrees(7))


        