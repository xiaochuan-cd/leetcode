class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum, ret = 0, nums[0]
        for i in nums:
            sum = max(sum+i, i)
            ret = max(ret, sum)
        return ret


if __name__ == "__main__":
    print(Solution().maxSubArray([-1]))
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
