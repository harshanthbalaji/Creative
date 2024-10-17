import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Set up the server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, sender_password)  # Log in to your email account
            server.send_message(msg)  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function call section
if __name__ == "__main__":
    sender_email = input("Enter your email: ")  # Take sender's email as input
    sender_password = input("Enter your app password: ")  # Take sender's password as input
    recipient_email = input("Enter recipient's email: ")  # Take recipient's email as input
    subject = input("Enter email subject: ")  # Take email subject as input
    message = input("Enter email message: ")  # Take email message as input

    # Call the send_email function
    send_email(sender_email, sender_password, recipient_email, subject, message)

