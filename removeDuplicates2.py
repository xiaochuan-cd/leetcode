class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums)

        i, j = 2, 2
        while i < len(nums):
            if not (nums[j-1] == nums[j-2] == nums[i]):
                nums[j] = nums[i]
                j += 1
            i += 1

        return j


if __name__ == "__main__":
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
