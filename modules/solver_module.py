from copy import deepcopy

SIZE_OF_BOARD = 9
SIZE_OF_BLOCK = 3

class solver_class():
    def __init__(self, board):
        self.board = board
        self.unsolved_board = deepcopy(board)
        self.solve(0,0)

    # return the solved board
    def get_solved_board(self):
        return self.board
    
    # return the unsolved board
    def get_unsolved_board(self):
        return self.unsolved_board

    # check to see if a number can go in a curtain row
    def valid_row(self, row, num):
        return self.board[row].count(num) == 0
    
    # check to see if a number can go in a curtain column
    def valid_col(self, col, num):
        for row in self.board:
            if row[col] == num:
                return False
        # if the code reach this far, the num is not in the column
        return True
    
    # check to see if a number can go in a curtain box
    def valid_block(self, row, col, num):
        # calculates the coordinates of the top leftmost cell in that box
        box_tl_x = row - (row % SIZE_OF_BLOCK)
        box_tl_y = col - (col % SIZE_OF_BLOCK) 

        for sub_row in range(SIZE_OF_BLOCK):
            for sub_col in range(SIZE_OF_BLOCK):
                if self.board[box_tl_x + sub_row][box_tl_y + sub_col] == num:
                    return False
        return True
        
    # check to see if a number can go in a curtain cell with break invalidating the board
    def valid_guess(self, row, col, num):
        return self.valid_row(row, num) and self.valid_col(col, num) and self.valid_block(row, col, num)
    
    def solve(self, row, col):
        # goes thought the board in till there are no more empty squares (a zero is a empty square)
        if col == 9:
            if row == 8:
                return True
            row += 1
            col = 0      

        # skips pass any of the starting numbers (aka cell the went are not a zero)
        if self.board[row][col] != 0:
            return self.solve(row, col + 1) 
        
        # guess and check number to see if the work
        for number in range(1, 10):
            if self.valid_guess(row, col, number):
                self.board[row][col] = number
                if self.solve(row, col + 1 ): return True     # recursively call the function to solve the board
            self.board[row][col] = 0
        # if no numbers work, return false and backtrack to the previous call in the stack
        return False
        

