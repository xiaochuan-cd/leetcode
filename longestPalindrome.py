
def preProcess(s):
    n = len(s)
    if n == 0:
        return "^$"
    ret = "^"
    for i in range(n):
        ret += "#" + s[i:i+1]

    ret += "#$"
    return ret


class Solution:

    def longestPalindrome(self, s):
        T = preProcess(s)
        n = len(T)
        P = [0]*n
        C = 0
        R = 0

        for i in range(1, n-1):

            i_mirror = 2*C-i

            P[i] = min(R-i, P[i_mirror]) if R > i else 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]

        maxLen = 0
        centerIndex = 0
        for i in range(1, n-1):
            if P[i] > maxLen:
                maxLen = P[i]
                centerIndex = i

        return s[int((centerIndex - 1 - maxLen)/2): int((centerIndex - 1 - maxLen)/2 + maxLen)]
