import random
import time


class TabuSearchNQueens:
    def __init__(self, n, visualizer=None, max_iter=50):
        self.n = n
        self.max_iter = max_iter
        self.visualizer = visualizer

    def solve(self):
        current = [random.randint(0, self.n - 1) for _ in range(self.n)]
        best = current.copy()
        start_time = time.time()

        for iteration in range(self.max_iter):
            conflicts = self.calculate_conflicts(current)

            if self.visualizer:
                self.visualizer.update_display(
                    current, "Tabu",
                    time.time() - start_time,
                    iteration + 1,
                    conflicts == 0
                )

            if conflicts == 0:
                break

            current = self.get_best_neighbor(current)

        return current, iteration + 1, time.time() - start_time

    def calculate_conflicts(self, queens):
        return sum(
            1 for i in range(self.n)
            for j in range(i + 1, self.n)
            if queens[i] == queens[j] or abs(i - j) == abs(queens[i] - queens[j])
        )

    def get_best_neighbor(self, queens):
        # Find most conflicted column
        col = max(
            range(self.n),
            key=lambda c: sum(
                1 for i in range(self.n)
                if i != c and (queens[i] == queens[c] or abs(i - c) == abs(queens[i] - queens[c]))
            )
        )

        # Find best row for that column
        best_row = min(
            range(self.n),
            key=lambda r: self.calculate_conflicts(queens[:col] + [r] + queens[col + 1:])
        )

        return queens[:col] + [best_row] + queens[col + 1:]