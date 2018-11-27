class Solution:

    def negative(self, n):
        return ~n+1

    def positive(self, n):
        t = n >> 31
        return (n + t) ^ t

    def negpos(self, sign, n):
        return self.positive(n) if sign else self.negative(n)

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        sign = dividend >> 31 == divisor >> 31
        dividend = self.positive(dividend)
        divisor = self.positive(divisor)

        cnt, minus = 0, divisor
        while dividend >= minus:
            minus <<= 1
            cnt += 1

        if cnt == 0:
            return 0

        r = self.negpos(sign, 2**(cnt-1) +
                        self.divide(dividend-(minus >> 1), divisor))

        if r < -2**31 or r > 2**31 - 1:
            return 2**31 - 1

        return r


if __name__ == "__main__":

    print(Solution().divide(-2147483648, -1), 2147483647)
    # print(Solution().divide(0, 3), 0)
    # print(Solution().divide(1, 3), 0)
    # print(Solution().divide(2, 3), 0)
    # print(Solution().divide(3, 3), 1)
    # print(Solution().divide(4, 3), 1)
    # print(Solution().divide(5, 3), 1)
    # print(Solution().divide(6, 3), 2)
    # print(Solution().divide(7, 3), 2)
    # print(Solution().divide(8, 3), 2)
    # print(Solution().divide(9, 3), 3)
    # print(Solution().divide(10, 3), 3)
    # print(Solution().divide(11, 3), 3)
    # print(Solution().divide(12, 3), 4)
    # print(Solution().divide(13, 3), 4)
    # print(Solution().divide(14, 3), 4)
    # print(Solution().divide(15, 3), 5)
    # print(Solution().divide(16, 3), 5)
    # print(Solution().divide(17, 3), 5)
    # print(Solution().divide(18, 3), 6)
