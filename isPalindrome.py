class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        x1, y = x, 0
        while x1:
            x1, m = int(x1/10), x1 % 10
            y = 10*y + m

        return x == y


if __name__ == "__main__":
    print(Solution().isPalindrome(121))
