import logging

# Configure logging
logging.basicConfig(
    filename="auto_clicker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_action(action, details=""):
    """
    Logs actions performed by the script.

    Args:
        action (str): Description of the action.
        details (str): Additional details.
    """
    logging.info(f"{action} | {details}")
