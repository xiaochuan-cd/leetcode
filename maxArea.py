class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        h, t = 0, len(height)-1
        a = 0

        while h < t:
            vh, vt = height[h], height[t]
            a = max(a, (t-h)*min(vh, vt))
            if vh < vt:
                h += 1
            else:
                t -= 1

        return a


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
