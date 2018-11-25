class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        res = None
        i = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]

                    res = s if res == None or abs(
                        s-target) < abs(res-target) else res

                    if s == target:
                        return s
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
        return res


if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, - 4], 1))
