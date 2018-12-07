class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return '1'

        st, r, sub = [], '', self.countAndSay(n-1)

        for i in sub:
            if (not st) or st[-1] == i:
                st.append(i)
            else:
                r += str(len(st))
                r += str(st[-1])
                st = [i]

        if st:
            r += str(len(st))
            r += str(st[-1])

        return r


if __name__ == "__main__":
    print(Solution().countAndSay(30))
