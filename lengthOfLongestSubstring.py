class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx = 0
        d = {}
        i = 0
        while i < len(s):
            if s[i] not in d:
                d[s[i]] = i
                i += 1
            else:
                mx = max(mx, len(d.keys()))
                i = d[s[i]]+1
                d = {}

        return max(mx, len(d.keys()))


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(" "))
