import pyautogui
import cv2
import numpy as np
import pytesseract
from modules.pause_btn_module import click_pause_btn

configurations = "--psm 10 outputbase digits"
board_length = 632
board_number = []

# for reg size board
# cell_length = 69
# cell_border = 5

# for smaller size board 0.5
cell_length = 34
cell_border = 5

def screen_grab_board(daily_challenge):
    # the daily challenge and classic boards are different heights on screen
    if daily_challenge:
        start_pos = (163, 310)
    else:
        start_pos = (163, 327)

    # get screenshot
    screenshot_region = (start_pos[0], start_pos[1], board_length, board_length)
    img = np.array(pyautogui.screenshot(region=screenshot_region))

    click_pause_btn()

    # processes screenshot for better OCR
    img_processed = get_processed_img(img)

    for y in range(9):
        board_number_row = []
        for x in range(9):
            # finds and parses the image of the cell
            cell_img_x = x * cell_length + ((x // 3) * cell_border)
            cell_img_y = y * cell_length + ((y // 3) * cell_border)
            cell_img = img_processed[cell_img_y:cell_img_y + cell_length ,cell_img_x:cell_img_x + cell_length]

            # preform OCR
            cell_num = pytesseract.image_to_string(cell_img, config=configurations)

            # filter noise from the OCR output and converts it into a format suitable for the solver module
            cell_num = cell_num.replace("\n",'')
            if len(cell_num) != 1: cell_num = "0"
            cell_num = int(cell_num)

            board_number_row.append(cell_num)
        board_number.append(board_number_row)
    return board_number, start_pos


# input: image
# output: processed image
# applies a vary of different image preprocessing techniques to the image
def get_processed_img(img):
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rct, img_black_white = cv2.threshold(img_grey, 80, 255, cv2.THRESH_BINARY_INV)
    img_processed = cv2.resize(img_black_white, dsize=(0,0), fx=0.5, fy=0.5)
    # kernel = np.ones((2,2), np.uint8)
    # img_processed = cv2.dilate(img_processed, kernel, iterations=1)
    return img_processed