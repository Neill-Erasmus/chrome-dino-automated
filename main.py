from typing import Tuple
import pyautogui
import keyboard
import time
import math

def GetGameScreenDimension() -> Tuple[int, int, int, int]:
    """
    GetGameScreenDimension Function

    Returns the dimensions of the game screen.

    Returns:
    Tuple[int, int, int, int]: Dimensions (top, left, width, height) of the game screen.
    """
    
    top, left, width, height = 293, 0, 1920, 465
    return top, left, width, height

def GetPixelColour(image, x : int, y : int) -> Tuple[int, int, int]:
    """
    GetPixelColour Function

    Gets the color of a pixel at a given position in an image.

    Parameters:
    - image: The image to get the pixel color from.
    - x: X-coordinate of the pixel.
    - y: Y-coordinate of the pixel.

    Returns:
    Tuple[int, int, int]: RGB values of the pixel color.
    """
    
    pixel_data = image.load()
    return pixel_data[x, y]

def UpdateSearchAreaEnd(x_end : int, screen_width : int, last_update : int, total_time_elapsed : float) -> Tuple[int, int]:
    """
    UpdateSearchAreaEnd Function

    Updates the end position of the search area based on time.

    Parameters:
    - x_end: Current end position of the search area.
    - screen_width: Width of the game screen.
    - last_update: Last time the search area was updated.
    - total_time_elapsed: Total time elapsed since the script started.

    Returns:
    Tuple[int, int]: Updated end position and the last time updated.
    """
    
    if math.floor(total_time_elapsed) != last_update:
        x_end += 4
        if x_end >= screen_width:
            x_end = screen_width
        last_update = math.floor(total_time_elapsed)
    return x_end, last_update

def IsObstacleDetected(screen_image, start_x : int, end_x : int, search_y : int, search_y2 : int) -> bool:
    """
    IsObstacleDetected Function

    Checks if obstacles are detected in the specified region.

    Parameters:
    - screen_image: The image of the game screen.
    - start_x: Starting X-coordinate of the search area.
    - end_x: Ending X-coordinate of the search area.
    - search_y: Y-coordinate of the search area.
    - search_y2: Additional Y-coordinate for a secondary search area.

    Returns:
    bool: True if an obstacle is detected, False otherwise.
    """
    
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