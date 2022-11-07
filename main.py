import os
import cv2
import torch
import numpy as np
from Model import Model
from Camera import Camera
import logging
logger = logging.getLogger("log")
logger.setLevel(logging.INFO)



def main():
    logger.debug(torch.__version__)
    model = Model()
    camera = Camera()
    while camera.feed.isOpened():
        ret, frame = camera.feed.read()
        if ret == True:
            #Q1
           bounding_box,offsets = model.detectFrame(frame)
           camera.displayPlates(frame,bounding_box)
           #cv2.imshow('Frame',frame)
           key = cv2.waitKey(1)
           if key == 27:
            break
        else: 
            break

    
    
if __name__=='__main__':
    main()