import numpy as np
import cv2
from PIL import ImageGrab

def capture_screen():
    screenshot = ImageGrab.grab()
    return screenshot

def find_image_on_screen(screen, template_path, threshold=0.8, scale_range=(0.5, 2.0), scale_step=0.1):
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    template_original = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    if template_original is None:
        raise FileNotFoundError(f"Template not found at {template_path}")

    found = None
    best_match_val = threshold

    # Iterate over scales
    for scale in np.arange(scale_range[0], scale_range[1], scale_step):
        # Resize the template
        template = cv2.resize(template_original, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
        template_height, template_width = template.shape

        # Ensure the resized template is smaller than the screen
        screen_height, screen_width = screen_gray.shape
        if template_height > screen_height or template_width > screen_width:
            continue

        # Perform template matching
        result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= best_match_val:
            found = (int(max_loc[0] + template_width / 2), int(max_loc[1] + template_height / 2))  # Center of the match
            best_match_val = max_val

    return found
