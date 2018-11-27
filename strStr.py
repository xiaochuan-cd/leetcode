class Solution:

    def cal_next(self, str0, next):

        if not str0:
            return

        next[0] = -1
        i, j = 0, -1

        while i < len(str0)-1:
            if j == -1 or str0[i] == str0[j]:
                i, j = i+1, j+1
                next[i] = j
            else:
                j = next[j]

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        next = [-1]*len(needle)
        self.cal_next(needle, next)

        i, j = 0, 0

        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i, j = i+1, j+1
            else:
                j = next[j]

        if j == len(needle):
            return i-j

        return -1


if __name__ == "__main__":
    print(Solution().strStr("", '11'))
