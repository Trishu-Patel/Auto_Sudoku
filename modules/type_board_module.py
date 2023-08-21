import pyautogui
from modules.pause_btn_module import click_pause_btn

# input: top-left cell position, a solved board list, a unsolved board list
# ouput: keyboard and mouse actions
# type in the solved board into the website
def export_board(start_pos, solved_board, unsolved_board):
    click_pause_btn()
    pyautogui.moveTo(start_pos[0],start_pos[1])
    pyautogui.click()
    for y in range(9):
        for x in range(9):
            if y % 2 == 0:
                if unsolved_board[y][x] == 0:
                    pyautogui.press(str(solved_board[y][x]))
                pyautogui.press("right")
            else:
                if unsolved_board[y][8 - x] == 0:
                    pyautogui.press(str(solved_board[y][8 - x]))
                pyautogui.press("left")
        pyautogui.press("down")
                  