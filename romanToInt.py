class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        m = {'IV': 4, 'XL': 40, 'CD': 400, 'IX': 9, 'XC': 90, 'CM': 900,
             'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        r = 0

        while s:

            v = -1
            if len(s) > 1:
                v = m.get(s[0:2], -1)

            if v != -1:
                r += v
                s = s[2:]
            else:
                r += m[s[0]]
                s = s[1:]

        return r


if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))
