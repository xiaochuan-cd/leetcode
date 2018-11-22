class Solution:

    def _isMatch(self, s, p):

        i = -1
        j = 0

        try:

            while i < len(s) - 1:
                i += 1

                if s[i] == p[j] or p[j] == '.':
                    j += 1

                elif p[j] == '*':
                    if p[j+1] in [s[i], '.']:

                        if j+2 < len(p) and (self._isMatch(s[i:], p[j+2:] or self._isMatch(s[i+1:], p[j+2:]))):
                            return True

                        if i+1 >= len(s) or p[j+1] not in [s[i+1], '.']:
                            j += 2

                    else:
                        j += 2
                        i -= 1
                        continue
                else:
                    return False

            while j < len(p):
                if '*' in [p[j], p[j-1]]:
                    j += 1
                else:
                    return False

        except:
            return False

        return True

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s = s[::-1]
        p = p[::-1]

        return self._isMatch(s, p)


if __name__ == "__main__":
    print(12, Solution().isMatch("abb", "a.*b") == True)
    print(11, Solution().isMatch("aasdfasdfasdfasdfas",
                                 "aasdf.*asdf.*asdf.*asdf.*s") == True)
    print(10, Solution().isMatch("aaa", "ab*ac*a") == True)
    print(0, Solution().isMatch("bbbba", ".*a*a") == True)
    print(1, Solution().isMatch("aaca", "ab*a*c*a") == True)
    print(2, Solution().isMatch("ab", ".*c") == False)
    print(4, Solution().isMatch("ab", ".*") == True)
    print(5, Solution().isMatch("aa", "a*") == True)
    print(6, Solution().isMatch("aa", "a") == False)
    print(7, Solution().isMatch("aab", "c*a*b") == True)
    print(8, Solution().isMatch("mississippi", "mis*is*p*.") == False)
    print(9, Solution().isMatch("mississippi", "mis*is*ip*.") == True)
