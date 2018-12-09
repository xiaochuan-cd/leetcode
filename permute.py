import copy


class Solution:

    def recursive(self, nums, used, path, ret):

        for k, v in enumerate(nums):
            if not used[k]:
                path.append(v)
                if len(path) < len(nums):
                    used[k] = 1
                    self.recursive(nums, used, path, ret)
                    used[k] = 0
                else:
                    ret.append(copy.copy(path))
                path.pop()

        return

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        used, path, ret = [0]*len(nums), [], []
        self.recursive(nums, used, path, ret)
        return ret


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
