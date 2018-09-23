import cv2
import numpy as np

path = input("Path: ")
sesitivity = int(input("Sensitivity: "))
divisor = int(input("Grid divisor: "))


videoFile = cv2.VideoCapture(path)

if(videoFile.isOpened() == False):
    print("FAIL")

fps = videoFile.get(cv2.CAP_PROP_FPS)
frameCount = 0 #devide by framerate for seconds
oldSum = 0

ret, frame = videoFile.read()
if ret == True:
    frameCount += 1
    x, y = frame.shape[:2]
    xDivision = x / divisor
    yDivision = y / divisor
    for x in range(divisor):
        for y in range(divisor):
            oldSum += sum(frame[int(x * xDivision), int(y * yDivision)])

while(videoFile.isOpened()):
    ret, frame = videoFile.read()
    if ret == True:
        frameCount += 1
        newSum = 0
        for x in range(divisor):
            for y in range(divisor):
                newSum += sum(frame[int(x * xDivision), int(y * yDivision)])
        if(abs(newSum - oldSum) > sesitivity):
            print("Change at second " + str(int(frameCount / fps)))
        oldSum = newSum
    else:
        quit()
