class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()

        res = []

        for k, v in enumerate(nums):
            if k >= 1 and v == nums[k-1]:
                continue

            target3 = target - v

            self.threesum(v, nums[k+1:], target3, res)

        return res

    def threesum(self, prefix, nums, target, res):

        for k, v in enumerate(nums):

            if k >= 1 and v == nums[k-1]:
                continue

            wanted_pairs = {}

            temp = None

            for pair in nums[k+1:]:

                if pair == temp:
                    continue

                if pair not in wanted_pairs:
                    wanted_pairs[target-v-pair] = 1
                else:
                    aim = [prefix, v, pair, target-v-pair]
                    aim.sort()
                    res.append(aim)
                    temp = pair


if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
