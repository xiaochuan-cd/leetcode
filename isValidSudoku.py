class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        line, col, blk = [[], [], [], [], [], [], [], [], []], [
            [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []]

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == '.':
                    continue
                l, c, b = line[i], col[j], blk[int(i/3)*3+int(j/3)]
                if item in l:
                    return False
                if item in c:
                    return False
                if item in b:
                    return False
                l.append(item)
                c.append(item)
                b.append(item)
        return True


if __name__ == "__main__":
    print(Solution().isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))

    print(Solution().isValidSudoku([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
