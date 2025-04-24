def print_board(solution):
    n = len(solution)
    for row in range(n):
        print(' '.join('Q' if solution[col] == row else '.' for col in range(n)))

def print_results(n, solution, conflicts, runtime):
    print(f"\nN = {n}")
    print(f"Runtime: {runtime:.4f}s")
    print(f"Conflicts: {conflicts}")
    if conflicts == 0:
        print("Valid solution:")
        print_board(solution)
    else:
        print("Best solution found:")
        print_board(solution)