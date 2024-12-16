import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils.analysis import generate_summary_report, count_status_occurrence
from utils.alert import send_email, format_critical_alert
from utils.log_manager import get_logger

logger = get_logger()

class LogFileHandler(FileSystemEventHandler):
    """
    Handles file modification events for monitored log files.
    """
    def on_modified(self, event):
        if event.src_path.endswith(".log"):
            try:
                logger.info(f"Modified file: {event.src_path}")
                
                # Read new lines from the log file
                with open(event.src_path, "r") as file:
                    lines = file.readlines()
                    new_lines = lines[-5:]  # Read the last 5 lines
                    logger.info(f"New lines: {new_lines}")

                    # Analyze each line individually
                    critical_events = []
                    for line in new_lines:
                        log_line_analysis = count_status_occurrence([line])
                        logger.info(log_line_analysis)

                        # Check if the line contains a critical alert
                        if log_line_analysis.get("CRITICAL", 0) > 0:
                            critical_events.append(line)

                    # Generate a summary report
                    status_occurrence_analysis = count_status_occurrence(new_lines)
                    generate_summary_report(status_occurrence_analysis)

                    # Send critical alerts if needed
                    if critical_events:
                        email_body = format_critical_alert(critical_events)
                        send_email(
                            subject="Critical Alert from Log Monitoring System",
                            body=email_body,
                            recipients=["admin@example.com"],  # Replace with actual email
                            smtp_server="smtp.gmail.com",
                            smtp_port=587,
                            sender_email="your_email@example.com",  # Replace with your email
                            sender_password="your_password"         # Replace with your password
                        )

            except Exception as e:
                logger.error(f"Error reading log file: {e}")


def monitor_logs(directory):
    """
    Monitors the specified directory for log file changes.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"Created monitored directory: {directory}")

    event_handler = LogFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=False)
    logger.info(f"Monitoring directory: {directory}")

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Log monitoring interrupted by user.")
        observer.stop()
    observer.join()














          