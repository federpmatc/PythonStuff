#https://www.raspberrypi.com/documentation/computers/camera_software.html

from picamera2 import Picamera2, Preview
import time
from os import system
import datetime

#libcamera is a software library to support cameras in Linux
#libcamera-apps are simple apps built on top of libcamera

#command = 'libcamera-hello -t 9000' #preview image 3000ms
#command = 'libcamera-jpeg -o ~/test.jpg' #take a pic
command = 'libcamera-jpeg -o ~/test.jpg -t 2000 --width 640 --height 480' #take a pic 2 sec preview, 640x480
#libcamera-still allows files to be saved in a number of different formats.
#command= "libcamera-still -e png -o ~/test.png"
#command='libcamera-still -e bmp -o ~/test2.bmp'
#command="libcamera-still -e rgb -o ~/test2.data"
#command="libcamera-still -e yuv420 -o ~/test.data"

#libcamera-vid is the video capture application.
#By default it uses the Raspberry Pi’s hardware H.264 encoder.
#It will display a preview window and write the encoded bitstream to the specified output.
#For example, to write a 10 second video to file use
#command="libcamera-vid -t 10000 -o ~/video.h264 --vflip --width 640 --height 480"
#command='libcamera-vid -h'
system(command)
