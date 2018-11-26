class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if not nums:
            return 0

        i = 0

        for k in range(len(nums)):

            if nums[k] != val:
                nums[i] = nums[k]
                i += 1

        return i


if __name__ == "__main__":
    print(Solution().removeElement([3, 2, 2, 3], 3))
