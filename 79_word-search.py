class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not len(word):
            return True
        if not len(board) or not len(board[0]):
            return False

        self.board, self.word = board, word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.move(set(), (i, j)):
                        return True

        return False

    def move(self, path, current):
        i, j = current
        newPath = path.copy()
        if i >= 0 and i < len(self.board) and j >= 0 and j < len(self.board[0]) and self.board[i][j] == self.word[len(path)]:
            newPath.add(current)
        if len(newPath) == len(path):
            return False
        if len(newPath) == len(self.word):
            return True
        return self.move(newPath, (i - 1, j)) or \
            self.move(newPath, (i + 1, j)) or \
            self.move(newPath, (i, j - 1)) or \
            self.move(newPath, (i, j + 1))
