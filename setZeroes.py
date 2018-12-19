class Solution:
    # def setZeroes(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: void Do not return anything, modify matrix in-place instead.
    #     """

    #     m, n = len(matrix), len(matrix[0])
    #     l, c = [0]*m, [0]*n

    #     for i in range(m):
    #         if 0 in matrix[i]:
    #             l[i] = 1
    #     for i in range(n):
    #         for j in range(m):
    #             if matrix[j][i] == 0:
    #                 c[i] = 1
    #                 continue
    #     for i in range(m):
    #         for j in range(n):
    #             if l[i] == 1 or c[j] == 1:
    #                 matrix[i][j] = 0

    #     return matrix

    def setZeroes(self, matrix):
        """
            :type matrix: List[List[int]]
            :rtype: void Do not return anything, modify matrix in-place instead.
            """

        m, n = len(matrix), len(matrix[0])
        l, c = -1, -1

        for i in range(m):
            if 0 in matrix[i]:
                l, c = i, matrix[i].index(0)
                break

        if l != -1:

            for i in range(m):
                if 0 in matrix[i]:
                    matrix[i][c] = None

            for i in range(n):
                for j in range(m):
                    if matrix[j][i] == 0:
                        matrix[l][i] = None
                        continue

            for i in range(n):
                if matrix[l][i] != None:
                    matrix[l][i] = 0
            for i in range(m):
                if matrix[i][c] != None:
                    matrix[i][c] = 0

            for i in range(m):
                for j in range(n):
                    if matrix[i][c] == None or matrix[l][j] == None:
                        if matrix[i][j] != None:
                            matrix[i][j] = 0

            for i in range(n):
                matrix[l][i] = 0
            for i in range(m):
                matrix[i][c] = 0

        return matrix


if __name__ == "__main__":
    print(Solution().setZeroes(
        [[1]]
    ))
