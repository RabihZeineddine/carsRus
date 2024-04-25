import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send purchase confirmation email
def send_confirmation_email(customer_email, purchase_details):
    # Email configuration
    sender_email = 'Car-R-Us'               # Your email address
    sender_password = 'ILoveProfessorKim'   # Your email password
    smtp_server = 'smtp.gmail.com'          # Your SMTP server
    smtp_port = 587                         # Port for SMTP server (587 for TLS)

    # Construct the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = customer_email
    msg['Subject'] = 'Purchase Confirmation'

    # Create email body
    body = f"Dear Customer,\n\nThank you for your purchase!\n\nPurchase Details:\n{purchase_details}\n\nBest regards,\nYour Company"
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, customer_email, msg.as_string())
            print("Purchase confirmation email sent successfully.")
    except Exception as e:
        print(f"Failed to send purchase confirmation email: {e}")

# Example usage
def main():
    # Simulate a purchase and collect the customer's email and purchase details
    customer_email = input("Enter customer's email address: ")
    purchase_details = input("Enter purchase details: ")

    # Send purchase confirmation email
    send_confirmation_email(customer_email, purchase_details)

if __name__ == "__main__":
    main()
