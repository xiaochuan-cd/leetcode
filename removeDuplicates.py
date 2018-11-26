class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        i = 0

        for k in range(len(nums)):

            if True if k == 0 or nums[k] != nums[k-1] else False:
                nums[i] = nums[k]
                i += 1

        return i


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2, 2, 3]))
