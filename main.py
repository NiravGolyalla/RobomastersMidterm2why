import os
import cv2
import numpy as np
from Model import Model
from Camera import Camera

def main():
    model = Model()
    camera = Camera()
    while camera.feed.isOpened():
        ret, frame = camera.feed.read()
        if ret == True:
            #Q1
           bounding_box = model.detectFrame(frame)
           camera.displayPlates(frame,bounding_box)
           #cv2.imshow('Frame',frame)
           key = cv2.waitKey(1)
           if key == 27:
            break
        else: 
            break

    
    
if __name__=='__main__':
    main()