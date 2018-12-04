import bisect


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums:
            return [-1, -1]

        l = bisect.bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            l = -1
        r = bisect.bisect_right(nums, target) - 1
        if nums[r] != target:
            r = -1

        return [l, r]


if __name__ == "__main__":
    print(Solution().searchRange([2, 2], 3))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
