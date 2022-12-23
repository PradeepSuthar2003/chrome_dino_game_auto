import pyautogui as pg
from PIL import Image, ImageGrab
import time


def press(key):
    pg.press(key)


def isCollide(data):
    for i in range(716, 780):
        for j in range(290, 342):
            if data[i, j] < 100:
                return True


if __name__ == '__main__':
    time.sleep(3)
    press("UP")
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        rt = isCollide(data)
        if rt:
            press("UP")
        else:
            pass
    # image.show()
