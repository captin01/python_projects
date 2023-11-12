import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
email = "my@gmail.com"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context) # Secure the connection
    server.login(email, password)
    

    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

#Not the right code wanted. pull (port 465)