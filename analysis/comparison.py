import time
from core.tabu_search import TabuSearchNQueens
from core.backtracking import BacktrackingNQueens


class AlgorithmComparator:
    @staticmethod
    def compare(n_values):
        results = []
        for n in n_values:
            # Tabu Search
            start = time.time()
            TabuSearchNQueens(n).solve()
            ts_time = time.time() - start

            # Backtracking
            bt_time = None
            if n <= 12:
                start = time.time()
                bt = BacktrackingNQueens(n)
                bt.solve()
                bt_time = time.time() - start

            results.append((n, ts_time, bt_time))
        return results