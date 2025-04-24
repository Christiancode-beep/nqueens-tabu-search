import random
from collections import deque


class TabuSearchNQueens:
    def __init__(self, n, tabu_tenure=5, max_iterations=10000):
        self.n = n
        self.tabu_tenure = tabu_tenure
        self.max_iterations = max_iterations
        self.tabu_list = deque(maxlen=tabu_tenure)

    def initialize_solution(self):
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def calculate_conflicts(self, solution):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solution[i] == solution[j] or abs(i - j) == abs(solution[i] - solution[j]):
                    conflicts += 1
        return conflicts

    def generate_neighbors(self, solution):
        neighbors = []
        for col in range(self.n):
            for row in range(self.n):
                if row != solution[col]:
                    neighbor = solution.copy()
                    neighbor[col] = row
                    neighbors.append((col, row, neighbor))
        return neighbors

    def solve(self):
        current_solution = self.initialize_solution()
        best_solution = current_solution.copy()
        best_conflicts = self.calculate_conflicts(current_solution)

        for iteration in range(self.max_iterations):
            if best_conflicts == 0:
                break

            neighbors = self.generate_neighbors(current_solution)
            best_neighbor = None
            best_neighbor_conflicts = float('inf')
            best_move = None

            for col, new_row, neighbor in neighbors:
                move = (col, current_solution[col], new_row)
                conflicts = self.calculate_conflicts(neighbor)

                if (conflicts < best_conflicts) or (move not in self.tabu_list):
                    if conflicts < best_neighbor_conflicts:
                        best_neighbor = neighbor
                        best_neighbor_conflicts = conflicts
                        best_move = move

            if best_neighbor is None:
                continue

            current_solution = best_neighbor
            self.tabu_list.append(best_move)

            if best_neighbor_conflicts < best_conflicts:
                best_solution = current_solution.copy()
                best_conflicts = best_neighbor_conflicts

        return best_solution, best_conflicts