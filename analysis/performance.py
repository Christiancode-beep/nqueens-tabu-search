import time
from collections import defaultdict
from core.tabu_search import TabuSearchNQueens

class PerformanceAnalyzer:
    @staticmethod
    def analyze(n_values, trials=5):
        results = defaultdict(dict)
        for n in n_values:
            total_time = 0
            success = 0
            for _ in range(trials):
                start = time.time()
                solver = TabuSearchNQueens(n)
                solution, conflicts = solver.solve()
                total_time += time.time() - start
                if conflicts == 0:
                    success += 1
            results[n] = {
                'avg_time': total_time / trials,
                'success_rate': success / trials
            }
        return results