class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i != len(nums):
            if 1 <= nums[i] <= len(nums) and nums[i] != i + 1 and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1

        m = 1
        for i in nums:
            if i == m:
                m += 1
            else:
                break

        return m


if __name__ == "__main__":
    print(Solution().firstMissingPositive([1, 2, 3, 5, 6, 7, 8, 9, 4]))
    print(Solution().firstMissingPositive([1, 2, 0]))
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
