class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        st, mx = [], 0
        for i in range(len(heights)):
            while st and heights[st[-1]] >= heights[i]:
                c = st.pop()
                mx = max(mx, heights[c]*(i-st[-1]-1 if st else i))
            st.append(i)
        return mx

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        heights, res = [0]*len(matrix[0]), 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            res = max(res, self.largestRectangleArea(heights))
        return res


if __name__ == "__main__":
    print(Solution().maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
    ))
