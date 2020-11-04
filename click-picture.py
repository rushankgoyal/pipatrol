from picamera import PiCamera  # importing the picamera module

camera = PiCamera()            # declaring a PiCamera object
camera.vflip = True            # orientation adjustment       
count = 0                      # variable to keep track of images

# capturing the image and storing it with the count variable as a unique identifier
camera.capture('/home/pi/Python_Projects/'+str(count)+'.jpg')

count+=1                   # increment the count variable by 1
