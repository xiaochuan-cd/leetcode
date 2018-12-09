class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jumps, start, end, far = 0, 0, 0, 0
        while end < len(nums) - 1:
            jumps += 1
            for i in range(start, end+1):
                far = max(far, nums[i]+i)
            start, end = end + 1, far
        return jumps

print(Solution().jump([2,3,1,1,4]))