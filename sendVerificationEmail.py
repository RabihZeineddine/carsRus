import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # Start TLS for security
        smtp.starttls()
        # Login to the SMTP server
        smtp.login(sender_email, sender_password)
        # Send email
        smtp.send_message(msg)

# Example usage
def main():
    sender_email = "CarsRUsBot@gmail.com"
    sender_password = "trmy fryn dsvk icij"
    receiver_email = "zeineddirabih@gmail.com"
    subject = "Test Email"
    message = "This is a test email sent from Python."

    send_email(sender_email, sender_password, receiver_email, subject, message)
