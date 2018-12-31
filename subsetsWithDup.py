import copy


class Solution:
    def recursive(self, nums, ret=[], pre=[], s=0):
        if s == len(nums)-1:
            pre.append(nums[s])
            ret.append(copy.copy(pre))
            pre.pop()
            return ret

        last = None
        for i in range(s, len(nums)):
            pre.append(nums[i])
            cur = copy.copy(pre)
            if last != cur:
                ret.append(cur)
                last = cur
                self.recursive(nums, ret, pre, i+1)
            pre.pop()
        return ret

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ret = [[]]
        nums.sort()
        return self.recursive(nums, ret)


if __name__ == "__main__":
    print(Solution().subsetsWithDup([1, 2, 2]))
