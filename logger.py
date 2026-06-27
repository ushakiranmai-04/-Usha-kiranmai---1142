# logger.py

"""
This file is used to log errors into error.log
with date and time.
"""

import logging

# Configure logging
logging.basicConfig(
    filename="error.log",          # Log file name
    level=logging.ERROR,           # Store only ERROR messages
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(error_message):
    """
    Logs the given error message into error.log.
    """
    logging.error(error_message)