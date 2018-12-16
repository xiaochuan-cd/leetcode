class Solution:

    def recursive(self, n):
        if self.d[n] != -1:
            return self.d[n]
        if n <= 2:
            return n
        r = self.recursive(n-1)+self.recursive(n-2)
        self.d[n] = r
        return r

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # self.d = [-1]*(n+1)
        # return self.recursive(n)

        sum, x1, x2 = 0, 0, 1
        for _ in range(1, n+1):
            sum = x1 + x2
            print(x1, x2, sum)
            x1 = x2
            x2 = sum
        return sum


if __name__ == "__main__":
    print(Solution().climbStairs(20))
