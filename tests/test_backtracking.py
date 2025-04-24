import pytest
from ..core.backtracking import BacktrackingNQueens

class TestBacktracking:
    @pytest.mark.parametrize("n,expected", [
        (1, True),
        (4, True),
        (8, True),
        (12, True)  # Warning: This might be slow
    ])
    def test_solutions(self, n, expected):
        solver = BacktrackingNQueens(n)
        assert solver.solve() == expected
        assert len(solver.solution) == n
        assert all(0 <= row < n for row in solver.solution)

    def test_safety_check(self):
        solver = BacktrackingNQueens(4)
        # Valid partial solution
        assert solver.is_safe([0, 2, -1, -1], 3, 2)
        # Invalid row
        assert not solver.is_safe([0, 0, -1, -1], 0, 2)
        # Invalid diagonal
        assert not solver.is_safe([0, 2, -1, -1], 1, 2)