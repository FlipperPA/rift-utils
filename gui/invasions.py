"""
Script to automatically build and target invasions at sourcewells to
complete invasion achievements.
"""
from time import sleep

import pyautogui

RANGED = (1091, 823)
AE = (1247, 1016)
MINIONS = (298, 677)
HEAL_SMALL = (1147, 935)
HEAL_BIG = (987, 1013)
PLANAR_BUILD = (1633, 861)
PLANAR_CHARGE_1 = (1900, 621)
PLANAR_CHARGE_2 = (1900, 671)


def action(coords, sleep_secs=1, repeat=1):
    pyautogui.moveTo(coords[0], coords[1])
    for x in range(0, repeat):
        pyautogui.click()
        sleep(sleep_secs)


for x in range(0, 99999):
    for hour_loop in range(0, 6):
        for five_min_loop in range(0, 12):
            for x in range(1, 3):
                pyautogui.press("tab")
                action(RANGED, 1, 3)
                pyautogui.keyDown('a')
                sleep(0.7)
                pyautogui.keyUp('a')
                pyautogui.press("tab")

                action(RANGED, 1, 3)
                action(AE, 1, 1)
                action(HEAL_SMALL, 0, 1)

            action(HEAL_BIG, 1, 3)
            action(MINIONS, 0.3, 6)

        pyautogui.moveTo(RANGED[0], RANGED[1])
        pyautogui.click()
        pyautogui.press("enter")
        pyautogui.typewrite("/tar dormant")
        pyautogui.press("enter")
        action(HEAL_SMALL, 0, 1)
        action(PLANAR_BUILD, 6.5, 1)
        action(HEAL_SMALL, 0, 1)
        action(HEAL_BIG, 1, 3)

    action(PLANAR_CHARGE_1, 1, 1)
    action(PLANAR_CHARGE_2, 1, 1)
