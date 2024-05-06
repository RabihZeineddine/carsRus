import smtplib
from email.mime.text import MIMEText
# Body of E-mail
def send_confirmation_email(recipient):
    msg = MIMEText("Dear Customer,\n\nThank you for your purchase. We hope you enjoy your new ride\n\n\nBest wishes,\nThe Cars-R-Us Team")
    # Subject of E-mail
    msg['Subject'] = "This is Subject of Email........."
    # Sender E-mail Id
    sender = 'CarsRUsBot@zohomail.com'
    msg['From'] = sender
    # Receiver E-mail Id
    msg['To'] = recipient
    # SMTP Server
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    # SMTP Server Login Credentials
    server.login(sender, 'pg7g p0e6 wzm7')
    # Gives Send Mail Request to SMTP Server
    server.sendmail(sender, recipient, msg.as_string())
    # Quit or Logout from SMTP Server
    server.quit()
    print("Email sent to " + recipient)

def main():
    send_confirmation_email('skoolrokz1232@gmail.com')

if __name__ == "__main__":
    main()
