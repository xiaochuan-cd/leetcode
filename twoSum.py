class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}
        for k, v in enumerate(nums):
            u = target-v
            if u in d:
                return [d[u], k]
            d[v] = k


if __name__ == "__main__":

    print(Solution().twoSum([3, 3], 6))
