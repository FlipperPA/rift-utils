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
MOTE_COLLECTOR = (728, 877)
SHARDS = {
    "Deepwood": (1157, 278),
    "Faeblight": (1157, 298),
    "Greybriar": (1157, 318),
    "Haliol": (1157, 338),
    "Laethys": (1157, 358),
    "Seastone": (1157, 378),
    "Wolfbane": (1157, 398),
}


def action(coords, sleep_secs=1, repeat=1):
    pyautogui.moveTo(coords[0], coords[1])
    for x in range(0, repeat):
        pyautogui.click()
        sleep(sleep_secs)


def shard_hop(shard="Deepwood"):
    # Portrait
    pyautogui.moveTo(896, 118)
    pyautogui.rightClick()
    sleep(0.5)
    pyautogui.moveTo(1063, 270)
    sleep(0.5)
    pyautogui.moveTo(SHARDS[shard][0], SHARDS[shard][1])
    sleep(0.5)
    pyautogui.click()


current_shard = "Deepwood"

for x in range(0, 999999):
    for five_min_loop in range(0, 12):
        print("In five minute loop...")
        for x in range(1, 3):
            pyautogui.press("tab")
            action(RANGED, 1, 3)
            pyautogui.keyDown('a')
            sleep(0.7)
            pyautogui.keyUp('a')
            pyautogui.press("tab")

            action(MOTE_COLLECTOR, 3)
            action(RANGED, 1, 3)
            action(AE, 1, 1)
            action(HEAL_SMALL, 0, 1)

        action(HEAL_BIG, 1, 3)
        action(MINIONS, 0.3, 6)

    shard_hop(current_shard)

    if(current_shard == "Deepwood"):
        current_shard = "Faeblight"
    elif(current_shard == "Faeblight"):
        current_shard = "Greybriar"
    elif(current_shard == "Greybriar"):
        current_shard = "Haliol"
    elif(current_shard == "Haliol"):
        current_shard = "Laethys"
    elif(current_shard == "Laethys"):
        current_shard = "Seastone"
    elif(current_shard == "Seastone"):
        current_shard = "Wolfbane"
    else:
        current_shard = "Deepwood"

    sleep(10)
