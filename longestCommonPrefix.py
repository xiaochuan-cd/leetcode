class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''

        r = ''
        i = 0

        while True:
            c = None
            for _, v in enumerate(strs):
                if len(v) <= i or (c != None and c != v[i]):
                    return r
                c = v[i]
            r += c
            i += 1

        return r


if __name__ == "__main__":
    print(Solution().longestCommonPrefix([]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
