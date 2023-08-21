# Website: Sudoku.com

from modules.ocr_module import screen_grab_board
from modules.solver_module import solver_class
from modules.type_board_module import export_board

# input: a 2d list
# output: types the contains of the 2d array into the terminal in a nice format
def print_board(board):
    for row in board:
        print(row)

# dc = select_difficulty("evil")
print("Starting Auto Sudoku")

# get the screenshot of the sudoku board and converts it into a 2d list of int
scanned_board, start_pos = screen_grab_board(daily_challenge=False)
print_board(scanned_board)

# solves the board
solver = solver_class(board=scanned_board)
solved_board = solver.get_solved_board()
unsolved_board = solver.get_unsolved_board()

# outputs mouse and keyboard command onto Sudoku.com
export_board(start_pos, solved_board, unsolved_board)
print("Done!")


