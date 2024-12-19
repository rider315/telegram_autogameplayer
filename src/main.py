import cv2
import time
from image_detection import capture_screen, find_image_on_screen
from click_handler import click_position
from logger import log_action

# Main configuration
THRESHOLD = 0.8
TEMPLATE_PATH = "images/icon1.png"

def main():
    print("Starting auto-clicker...")
    last_click_time = 0
    click_delay = 0.1  # Minimum time between clicks

    while True:
        try:
            # Capture the entire screen
            screen = capture_screen()

            # Find the template in the screen
            try:
                position = find_image_on_screen(screen, TEMPLATE_PATH, THRESHOLD)

                if position and (time.time() - last_click_time) > click_delay:
                    print(f"Template found at {position}. Clicking...")
                    log_action("Template Found", f"Position: {position}")
                    click_position(position)
                    log_action("Click Performed", f"Position: {position}")
                    last_click_time = time.time()

            except FileNotFoundError as e:
                print(e)
                log_action("Error", str(e))

        except Exception as e:
            print(f"Unexpected error: {e}")
            log_action("Critical Error", str(e))

if __name__ == "__main__":
    main()
