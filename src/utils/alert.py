import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from utils.log_manager import get_logger
import os

logger = get_logger()
def send_email(subject, body, recipients, smtp_server, smtp_port, sender_email, sender_password, attachment_path=None):
    """
    Sends an email with optional attachment.
    
    Args:
        subject (str): Subject of the email.
        body (str): Body content of the email.
        recipients (list): List of email addresses to send the email to.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        sender_email (str): Email address of the sender.
        sender_password (str): Password for the sender's email account.
        attachment_path (str): Optional path to a file to attach.
    
    Returns:
        None
    """
    load_dotenv()
    enable_email_alerts = os.getenv("ENABLE_EMAIL_ALERTS", "true").lower() == "true"
    if not enable_email_alerts:
        print("Email alerts are disabled.")
        return
    
    try:
        # Fetch email configuration from environment variables
        email_host = os.getenv("EMAIL_HOST")
        email_port = int(os.getenv("EMAIL_PORT"))
        email_user = os.getenv("EMAIL_USER")
        email_pass = os.getenv("EMAIL_PASS")
        email_receiver = os.getenv("EMAIL_RECEIVER")
        
        # Constructs the email
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        with smtplib.SMTP(email_host, email_port,timeout=60) as server:
            server.starttls()  # Encrypt the connection
            server.login(email_user, email_pass)
            server.send_message(msg)
            logger.info(f"Alert sent to {email_receiver}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")

        # Attach the body content
        msg.attach(MIMEText(body, 'plain'))

        # Attach a file if provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
                msg.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipients, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")


def format_critical_alert(log_lines):
    """
    Formats a critical alert message from log lines.
    
    Args:
        log_lines (list): List of log lines that triggered the alert.
    
    Returns:
        str: Formatted alert message.
    """
    alert_message = "Critical Alert!\n\nThe following critical events were detected:\n"
    for line in log_lines:
        alert_message += f"- {line.strip()}\n"
    return alert_message
