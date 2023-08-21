import pyautogui
import time

skip_ad_pos = (1175,790)
diff_height = 280
difficulties = {
    "easy"      :   300,
    "medium"    :   385,
    "hard"      :   500,
    "expert"    :   580,
    "evil"      :   675,
}

# input: a string specifying your difficulty
# output: mouse and keyboard actions
# select a board difficulty 
def select_difficulty(diff):
    if diff == "daily challenge":
        return True
    else:
        pyautogui.moveTo(difficulties.get(diff), diff_height)
        pyautogui.click()
        pyautogui.moveTo(skip_ad_pos[0], skip_ad_pos[1])
        time.sleep(6)
        pyautogui.click()
        time.sleep(3)
        return False