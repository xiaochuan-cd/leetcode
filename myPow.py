class Solution:

    def recursive(self, x, n):

        r = self.d.get(n, None)
        if r != None:
            return r

        if n == 1:
            return x
        if n == 0:
            return 1

        r = self.recursive(x, int(n/2)) * self.recursive(x, int(n-int(n/2)))
        self.d[n] = r
        return r

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        self.d = {}
        v = self.recursive(x, abs(n))
        if n < 0:
            v = 1/v

        return round(v, 5)


if __name__ == "__main__":
    print(Solution().myPow(0.00001, 2147483647))
    print(Solution().myPow(2.0, 10))
    print(Solution().myPow(2.1, 3))
