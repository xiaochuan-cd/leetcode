class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        heights.append(0)
        st, mx = [], 0
        for i in range(len(heights)):
            while st and heights[st[-1]] >= heights[i]:
                c = st.pop()
                mx = max(mx, heights[c]*(i-st[-1]-1 if st else i))
            st.append(i)
        return mx


if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 2, 2, 2, 2, 2]))
