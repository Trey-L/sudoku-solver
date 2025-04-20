def solve_sudoku(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10): # try numbers 1-9
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve_sudoku(grid): # recursively try to solve the rest
                return True

            grid[row][col] = 0 # reset the cell if the path failed

    return False # trigger backtracking if no number works for this cell

def is_valid(grid, num, pos):
    """Checks if placing 'num' at 'pos' (row, col) is valid."""
    row, col = pos

    # Check row
    for i in range(9):
        if grid[row][i] == num and i != col:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num and i != row:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(grid):
    """
    Finds the next empty cell (represented by 0) in the grid.
    Returns (row, col) tuple or None if no empty cell is found.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def print_grid(grid):
    """
    Prints the Sudoku grid in a readable format.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ") # Horizontal separator

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="") # Vertical separator

            if j == 8:
                print(grid[i][j] if grid[i][j] != 0 else ".")
            else:
                print(str(grid[i][j] if grid[i][j] != 0 else ".") + " ", end="")

def parse_input_string(input_str):
    """
    Parses the 81-character input string into a 9x9 grid.
    Returns the grid or None if input is invalid.
    """
    if len(input_str) != 81:
        print("Error: Input string must be exactly 81 characters long.")
        return None

    grid = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(81):
        char = input_str[i]
        row = i // 9
        col = i % 9
        if '1' <= char <= '9':
            grid[row][col] = int(char)
        elif char == '0' or char.lower() == 'x' or char == '.':
             grid[row][col] = 0
        else:
            print(f"Error: Invalid character '{char}' at position {i+1}. Use 1-9 or 0/x/.")
            return None
    return grid

if __name__ == "__main__":
    print("Sudoku Solver")
    print("Enter the puzzle as a single 81-character string, row by row, left to right, up to down.")
    print("Use digits 1-9 for filled cells and '0', 'x', or '.' for empty cells.")
    print("Example: 530070000600195000098000060800060003400803001700020006060000280000419005000080079")

    while True:
        puzzle_string = input("Enter puzzle string: ")
        board = parse_input_string(puzzle_string.strip())

        if board:
            # check if initial board has obvious conflicts before solving
            initial_valid = True
            for r in range(9):
                for c in range(9):
                    num = board[r][c]
                    if num != 0:
                       # temporarily set to 0 to check validity against others
                       board[r][c] = 0
                       if not is_valid(board, num, (r, c)):
                           print(f"\nError: Initial board has a conflict with value {num} at row {r+1}, col {c+1}.")
                           initial_valid = False
                       board[r][c] = num # put it back
                    if not initial_valid: break
                if not initial_valid: break

            if initial_valid:
                print("\nInitial Puzzle:")
                print_grid(board)

                if solve_sudoku(board):
                    print("\nSolved Puzzle:")
                    print_grid(board)
                else:
                    print("\nCould not find a solution for this puzzle.")
            break
        else:
            print("Please try entering the puzzle string again.")
