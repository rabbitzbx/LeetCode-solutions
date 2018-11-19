class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        count = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.' and (('row', i, num) in count or ('column', j, num) in count or (i // 3, j // 3, num) in count):
                    return False
                count.add(('row', i, num))
                count.add(('column', j, num))
                count.add((i // 3, j // 3, num))

        return True
