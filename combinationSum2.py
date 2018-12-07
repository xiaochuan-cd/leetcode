class Solution:

    def recursive(self, candidates, target, i, pre=[], ret=[]):

        if i == len(candidates) or sum(candidates[i:]) < target:
            return

        target_bak, curpre = target, []
        if target >= candidates[i]:
            target -= candidates[i]
            curpre = [candidates[i]]

        if target == 0:
            ret.append(pre+[candidates[i]])
        else:
            self.recursive(candidates, target, i + 1, pre+curpre, ret)

        if target_bak >= candidates[i]:
            target += candidates[i]
            curpre = []
            self.recursive(candidates, target, i + 1, pre+curpre, ret)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ret, ret2 = [], []
        self.recursive(candidates, target, 0, [], ret)
        for i in ret:
            i.sort()
            if i not in ret2:
                ret2.append(i)
        return ret2


if __name__ == "__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
