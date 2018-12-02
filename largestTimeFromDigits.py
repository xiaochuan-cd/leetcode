import itertools


class Solution:
    def largestTimeFromDigits(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

        t = [-1, -1, -1, -1]
        for i in itertools.permutations(deck, 4):
            if i[0]*10+i[1] < 24 and i[2] < 6:
                if (i[0]*10+i[1])*60+i[2]*10+i[3] > (t[0]*10+t[1])*60+t[2]*10+t[3]:
                    t = i
        if t == [-1, -1, -1, -1]:
            return ''

        return str(t[0])+str(t[1])+':'+str(t[2])+str(t[3])


if __name__ == "__main__":
    print(Solution().largestTimeFromDigits([0, 0, 0, 0]))
