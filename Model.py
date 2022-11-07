import torch
import cv2
import numpy as np
import pandas

class Model:
    def __init__(self, model_type = "custom", weights = "best.pt", repo_name = "ultralytics/yolov5",width=640, height=360) :
        self.model_type = model_type
        self.weight_path = weights
        self.repo_name = repo_name
        self.model = torch.hub.load(repo_name,model_type,path=weights)
        self.width = width
        self.height = height
        
        self.center_x = width/2
        self.center_y = height/2

    def calculate_offset(self, x,y):
        yspecial = self.width - y
        move_x = x - self.center_x
        move_y = yspecial - self.center_y
        if(move_x != 0):
            move_x /= self.center_x
        if(move_y != 0):
            move_y /= self.center_y
        print("sus")
        return move_x, move_y


    def detectFrame(self, frame):
        plates = self.model(frame)

        detections_rows = plates.pandas().xyxy

        for i in range(len(detections_rows)):
            rows = detections_rows[i].to_numpy()
        bboxes = []
        offsets = []
        for i in range(len(rows)):
            x_min, y_min, x_max, y_max, conf, cls, label = rows[i]

            detection = frame[int(y_min):int(y_max), int(x_min):int(x_max)]
            hsv = cv2.cvtColor(detection, cv2.COLOR_BGR2HSV)
            lower_blue = np.array([110,50,50])
            upper_blue = np.array([130,255,255])
        
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            average = cv2.mean(mask)[0]
            if average == 0:
                continue

            x_offset,y_offset = self.calculate_offset(x_min,y_min)
            offsets.append((x_offset,y_offset))
            bbox = [x_min, y_min, x_max, y_max, conf, label]
            bboxes.append(bbox)

            print("Object {} detected at ({},{}) \n\n\n ({},{})".format(i, x_min, y_min, x_max, y_max))
        return bboxes,offsets

    
            