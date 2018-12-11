class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        far = 0
        for k, v in enumerate(nums):
            far = max(far, k+v)
            if far <= k and k != len(nums)-1:
                return False

        return True


if __name__ == "__main__":
    print(Solution().canJump([3, 2, 1, 0, 4]))
    print(Solution().canJump([2, 3, 1, 1, 4]))
