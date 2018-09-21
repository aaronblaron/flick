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
    frameCount += 1
    ret, frame = videoFile.read()
    if ret == True:
        newSum = 0
        height, width = frame.shape[:2]
        for x in range(width):
            for y in range(height):
                newSum += frame[x, y][0] + frame[x, y][1] + frame[x, y][2]
        if(abs(newSum - oldSum) > 100):
            print(frameCount / 40)
        oldSum = 0
