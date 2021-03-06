class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        return [bin(i ^ i >> 1) for i in range(2 ** n)]


if __name__ == "__main__":
    print(Solution().grayCode(3))
