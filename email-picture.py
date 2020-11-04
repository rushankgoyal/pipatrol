## This part sends an email of the picture taken to the owner.

# import libraries
import email, smtplib, ssl

# port 465 connects to Gmail's SMTP server, smtp.gmail.com
port = 465
smtp_serv = "smtp.gmail.com"

# more import statements for functions we'll need
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# more variables
subject = "Alert"
body = "Motion has been detected at your home. See photo attached"
sender_email = <ENTER_SENDER_ADDRESS>
receiver_email = <ENTER_RECEIVER_ADDRESS>
password = <ENTER_PASSWORD_FOR_SENDER_ADDRESS>

# create message with details
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email

# define body
message.attach(MIMEText(body, "plain"))

# attach image
filename = str(count)+".jpg"    

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    
encoders.encode_base64(part)

part.add_header("Content-Disposition","attachment; filename= intruder_photo.jpg")
message.attach(part)

# send email
text = message.as_string()
cxt = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_serv, port, cxt=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    time.sleep(0.1)
