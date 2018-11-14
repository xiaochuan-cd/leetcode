
class Solution:

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        ret = []
        for _ in range(min(numRows, len(s))):
            ret.append([])

        cursor = 0
        direction = 0

        for c in s:
            ret[cursor].append(c)
            if direction == 0:
                cursor += 1
                if cursor == numRows:
                    direction = 1
                    cursor -= 2
            else:
                cursor -= 1
                if cursor < 0:
                    direction = 0
                    cursor += 2

        sret = ''
        for l in range(min(numRows, len(s))):
            sret = sret + ''.join(ret[l])

        return sret


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 4))
