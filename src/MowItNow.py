from src.LawnSolver import LawnSolver


def run(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    cleaned_lines = [value.strip() for value in lines]

    max_values = cleaned_lines[0].split()
    cleaned_lines.pop(0)

    solver = LawnSolver(int(max_values[0]), int(max_values[1]))
    initial_position = ""
    i = 0
    for line in cleaned_lines:
        i += 1
        if i % 2 == 0:
            print(solver.solve(initial_position, line))
            continue
        initial_position = line
