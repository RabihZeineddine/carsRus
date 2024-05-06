import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from Car_data.py import *
    #Function to send purchase confirmation email
def purchase_confirmation_email(customer_email):
    # Email configuration
    sender_email = 'carsrus@gmail.com'               # Your email address
    sender_password = 'trmy fryn dsvk icij'   # Your email password
    smtp_server = 'smtp.gmail.com'             # Your SMTP server
    smtp_port = 587                           # Port for SMTP server (587 for TLS)
    
    # Construct the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = customer_email
    msg['Subject'] = 'Purchase Confirmation'
    
    #link and import information about the car
    # Create email body
    body = f"Dear Customer,\n\nThank you for your purchase! We Hope you enjoy Your new Ride!\n\n\nBest regards,\nCars R Us"
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, customer_email, msg.as_string())
            print("Purchase confirmation email sent successfully.")
            server.quit()
    except Exception as e:
        print(f"Failed to send purchase confirmation email: {e}")
