#https://www.tomshardware.com/how-to/use-picamera2-take-photos-with-raspberry-pi
#https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

#Added the following to crontab to run at 4:20PM.  Needed to redirect print to file or would not work
#20 16 * * * python3 /home/matc/time/script/PiCam2.py > /home/matc/time/script/file.txt

from picamera2 import Picamera2, Preview #import Picamera2 class and Preview class from picamera2 module
import time #import everything from time module
from os import system #from os module import system class
import datetime #import datetime module

picam2 = Picamera2() #define an instance of the Picamera2() class
#call a method
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)

#Define preview window
#picam2.start_preview(Preview.QTGL)
#Start the camera
picam2.start()
#time.sleep(1)
#Null preview
#After the framing shot of 10 seconds, turn the window off 
#picam2.stop_preview() #call the method
#picam2.start_preview(Preview.NULL)

dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")

system('rm /home/matc/time/*.jpg') #delete all photos in the Pictures folder before timelapse start
fps=30
#10000 should be 35 minutes about
numphotos=1000
secondsinterval=.1
start=time.time()
for i in range(numphotos):
    print('Capturing: /home/matc/time/image{0:06d}.jpg of {1}'.format(i,numphotos))
    picam2.capture_file('/home/matc/time/image{0:06d}.jpg'.format(i))
    time.sleep(secondsinterval)
end=time.time()
diff_time=end-start
print("{0} pictures takens in {1:.2f} seconds".format(numphotos,diff_time))

start=time.time()
print("Please standby as your timelapse video is created.")
system('ffmpeg -r {0} -f image2 -s 1920x1080 -nostats -loglevel 0 -pattern_type glob -i "/home/matc/time/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/matc/time/{1}.mp4'.format(fps, datetimeformat))
end=time.time()
diff_time=end-start
print('Timelapse video is complete. Video saved as /home/matc/time/{}.mp4'.format(datetimeformat))
print("It took {0:.2f} seconds to make the video - /home/matc/time/{1}.mp4".format(diff_time,datetimeformat))

#system("vlc /home/matc/Videos/{0}.mp4".format(datetimeformat))
