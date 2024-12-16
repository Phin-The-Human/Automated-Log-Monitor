import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger():
    """
    Configures and returns a logger instance for system logs.
    """
    # Ensure the system log directory exists
    log_dir = "logs/system"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a logger instance
    logger = logging.getLogger("LogMonitor")
    if logger.hasHandlers():
        return logger # Avoid adding duplicate handlers
    
    logger.propagate = False  # Prevent duplicate log messages
    logger.setLevel(logging.DEBUG)  # Set logging level to DEBUG (capture all levels)

    # Create a rotating file handler
    handler = RotatingFileHandler(
        filename=f"{log_dir}/system.log",  # Path to the system log file
        maxBytes=1 * 1024 * 1024,         # Rotate after 1 MB
        backupCount=5                     # Keep last 5 log files
    )
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)  # Apply the format to the handler
    logger.addHandler(handler)  # Attach the handler to the logger

    return logger
