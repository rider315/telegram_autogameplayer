import pyautogui
import time

def select_region(min_width=100, min_height=100):
    """
    Allows the user to define a rectangular region on the screen by clicking two points.
    Automatically adjusts the coordinates to ensure a valid rectangle.

    Returns:
        tuple: (left, top, width, height) defining the rectangular region.
    """
    try:
        print("Move your mouse to the first point and press ENTER.")
        input("Press ENTER when ready...")
        x1, y1 = pyautogui.position()
        print(f"First point: ({x1}, {y1})")

        time.sleep(1)

        print("Move your mouse to the second point and press ENTER.")
        input("Press ENTER when ready...")
        x2, y2 = pyautogui.position()
        print(f"Second point: ({x2}, {y2})")

        left = min(x1, x2)
        right = max(x1, x2)
        top = min(y1, y2)
        bottom = max(y1, y2)

        width = right - left
        height = bottom - top

        if width < min_width or height < min_height:
            print(f"Selected region is too small (Minimum size: {min_width}x{min_height}). Try again.")
            return None

        print(f"Screen region selected: (Left: {left}, Top: {top}, Width: {width}, Height: {height})")
        return left, top, width, height

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
