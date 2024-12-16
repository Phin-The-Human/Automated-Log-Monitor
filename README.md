# Automated Log File Monitoring and Alert System 📊🛠️
The Automated Log File Monitoring and Alert System is a Python-based project designed to monitor log files in real-time, generate detailed summary reports, and send email alerts for critical events. It leverages libraries like Watchdog for file monitoring, Matplotlib for visualizations, and SMTP for email alerts, making it a comprehensive solution for log management and analysis.

# Features
- Real-Time Monitoring: Tracks changes in specified log files and reacts instantly.
- Summary Report Generation: Creates concise reports summarizing log levels and their occurrences.
- Email Alerts: Sends notifications for critical events directly to your inbox. 
- Customizable Paths: Easily set paths for monitored logs and system logs using environment variables. 
- Extensible: Well-structured and modular code for easy enhancement and future integration with tools like Docker. 

# Getting Started

### Prerequisites

- Python 3.9 or higher 

- Virtual environment management tool (e.g., venv or virtualenv)

### Installation
1. Clone the Repository:
```bash
git clone https://github.com/Phin-The-Human/Automated-Log-Monitor.git
cd Automated-Log-Monitor
```
2. Create and Activate a Virtual Environment: 
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows:venv\Scripts\activate
```
3. Install Dependencies:
```bash
pip install -r requirements.txt
```
4. Set Up Environment Variables:
Create a .env file in the project root with the following content:
```bash
ENABLE_EMAIL_ALERTS=true
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password
EMAIL_RECEIVER=receiver-email@gmail.com
LOG_DIR=./logs/monitored
```
Replace placeholders (your-email, your-app-password, etc.) with actual values.

5. Run the Application:
```bash
python src/main.py
```

# How It Works 

### Workflow

1. The application monitors changes in the specified log directory (LOG_DIR). 

2. When a log file is modified, the system:

- Reads and processes the new log entries.

- Analyzes the log levels (e.g., INFO, WARNING, ERROR, CRITICAL).

- Updates a summary report stored in logs/report.txt.

- Sends email alerts for critical events.

3. Summary statistics can also be visualized using Matplotlib charts. 

### Directory Structure
```AUTOMATED-LOG-MONITOR/
├── logs/                     # Logs and reports
│   ├── monitored/            # Logs being monitored
│   ├── system/               # System-generated logs
├── src/                      # Source code
│   ├── main.py               # Entry point
│   ├── utils/                # Utility modules
│       ├── monitor.py
│       ├── analysis.py
│       ├── alert.py
│       ├── log_manager.py
├── tests/                    # Test files
│   ├── test_monitor.py
│   ├── test_alert.py
├── .gitignore                # Ignore unnecessary files
├── README.md                 # Documentation
├── requirements.txt          # Python dependencies
```
# Key Functionalities
### 1. Real-Time Monitoring
The application tracks changes in all .log files under the monitored directory. Detected modifications trigger:

- Analysis of new log entries.

- Updates to the summary report.

- Email alerts for critical or error-level events.
### 2. Summary Reports 
Generates a comprehensive summary of log levels and stores it in logs/report.txt. Example:
```
Log Analysis Summary:
- INFO: 10 occurrences (50.00%)
- WARNING: 5 occurrences (25.00%)
- ERROR: 3 occurrences (15.00%)
- CRITICAL: 2 occurrences (10.00%)
```
### 3. Email Alerts
Automatically notifies the configured recipient about critical log events. Example alert message: 
```
Subject: Critical Alert from Log Monitoring System

Critical Alert!
The following critical events were detected:
- 2024-12-09 10:00:00 - CRITICAL - System out of memory.
```

# Testing the Application

Running Unit Tests

Tests are provided for core functionalities: 

1. Navigate to the project directory:
```bash
cd Automated-Log-Monitor
```
Run all tests: 
```bash
python -m unittest discover tests
```

### Example Test Cases

- Test Monitoring: Verify that file modifications are detected correctly.

- Test Email Alerts: Simulate critical log events and ensure alerts are sent. 

# Contributing

We welcome contributions to enhance this project!  To contribute:

1. Fork the repository. 

2. Create a new feature branch:
```bash
git checkout -b feature-name
```
3. Commit your changes and push the branch:
```bash
git push origin feature-name
```
4. Open a pull request.

# Future Enhancements

- Containerization: Add Docker support for platform-independent deployment. 

- Dashboard Integration: Create a web-based dashboard for live log monitoring and visualization. 

- Additional Alert Channels: Integrate SMS or Slack notifications. 

# License

This project is licensed under the MIT License. See the LICENSE file for details. 

# Acknowledgments

Special thanks to Python libraries like Watchdog, Matplotlib, and SMTP for enabling this functionality. 

