class Solution:

    def __init__(self):
        self.line, self.col, self.blk = [[], [], [], [], [], [], [], [], []], [
            [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []]

    def conflict(self, i, j, item):
        if item == '.':
            return False
        if item in self.line[i]:
            return True
        if item in self.col[j]:
            return True
        if item in self.blk[int(i/3)*3+int(j/3)]:
            return True
        return False

    def append(self, i, j, item):
        self.line[i].append(item)
        self.col[j].append(item)
        self.blk[int(i/3)*3+int(j/3)].append(item)

    def pop(self, i, j):
        self.line[i].pop()
        self.col[j].pop()
        self.blk[int(i/3)*3+int(j/3)].pop()

    def init(self, board):
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if not self.conflict(i, j, item):
                    if item != '.':
                        self.append(i, j, int(item))
                else:
                    assert(False)

    def recursive(self, i, j, board):

        if i == 9:
            return True

        item = board[i][j]
        ir, jr = i, j + 1
        if jr == 9:
            ir, jr = ir + 1, 0

        r = False

        if item == '.':
            for itemx in range(1, 10, 1):
                if self.conflict(i, j, itemx):
                    continue
                self.append(i, j, itemx)
                r = self.recursive(ir, jr, board)
                self.pop(i, j)
                if r:
                    board[i][j] = str(itemx)
                    break
        else:
            r = self.recursive(ir, jr, board)

        return r

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        self.init(board)
        self.recursive(0, 0, board)


if __name__ == "__main__":
    b = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    Solution().solveSudoku(b)
    print(b)
