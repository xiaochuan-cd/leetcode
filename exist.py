class Solution:
    def recursive(self, can, board, word, pre):
        if len(pre) == len(word):
            return True
        for i in can:
            if (0 <= i[0] < self.shape[0]) and (0 <= i[1] < self.shape[1]) and word[len(pre)] == board[i[0]][i[1]] and i not in pre:
                pre[i] = 1
                if self.recursive([(i[0]-1, i[1]), (i[0]+1, i[1]), (i[0], i[1]-1), (i[0], i[1]+1)], board, word, pre):
                    return True
                del pre[i]
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        self.shape = (len(board), len(board[0]))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if board[i][j] == word[0]:
                    pre = {}
                    if self.recursive([(i, j)], board, word, pre):
                        return True
        return False


if __name__ == "__main__":
    print(Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "SSE"))
