class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(x)[::-1]
        if s[-1] == '-':
            s = '-' + s[:len(s)-1]

        s = int(s)

        return s if -2**31 <= s <= 2**31-1 else 0


if __name__ == "__main__":
    print(Solution().reverse(-2147483648))
