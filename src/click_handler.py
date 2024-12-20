import pyautogui

def click_position(position):
    """
    Simulates a mouse click at the given position.

    Args:
        position (tuple): (x, y) coordinates for the click.
    """
    try:
        # Validate the input type and length
        if not isinstance(position, tuple) or len(position) != 2:
            raise ValueError("Position must be a tuple of (x, y) coordinates.")

        # Extract and validate the coordinates
        x, y = position
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Coordinates must be integers or floats.")

        # Convert coordinates to integers
        x, y = int(x), int(y)

        print(f"Clicking at position: ({x}, {y})")
        pyautogui.click(x, y)

    except Exception as e:
        print(f"Error in click_position: {e}")
