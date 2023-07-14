import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'chmalyadri1989@gmail.com'
receiver_email = 'chmali007@gmail.com'
subject = 'data enginner role -importnant'
message = 'Hi malydri, i am looking for the data enginner'

# Create a multipart message and set headers
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message to the email
msg.attach(MIMEText(message, 'plain'))

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'yourmailaddress'
password = 'smpt password'
# created this password thorugh google account 2step authentication - apps manage
# Create a secure connection with the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)

# Send the email
server.sendmail(sender_email, receiver_email, msg.as_string())

# Disconnect from the server
server.quit()