class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.strip()

        str2 = ''
        for k, v in enumerate(str):
            if k == 0:
                if '0' <= v <= '9':
                    str2 += v
                elif v == '-':
                    str2 += '-0'
                elif v == '+':
                    pass
                else:
                    break
            elif '0' <= v <= '9':
                str2 += v
            else:
                break

        i = int(str2) if str2 else 0

        if i < -2**31:
            return -2147483648
        elif i > 2**31-1:
            return 2147483647

        return i


if __name__ == "__main__":
    print(Solution().myAtoi("-"))
