sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 1, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def solve_board(board):
    # find empty cell
    empty_cell = find_empty(board)
    # if not empty cell then solved (return True)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    # check which num between 1 and 9 is valid for row, col
    for i in range(1, 10):
        # if valid position then update board
        if check_valid(board, i, (row, col)):
            board[row][col] = i
            # return True if board is solved else backtrack
            if solve_board(board):
                return True
            # backtrack
            board[row][col] = 0

    return False


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("________________________")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # (row, column)

    return None


def check_valid(board, num, pos):
    # Check if the num is already in the row
    # return False if it is present
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check if the num is already present in the column
    # return False if it is present
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range((box_y * 3), (box_y * 3 + 3)):
        for j in range((box_x * 3), (box_x * 3 + 3)):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


print_board(sudoku_board)
print("**********************")
solve_board(sudoku_board)
print_board(sudoku_board)
