class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        m, n = 0, len(nums)-1

        for i in range(len(nums)):
            while m < len(nums) and nums[m] == 0:
                m += 1
            while n > 0 and nums[n] == 2:
                n -= 1
            if i > n or m == len(nums) or n == -1 or m == n:
                break
            if nums[i] == 0 and i >= m:
                nums[i], nums[m] = nums[m], nums[i]
            if nums[i] == 2 and i <= n:
                nums[i], nums[n] = nums[n], nums[i]
                while nums[i] == 0 and i >= m:
                    nums[i], nums[m] = nums[m], nums[i]
                    m += 1

        return nums


if __name__ == "__main__":
    print(Solution().sortColors([2, 0]))
