class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[-1] = digits[-1]+1
        ret = [0]+digits
        for i in range(len(ret)-1, -1, -1):
            ret[i-1] += ret[i]//10
            ret[i] = ret[i] % 10
        if ret[0] == 0:
            return ret[1:]
        return ret


if __name__ == "__main__":
    print(Solution().plusOne([9, 9, 9]))
