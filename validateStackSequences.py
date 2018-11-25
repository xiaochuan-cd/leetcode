class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        pushed.reverse()
        popped.reverse()

        ps = []
        pp = []

        i, j = 0, 0

        while pushed or popped:
            _p = []
            while pushed:
                _p.append(pushed.pop())
                while _p and popped[-1] == _p[-1]:
                    popped.pop()
                    _p.pop()

            while _p:
                if popped[-1] == _p[-1]:
                    popped.pop()
                else:
                    return False

        return True


if __name__ == "__main__":
    print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
