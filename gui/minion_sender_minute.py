from time import sleep

import pyautogui

for x in range(0, 9999999999):
    pyautogui.moveTo(298, 681)
    for x in range(0, 16):
        pyautogui.click()
        sleep(0.2)
    sleep(61)
