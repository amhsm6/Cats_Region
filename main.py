from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv
#import tensorflow as tf

camera = PiCamera()
camera.framerate = 20 
rawCapture = PiRGBArray(camera)
time.sleep(1)

#model = tf.keras.models.load_model("EasyNet.h5")

i = 0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array

        cv.imwrite(str(i) + ".png", image)
	rawCapture.truncate(0)

        i += 1
	if cv.waitKey(1) == 27:
		break
