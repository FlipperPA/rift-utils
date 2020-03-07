from time import sleep

import pyautogui

SLEEP = 0.3
JUMPS = 30

def interact_hobert():
    pyautogui.press('escape')
    sleep(SLEEP)
    pyautogui.press('escape')
    sleep(SLEEP)
    pyautogui.press('enter')
    sleep(SLEEP)
    pyautogui.write('/tar hobert', interval=0.03)
    sleep(SLEEP)
    pyautogui.press('enter')
    sleep(SLEEP)
    pyautogui.write('/interact', interval=0.03)
    sleep(SLEEP)
    pyautogui.press('enter')
    sleep(SLEEP)


while True:
    pyautogui.moveTo(298, 681)
    for x in range(0, 6):
        pyautogui.click()
        sleep(SLEEP)

    interact_hobert()

    pyautogui.moveTo(500, 570)
    sleep(SLEEP)
    pyautogui.click()
    sleep(SLEEP)

    for x in range(0, JUMPS):
        pyautogui.press('space')
        pyautogui.sleep(SLEEP)

    interact_hobert()

    pyautogui.moveTo(550, 570)
    sleep(SLEEP)
    pyautogui.click()
    sleep(SLEEP)
