class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        d = {'}': '{', ']': '[', ')': '('}

        stk = [' ']

        for c in s:

            c2 = d.get(c, '')
            if stk[-1] == c2:
                stk.pop()
            elif c2:
                return False
            else:
                stk.append(c)

        return len(stk) == 1


if __name__ == "__main__":
    print(Solution().isValid('') == True)
    print(Solution().isValid('(]') == False)
    print(Solution().isValid('([)]') == False)
    print(Solution().isValid('{[]}') == True)
