import unittest
from unittest.mock import patch, MagicMock, mock_open
from src.monitor import LogFileHandler, monitor_logs
import os

class TestLogFileHandler(unittest.TestCase):
    """
    Tests for the LogFileHandler class in monitor.py
    """

    @patch("builtins.open", new_callable=mock_open, read_data="2024-11-28 10:00:00 - INFO - Application started successfully.\n")
    @patch("utils.monitor.logger")
    def test_on_modified_with_log_file(self, mock_logger, mock_file):
        """
        Test that on_modified processes a .log file correctly.
        """
        # Simulate the event for a modified .log file
        event_mock = MagicMock()
        event_mock.src_path = "logs/monitored/test.log"

        # Create an instance of the handler and call on_modified
        handler = LogFileHandler()
        handler.on_modified(event_mock)

        # Assert that logger.info was called with expected messages
        mock_logger.info.assert_any_call("Modified file: logs/monitored/test.log")
        mock_logger.info.assert_any_call("New lines: ['2024-11-28 10:00:00 - INFO - Application started successfully.\\n']")

    @patch("utils.monitor.logger")
    def test_on_modified_with_non_log_file(self, mock_logger):
        """
        Test that on_modified ignores non-log files.
        """
        # Simulate the event for a modified non-log file
        event_mock = MagicMock()
        event_mock.src_path = "logs/monitored/test.txt"

        # Create an instance of the handler and call on_modified
        handler = LogFileHandler()
        handler.on_modified(event_mock)

        # Assert that no logging was performed
        mock_logger.info.assert_not_called()

class TestMonitorLogs(unittest.TestCase):
    """
    Tests for the monitor_logs function in monitor.py
    """

    @patch("os.makedirs")
    @patch("utils.monitor.Observer")
    @patch("utils.monitor.LogFileHandler")
    def test_monitor_logs_directory_creation(self, mock_handler, mock_observer, mock_makedirs):
        """
        Test that monitor_logs creates the directory if it doesn't exist.
        """
        # Mock the Observer instance and its start method
        observer_mock = MagicMock()
        mock_observer.return_value = observer_mock

        # Call monitor_logs with a non-existent directory
        monitor_logs("logs/nonexistent")

        # Assert that the directory was created
        mock_makedirs.assert_called_with("logs/nonexistent")

        # Assert that Observer and its methods were called
        mock_observer.assert_called_once()
        observer_mock.schedule.assert_called_once_with(mock_handler.return_value, path="logs/nonexistent", recursive=False)
        observer_mock.start.assert_called_once()

    @patch("utils.monitor.time.sleep", side_effect=KeyboardInterrupt)  # Simulate Ctrl+C interruption
    @patch("utils.monitor.Observer")
    def test_monitor_logs_graceful_shutdown(self, mock_observer, mock_sleep):
        """
        Test that monitor_logs handles graceful shutdown on KeyboardInterrupt.
        """
        # Mock the Observer instance
        observer_mock = MagicMock()
        mock_observer.return_value = observer_mock

        # Call monitor_logs and simulate an interruption
        with self.assertRaises(KeyboardInterrupt):
            monitor_logs("logs/monitored")

        # Assert that Observer.stop and Observer.join were called
        observer_mock.stop.assert_called_once()
        observer_mock.join.assert_called_once()

if __name__ == "__main__":
    unittest.main()


