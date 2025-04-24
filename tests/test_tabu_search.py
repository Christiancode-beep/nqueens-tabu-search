import pytest
from ..core.tabu_search import TabuSearchNQueens

class TestTabuSearch:
    @pytest.fixture
    def solver(self):
        return TabuSearchNQueens(8)

    def test_initialization(self, solver):
        assert solver.n == 8
        assert solver.tabu_tenure == 5
        assert solver.max_iterations == 10000

    def test_initial_solution(self, solver):
        solution = solver.initialize_solution()
        assert len(solution) == 8
        assert all(0 <= row < 8 for row in solution)

    def test_conflict_calculation(self):
        solver = TabuSearchNQueens(4)
        # Test known configuration
        assert solver.calculate_conflicts([0, 0, 0, 0]) == 6  # All in same row
        assert solver.calculate_conflicts([0, 1, 2, 3]) == 2  # Diagonal conflicts
        assert solver.calculate_conflicts([1, 3, 0, 2]) == 0  # Valid solution

    def test_neighbor_generation(self, solver):
        neighbors = solver.generate_neighbors([0]*8)
        assert len(neighbors) == 8*7  # 8 columns, 7 possible rows each
        for col, new_row, neighbor in neighbors:
            assert neighbor[col] == new_row

    def test_full_solution(self):
        solver = TabuSearchNQueens(4, max_iterations=1000)
        solution, conflicts = solver.solve()
        assert conflicts == 0
        assert solver.calculate_conflicts(solution) == 0

    def test_tabu_list_management(self, solver):
        move = (0, 0, 1)
        solver.tabu_list.append(move)
        assert move in solver.tabu_list
        # Test tabu list expiration (using deque maxlen)
        for _ in range(solver.tabu_tenure + 1):
            solver.tabu_list.append((0, 0, 0))
        assert move not in solver.tabu_list