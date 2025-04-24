from core.tabu_search import TabuSearchNQueens
from core.backtracking import BacktrackingNQueens
from analysis.performance import PerformanceAnalyzer
from analysis.comparison import AlgorithmComparator
from utils.display import print_results, print_board
import time


def main():
    print("N-Queens Solver Suite")

    # Basic demo
    n = 8
    start = time.time()
    ts = TabuSearchNQueens(n)
    solution, conflicts = ts.solve()
    print_results(n, solution, conflicts, time.time() - start)

    # Performance analysis
    print("\nPerformance Analysis:")
    perf_results = PerformanceAnalyzer.analyze([4, 8, 16])
    for n, metrics in perf_results.items():
        print(f"{n} Queens: {metrics['avg_time']:.3f}s avg, {metrics['success_rate']:.0%} success")

    # Algorithm comparison
    print("\nAlgorithm Comparison:")
    comparison_results = AlgorithmComparator.compare([4, 8, 12])
    for n, ts_time, bt_time in comparison_results:
        print(f"{n} Queens | Tabu: {ts_time:.4f}s  Backtrack: {bt_time:.4f}s" if bt_time else
              f"{n} Queens | Tabu: {ts_time:.4f}s  Backtrack: N/A")


if __name__ == "__main__":
    main()