import smtplib
import ssl
import getpass

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
email = "my@gmail.com"
password = getpass.getpass("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)  # Secure the connection
        server.login(email, password)
        
        # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
