import matplotlib.pyplot as plt
import numpy as np
from matplotlib.table import Table


class NQueensVisualizer:
    def __init__(self, n):
        self.fig, (self.ax_board, self.ax_table) = plt.subplots(1, 2, figsize=(14, 6))
        self.n = n
        self.setup_board()
        self.setup_table()
        plt.ion()

    def setup_board(self):
        self.ax_board.clear()
        self.ax_board.set_xticks(np.arange(0.5, self.n, 1))
        self.ax_board.set_yticks(np.arange(0.5, self.n, 1))
        self.ax_board.grid(True)
        self.ax_board.set_title("Live N-Queens Board")

    def setup_table(self):
        self.ax_table.clear()
        self.ax_table.axis('off')
        self.table_data = [
            ["Metric", "Tabu Search", "Backtracking"],
            ["Time (s)", "-", "-"],
            ["Iterations", "-", "-"],
            ["Solution Found", "-", "-"]
        ]
        self.table = self.ax_table.table(
            cellText=self.table_data,
            loc='center',
            cellLoc='center',
            colWidths=[0.3, 0.3, 0.3]
        )
        self.ax_table.set_title("Performance Comparison")
        self.table.auto_set_font_size(False)
        self.table.set_fontsize(12)
        self.table.scale(1, 2)

    def update_display(self, queens, algorithm, time_elapsed, iterations, solved):
        # Update board
        self.setup_board()
        for col, row in enumerate(queens):
            color = 'red' if self.is_under_attack(queens, col) else 'gold'
            self.ax_board.add_patch(plt.Circle((col + 0.5, row + 0.5), 0.4, color=color))

        # Update table
        row_offset = 1 if algorithm == "Tabu" else 2
        self.table_data[1][row_offset] = f"{time_elapsed:.4f}"
        self.table_data[2][row_offset] = str(iterations)
        self.table_data[3][row_offset] = "✓" if solved else "✗"

        self.table = self.ax_table.table(
            cellText=self.table_data,
            loc='center',
            cellLoc='center',
            colWidths=[0.3, 0.3, 0.3]
        )
        plt.draw()
        plt.pause(0.001)

    def is_under_attack(self, queens, col):
        for i in range(self.n):
            if i != col and (queens[i] == queens[col] or abs(i - col) == abs(queens[i] - queens[col])):
                return True
        return False

    def show_final(self):
        plt.ioff()
        plt.show()