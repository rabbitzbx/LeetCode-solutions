class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.count = set()
        self.record()
        self.solve()

    def solve(self):
        row, col = self.find()
        if row == -1 and col == -1:
            return True
        for i in range(1, 10):
            i = str(i)
            if self.valid(i, row, col):
                self.add(i, row, col)
                if self.solve():
                    return True
                self.remove(i, row, col)
        return False

    def find(self):
        for i in range(9):
            for j in range(9):
                num = self.board[i][j]
                if num == '.':
                    return i, j
        return -1, -1

    def add(self, num, row, col):
        self.board[row][col] = num
        self.recordItem(num, row, col)

    def remove(self, num, row, col):
        self.board[row][col] = '.'
        self.count.remove(('row', row, num))
        self.count.remove(('col', col, num))
        self.count.remove((row // 3, col // 3, num))

    def record(self):
        for i in range(9):
            for j in range(9):
                num = self.board[i][j]
                if num != '.':
                    self.recordItem(num, i, j)

    def recordItem(self, num, row, col):
        self.count.add(('row', row, num))
        self.count.add(('col', col, num))
        self.count.add((row // 3, col // 3, num))

    def valid(self, num, row, col):
        if ('row', row, num) in self.count or ('col', col, num) in self.count or (row // 3, col // 3, num) in self.count:
            return False
        return True
