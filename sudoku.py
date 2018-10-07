def solver(puzzle):
    blank_counts = len([True for i in range(9) for j in range(9) if puzzle[i][j] == 0])
    if blank_counts == 0: return puzzle

    while blank_counts > 0:
        found_one_choice = False
        for i in range(9):
            for j in range(9):
                choices = possibilities(puzzle, i, j)
                print(choices)
                if len(choices) == 1:
                    found_one_choice = True
                    if puzzle[i][j] == 0:
                        blank_counts -= 1
                    puzzle[i][j] = choices[0]
                elif len(choices) == 0:
                    return []

        if not found_one_choice:
            return []
    return puzzle

def possibilities(puzzle, row, column):
    if puzzle[row][column] > 0:
        return [puzzle[row][column]]
    invalid_vals = set()

    for i in range(9):
        if puzzle[row][i] > 0:
            invalid_vals.add(puzzle[row][i])
        if puzzle[i][column] > 0:
            invalid_vals.add(puzzle[i][column])

    grid_col_start = (column // 3) * 3
    grid_row_start = (row // 3) * 3
    grid_col_end = (column // 3 + 1) * 3
    grid_row_end = (row // 3 + 1) * 3

    for i in range(grid_row_start, grid_row_end):
        for j in range(grid_col_start, grid_col_end):
            if puzzle[i][j] > 0:
                invalid_vals.add(puzzle[i][j])

    return [i for i in range(1, 10) if i not in invalid_vals]

puzzle = [
    [0,3,0,0,0,5,0,0,8],
    [1,2,0,3,0,0,0,0,0],
    [7,8,0,0,2,0,0,0,5],
    [0,7,0,0,0,6,0,0,0],
    [0,0,3,0,0,0,6,0,0],
    [0,0,0,8,0,0,0,4,0],
    [4,0,0,0,7,0,0,5,3],
    [0,0,0,0,0,2,0,6,4],
    [5,0,0,9,0,0,0,7,0]
]
print(solver(puzzle))
