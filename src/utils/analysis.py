import os
import matplotlib.pyplot as plt

def count_status_occurrence(log_lines):
    """
    Counts the occurrences of each log level in the provided lines.
    
    Args:
        log_lines (list): A list of log lines to analyze.
    
    Returns:
        dict: A dictionary with log levels as keys and their occurrences as values.
    """
    levels = {"INFO": 0, "WARNING": 0, "DEBUG": 0, "ERROR": 0, "CRITICAL": 0}

    for line in log_lines:
        for level in levels.keys():
            if f" - {level} - " in line:  # Check if the log line contains the log level
                levels[level] += 1
    
    return levels


def generate_summary_report(status_occurrence):
    """
    Generates a summary report based on the log level occurrences and saves it to a file.
    
    Args:
        status_occurrence (dict): A dictionary containing log levels and their counts.
    
    Returns:
        None
    """
    # Calculate the total number of log entries
    total = sum(status_occurrence.values())
    report_lines = ["Log Analysis Summary:"]
    
    # Format the summary
    for level, count in status_occurrence.items():
        percentage = (count / total) * 100 if total > 0 else 0
        report_lines.append(f"- {level}: {count} occurrences ({percentage:.2f}%)")
    
    # Combine the report into a single string
    report = "\n".join(report_lines)
    print(report)

    # Write the report to a file
    report_file_path = os.path.join(os.path.dirname(__file__), "../../logs/report.txt")
    with open(report_file_path, "a") as file:
        file.write(report + "\n\n")


def plot_log_data(status_occurrence):
    """
    Plots the log level occurrences using a bar chart.
    
    Args:
        status_occurrence (dict): A dictionary containing log levels and their counts.
    
    Returns:
        None
    """
    levels, counts = zip(*status_occurrence.items())  # Separate log levels and counts for plotting

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(levels, counts, color='purple')
    plt.xlabel('Log Levels')
    plt.ylabel('Number of Occurrences')
    plt.title('Log Level Analysis')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
