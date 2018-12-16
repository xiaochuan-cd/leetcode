class Solution:

    def isint(self, s):
        if not s:
            return False
        if s[0] not in ['+', '-'] and (s[0] < '0' or s[0] > '9'):
            return False
        s1 = s[1:]
        if not s1:
            return '0' <= s[0] <= '9'
        for c in s1:
            if c < '0' or c > '9':
                return False
        return True

    def isfloat(self, s):
        if not s:
            return False
        if s[0] not in ['+', '-', '.'] and (s[0] < '0' or s[0] > '9'):
            return False
        dot, dig = s[0] == '.', '0' <= s[0] <= '9'
        s = s[1:]
        for c in s:
            if c == '.' and not dot:
                dot = True
                continue
            if c < '0' or c > '9':
                return False
            dig = True
        return bool(s) and dig

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.strip()
        if 'e' in s:
            i = s.index('e')
            if self.isint(s[i+1:]):
                if '.' in s[0:i]:
                    return self.isfloat(s[0:i])
                else:
                    return self.isint(s[0:i])
            return False

        if '.' in s:
            return self.isfloat(s)

        return self.isint(s)


if __name__ == "__main__":
    print(Solution().isNumber('-.'))
    print(Solution().isNumber('2e10'))
