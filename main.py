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

def IsObstacleDetected(screen_image, start_x : int, end_x : int, search_y : int, search_y2 : int) -> bool:
    background_color = GetPixelColour(screen_image, 440, 30)
    for x_pos in reversed(range(start_x, end_x)):
        if (GetPixelColour(screen_image, x_pos, search_y) != background_color or GetPixelColour(screen_image, x_pos, search_y2) != background_color):
            return True
    return False

def main() -> None:
    top, left, screen_width, screen_height = GetGameScreenDimension()
    last_update_second = 0
    total_time_elapsed = 0
    search_y, search_x_start, search_x_end = 350, 435, 450
    search_y2 = 275
    while True:
        start_time = time.time()
        if keyboard.is_pressed("q"):
            break
        search_x_end, last_update_second = UpdateSearchAreaEnd(search_x_end, screen_width, last_update_second, total_time_elapsed)
        game_screen = pyautogui.screenshot(region=(left, top, screen_width, screen_height))
        if IsObstacleDetected(game_screen, search_x_start, search_x_end, search_y, search_y2):
            keyboard.press(" ")
        elapsed_time = time.time() - start_time
        total_time_elapsed += elapsed_time

if __name__ == "__main__":
    main()