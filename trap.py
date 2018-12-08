class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) <= 2:
            return 0

        maxrs = [0]*(len(height)+1)
        for i in range(len(height)):
            ri = len(height)-i-1
            maxrs[ri] = max(height[ri], maxrs[ri+1])

        maxl, sumw = 0, 0
        for i in range(len(height)):
            maxl = max(maxl, height[i])
            sumw += max(min(maxl, maxrs[i]) - height[i], 0)

        return sumw


if __name__ == "__main__":
    print(Solution().trap([2, 1, 0, 3, 1, 0, 1, 3, 2, 0, 2, 1]))
