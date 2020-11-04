## This part records footage of the intruder

from picamera import PiCamera       # importing the picamera module
camera = PiCamera()                 # declaring a PiCamera object
camera.vflip = True
count = 0                           # variable to keep track of images

camera.start_recording('/home/pi/Python_Projects/videos/'+str(count)+'.h264')

time.sleep(60)                      # change 60 to however many seconds you want

camera.stop_recording()
