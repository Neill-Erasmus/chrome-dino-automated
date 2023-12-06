from typing import Tuple
import pyautogui
import keyboard
import time
import math

def GetGameScreenDimension() -> Tuple[int, int, int, int]:
    top, left, width, height = 293, 0, 1920, 465
    return top, left, width, height

def GetPixelColour(image, x : int, y : int) -> Tuple[int, int, int]:
    pixel_data = image.load()
    return pixel_data[x, y]

def UpdateSearchAreaEnd(x_end : int, screen_width : int, last_update : int, total_time_elapsed : float) -> Tuple[int, int]:
    if math.floor(total_time_elapsed) != last_update:
        x_end += 4
        if x_end >= screen_width:
            x_end = screen_width
        last_update = math.floor(total_time_elapsed)
    return x_end, last_update

def main() -> None:
    pass

if __name__ == "__main__":
    main()