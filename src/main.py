import os
from utils.monitor import monitor_logs
from utils.log_manager import get_logger

logger = get_logger()

def main():
    """
    Entry point for the Automated Log Monitoring System.
    """
    monitored_directory = os.getenv("LOG_DIR", "./logs/monitored")  # Default directory
    
    if not os.path.exists(monitored_directory):
        os.makedirs(monitored_directory)
        logger.info(f"Created monitored directory: {monitored_directory}")
    
    logger.info("Starting the Automated Log Monitoring System...")
    logger.info("Debug: About to call monitor_logs")  # Debug log

    # Call the monitoring function
    monitor_logs(monitored_directory)

if __name__ == "__main__":
    main()


