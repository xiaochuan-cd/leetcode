
tb = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


class Solution:

    def recursive(self, st, res):
        if not st:
            return res

        if not res:
            res = ['']

        res2 = []
        cs = st.pop()

        for c in cs:
            res2 += [c+x for x in res]

        return self.recursive(st, res2)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        st = [tb[int(x)-2] for x in str(digits)]
        res = []

        return self.recursive(st, res)


if __name__ == "__main__":
    print(Solution().letterCombinations(23456789))
