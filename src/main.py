import os
import time
from image_detection import capture_screen, find_image_on_screen
from click_handler import click_position
from logger import log_action

# Main configuration
THRESHOLD = 0.8
CLICK_DELAY = 0.1  # Minimum time between clicks per icon
SCALE_RANGE = (0.5, 2.0)
SCALE_STEP = 0.1
IMAGE_FOLDER = "images"

def main():
    print("Starting auto-clicker...")
    last_click_times = {}

    # Get all template paths
    templates = [os.path.join(IMAGE_FOLDER, f) for f in os.listdir(IMAGE_FOLDER) if f.endswith(".png")]

    while True:
        try:
            # Capture the screen
            screen = capture_screen()

            # Iterate over each template
            for template_path in templates:
                try:
                    position = find_image_on_screen(screen, template_path, THRESHOLD, SCALE_RANGE, SCALE_STEP)

                    if position:
                        current_time = time.time()
                        if (template_path not in last_click_times) or \
                                (current_time - last_click_times[template_path] > CLICK_DELAY):
                            print(f"Template {template_path} found at {position}. Clicking...")
                            log_action("Template Found", f"Template: {template_path}, Position: {position}")
                            click_position(position)
                            log_action("Click Performed", f"Template: {template_path}, Position: {position}")
                            last_click_times[template_path] = current_time

                except FileNotFoundError as e:
                    print(f"Error: {e}")
                    log_action("Error", str(e))

        except Exception as e:
            print(f"Unexpected error: {e}")
            log_action("Critical Error", str(e))

if __name__ == "__main__":
    main()
