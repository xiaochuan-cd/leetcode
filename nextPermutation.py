class Solution:

    def reverse(self, nums, st):
        lena = len(nums)
        for i in range(st, st+int((lena-st)/2)):
            nums[i], nums[lena-(i-st)-1] = nums[lena-(i-st)-1], nums[i]

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        lena = len(nums)
        for i in range(1, lena):
            ri = lena-i-1
            if nums[ri] < nums[ri+1]:
                j = ri+1
                while j < lena and nums[j] > nums[ri]:
                    j += 1
                j -= 1
                nums[ri], nums[j] = nums[j], nums[ri]
                self.reverse(nums, ri+1)
                return

        nums.sort()


if __name__ == "__main__":
    nums = [5, 4, 7, 5, 3, 2]
    Solution().nextPermutation(nums)
    print(nums)
