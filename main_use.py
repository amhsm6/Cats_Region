from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv
import tensorflow as tf
import numpy as np
import RPi.GPIO as GPIO

camera = PiCamera()
camera.framerate = 1
rawCapture = PiRGBArray(camera)
time.sleep(1)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

model = tf.keras.models.load_model("EasyNet.h5")

i = 0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array

        image = cv.resize(image, (32, 32))
        data = image.astype("float") / 255.0
        data = np.expand_dims(data, axis=0)
        pred = model.predict([[data]])

        if max(pred[0]) == pred[0][0]:
            cat = "barsic"
        elif max(pred[0]) == pred[0][1]:
            cat = "persic"
        else:
            cat = "none"

        if cat == "persic":
	    GPIO.output(18, GPIO.HIGH)
            time.sleep(15)

            GPIO.output(18, GPIO.LOW)

       	rawCapture.truncate(0)

        i += 1
	if cv.waitKey(1) == 27:
            break
