class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        m = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]

        d = [1000, 100, 10, 1]

        r = ''

        for k, v in enumerate(d):
            r += m[k][int(num/v)]
            num = num % v

        return r


if __name__ == "__main__":
    print(Solution().intToRoman(1094))
    print(Solution().intToRoman(1994) == 'MCMXCIV')
