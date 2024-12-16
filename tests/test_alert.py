from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

def send_test_email():
    email_host = os.getenv("EMAIL_HOST")
    email_port = int(os.getenv("EMAIL_PORT"))
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")
    email_receiver = os.getenv("EMAIL_RECEIVER")

    # Debugging environment variables
    print(f"EMAIL_HOST={email_host}")
    print(f"EMAIL_USER={email_user}")

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_receiver
    msg['Subject'] = "Test Email"
    msg.attach(MIMEText("This is a test email.", 'plain'))

    try:
        with smtplib.SMTP(email_host, email_port) as server:
            server.starttls()
            server.login(email_user, email_pass)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_test_email()
