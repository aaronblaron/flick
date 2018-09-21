import cv2
import numpy as np

path = raw_input("Path: ")
frameRate = float(raw_input("Frame rate: "))

videoFile = cv2.VideoCapture(path)

if(videoFile.isOpened() == False):
    print "FAIL"

frameCount = 0 #devide by framerate for seconds
oldSum = 0

while(videoFile.isOpened()):
    ret, frame = videoFile.read()
    if ret == True:
        frameCount += 1
        newSum = 0
        height, width = frame.shape[:2]
        for x in range(width / 400):
            for y in range(height / 400):
                newSum += sum(frame[y*400,x*400])
        if(abs(newSum - oldSum) > 10):
            print("Change at second " + str(frameCount / frameRate))
        oldSum = 0
