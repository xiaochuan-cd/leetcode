class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        lvl, lenw, lenh, ret = 0, len(matrix[0]), len(matrix), []
        while lvl <= int(min(lenw, lenh)/2):
            if len(ret) != lenh*lenw:
                for i in range(lvl, lenw-lvl):
                    ret.append(matrix[lvl][i])
            if len(ret) != lenh*lenw:
                for i in range(lvl+1, lenh-lvl):
                    ret.append(matrix[i][lenw-lvl-1])
            if len(ret) != lenh*lenw:
                for i in range(lenw-lvl-2, -1+lvl, -1):
                    ret.append(matrix[lenh-lvl-1][i])
            if len(ret) != lenh*lenw:
                for i in range(lenh-lvl-2, lvl, -1):
                    ret.append(matrix[i][lvl])
            lvl += 1

        return ret


if __name__ == "__main__":
    print(Solution().spiralOrder(
        [
            [1]
        ]
    ))
    print(Solution().spiralOrder(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20]
        ]
    ))
