class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()
        r = s.rfind(' ')
        return len(s) - r - 1


if __name__ == "__main__":
    print(Solution().lengthOfLastWord(""))
