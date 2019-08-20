import pyautogui
from time import sleep


for x in range(1, 1000):
    for y in range(1, 20):
        pyautogui.moveTo(1816, 183)
        pyautogui.click()
        sleep(0.1)
        pyautogui.moveTo(600, 600)
        pyautogui.click()
        sleep(1)
        pyautogui.click()
        sleep(1)
        pyautogui.moveTo(1061, 985)
        pyautogui.click()
        sleep(1)

    pyautogui.moveTo(298, 681)
    for z in range(0, 2):
        pyautogui.click()
        sleep(0.4)
