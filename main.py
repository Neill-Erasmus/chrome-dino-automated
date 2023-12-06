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

def main() -> None:
    pass

if __name__ == "__main__":
    main()