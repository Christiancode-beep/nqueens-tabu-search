class BacktrackingNQueens:
    def __init__(self, n):
        self.n = n
        self.solution = None

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[i] == row or abs(board[i] - row) == abs(i - col):
                return False
        return True

    def solve(self, col=0, board=None):
        if board is None:
            board = [-1] * self.n
        if col >= self.n:
            self.solution = board.copy()
            return True
        for row in range(self.n):
            if self.is_safe(board, row, col):
                board[col] = row
                if self.solve(col + 1, board):
                    return True
                board[col] = -1
        return False