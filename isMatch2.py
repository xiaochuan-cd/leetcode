class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        scur, pcur, sstar, pstar = 0, 0, None, None

        while scur < len(s):
            if pcur < len(p) and p[pcur] in [s[scur], '?']:
                scur, pcur = scur+1, pcur+1
            elif pcur < len(p) and p[pcur] == '*':
                pstar, pcur = pcur, pcur+1
                sstar = scur
            elif pstar != None:
                pcur = pstar + 1
                sstar += 1
                scur = sstar
            else:
                return False

        while pcur < len(p) and p[pcur] == '*':
            pcur += 1

        return pcur >= len(p)


if __name__ == "__main__":

    print(1, Solution().isMatch('mississippi', 'm??*ss*?i*pi') == False)
    print(2, Solution().isMatch('aa', 'c*') == False)
    print(3, Solution().isMatch('aab', 'c*a*b') == False)
    print(4, Solution().isMatch('aa', 'a') == False)
    print(5, Solution().isMatch('aa', '*') == True)
    print(6, Solution().isMatch('cb', '?a') == False)
    print(7, Solution().isMatch('adceb', '*a*b') == True)
    print(8, Solution().isMatch('acdcb ', 'a*c?b') == False)
    print(9, Solution().isMatch(
        'aaaababbbbaaabaaaabbbbabbaaaabaababaaabbbbbabaabaaab ', "ab*aaba**abbaaaa**b*b****aa***a*b**ba*a**ba*baaa*b*ab*") == False)
