from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        d = defaultdict(int)
        for i in t:
            d[i] += 1

        m, l, ml, cnt = 2**30, 0, 0, 0
        for r in range(len(s)):
            c = s[r]
            if c in d:
                cnt = cnt + 1 if d[c] > 0 else cnt
                d[c] -= 1
            while cnt == len(t):
                if r - l < m:
                    m = r - l
                    ml = l
                c2 = s[l]
                if c2 in d:
                    if d[c2] >= 0:
                        cnt -= 1
                    d[c2] += 1
                l += 1
        return '' if m == 2**30 else s[ml:ml+m+1]


if __name__ == "__main__":
    print(Solution().minWindow("ab", "a"))
