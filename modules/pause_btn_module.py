import pyautogui

pause_btn_pos = (1235, 270)

# output: mouse movement
# clicks on the pause button (to pause or unpause)
def click_pause_btn():
    pyautogui.moveTo(x=pause_btn_pos[0], y=pause_btn_pos[1])
    pyautogui.click()