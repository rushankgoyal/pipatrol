import email, smtplib, ssl, webbrowser, os, sys
port = 465
smtp_server = "smtp.gmail.com"

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Alert"
body = "Motion has been detected at your home. Please see photo attached"
sender_email = <ENTER_SENDER_ADDRESS>
receiver_email = <ENTER_RECEIVER_ADDRESS>
password = <ENTER_PASSWORD_IN_PLAIN_TEXT>

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email

from picamera import PiCamera
import RPi.GPIO as GPIO
import time

time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.IN)

camera = PiCamera()
camera.framerate = 10
camera.vflip = True

seconds = 60
count=1

time.sleep(1)

while True:
    i=GPIO.input(4)
    if i==0:
        time.sleep(0.1)
    elif i==1:
        time.sleep(0.1)      
        i = GPIO.input(4)
        if i==1:        
          url = "https://maker.ifttt.com/trigger/motion/with/key/eupEZJIDrrkF4gVP0JkpVKHX3UpL0qq0C_iyJPryS1F"
          chrome_path = '/usr/lib/chromium-browser/chromium-browser'
          webbrowser.get(chrome_path).open(url)

          time.sleep(0.01)       

          camera.capture('/home/pi/Python_Projects/'+str(count)+'.jpg')
          message.attach(MIMEText(body, "plain"))
          filename = str(count)+".jpg"    

          with open(filename, "rb") as attachment:
              part = MIMEBase("application", "octet-stream")
              part.set_payload(attachment.read())

          encoders.encode_base64(part)

          part.add_header("Content-Disposition","attachment; filename= intruder_photo.jpg")

          message.attach(part)
          text = message.as_string()
          context = ssl.create_default_context()

          with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
              server.login(sender_email, password)
              server.sendmail(sender_email, receiver_email, text)

          time.sleep(0.01)
          camera.start_recording('/home/pi/Python_Projects/videos/'+str(count)+'.h264')
          time.sleep(seconds)
          camera.stop_recording()
          count+=1
          time.sleep(1)
