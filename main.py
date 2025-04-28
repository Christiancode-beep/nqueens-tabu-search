from core.tabu_search import TabuSearchNQueens
from core.backtracking import BacktrackingNQueens
from utils.visualizer import NQueensVisualizer
import matplotlib.pyplot as plt


def main():
    print("N-Queens Solver with Live Visualization")
    n = int(input("Enter number of queens (4-12 recommended): "))

    # Initialize visualizer
    visualizer = NQueensVisualizer(n)

    # Run Tabu Search
    print("\nRunning Tabu Search...")
    ts_solver = TabuSearchNQueens(n, visualizer=visualizer)
    ts_solution, ts_iters, ts_time = ts_solver.solve()

    # Run Backtracking (for N <= 12)
    bt_solution = bt_iters = bt_time = None
    if n <= 12:
        print("Running Backtracking...")
        bt_solver = BacktrackingNQueens(n, visualizer=visualizer)
        bt_solution, bt_iters, bt_time = bt_solver.solve()

    # Final display
    visualizer.update_display(
        ts_solution, "Tabu", ts_time, ts_iters,
        ts_solver.calculate_conflicts(ts_solution) == 0
    )

    if bt_solution is not None:
        visualizer.update_display(
            bt_solution, "Backtracking", bt_time, bt_iters,
            True  # Backtracking always finds solution if exists
        )

    # Show final results
    print("\nResults:")
    print(f"Tabu Search: {ts_time:.4f}s, {ts_iters} iterations")
    if bt_solution:
        print(f"Backtracking: {bt_time:.4f}s, {bt_iters} iterations")

    visualizer.show_final()


if __name__ == "__main__":
    main()