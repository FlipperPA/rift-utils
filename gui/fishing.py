from time import sleep

import pyautogui
from pyscreenshot import grab

# Goboro Reef looking south, 4091, 6597
# In dark corner above rocks
# Brevane / Cape Jule 8471, 11970 looking NW
# Dusken / Steppes 15268, 8354 looking N / NW
FISH_START = (730, 821)
CAST_POINT = (725, 418)  # Cape Jule
CAST_POINT = (739, 501)  # Steppes
CAPTURE_REGION = (
    CAST_POINT[0] - 10,
    CAST_POINT[1] - 10,
    CAST_POINT[0] + 10,
    CAST_POINT[1] + 10,
)
THRESHOLD = 4.00

while True:
    pyautogui.moveTo(298, 681)
    for x in range(0, 6):
        pyautogui.click()
        sleep(0.3)

    pyautogui.moveTo(FISH_START[0], FISH_START[1])
    pyautogui.click()
    sleep(0.2)
    pyautogui.moveTo(CAST_POINT[0], CAST_POINT[1])
    pyautogui.click()
    sleep(0.2)

    original_image = grab(
        bbox=CAPTURE_REGION,
    )
    for x in range(0, 70):
        current_image = grab(
            bbox=CAPTURE_REGION,
        )

        pairs = zip(original_image.getdata(), current_image.getdata())
        if len(original_image.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1 - p2) for p1, p2 in pairs)
        else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

        ncomponents = original_image.size[0] * original_image.size[1] * 3
        diff_pct = (dif / 255.0 * 100) / ncomponents
        print(f"{x} Difference (percentage): {diff_pct}")

        # Use 1.75 for Ghar Station in Gobor
        # Use 1.00 for Tarken Ascent
        if diff_pct > THRESHOLD:
            pyautogui.rightClick()
            sleep(0.3)
