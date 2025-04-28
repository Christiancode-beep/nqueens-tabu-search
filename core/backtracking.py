import time


class BacktrackingNQueens:
    def __init__(self, n, visualizer=None):
        self.n = n
        self.visualizer = visualizer

    def solve(self):
        board = [-1] * self.n
        start_time = time.time()
        iterations = [0]  # Using list to pass by reference

        is_solved = self.solve_util(board, 0, iterations, start_time)

        return board if is_solved else None, iterations[0], time.time() - start_time

    def solve_util(self, board, col, iterations, start_time):
        iterations[0] += 1

        # Update visualization every 100 iterations
        if self.visualizer and iterations[0] % 100 == 0:
            self.visualizer.update_display(
                board, "Backtracking",
                time.time() - start_time,
                iterations[0],
                False
            )

        if col >= self.n:
            return True

        for row in range(self.n):
            if self.is_safe(board, col, row):
                board[col] = row

                if self.solve_util(board, col + 1, iterations, start_time):
                    return True

                board[col] = -1

        return False

    def is_safe(self, board, col, row):
        for i in range(col):
            if board[i] == row or abs(i - col) == abs(board[i] - row):
                return False
        return True