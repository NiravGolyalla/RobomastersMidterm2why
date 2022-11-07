import cv2

class Camera:
    def __init__(self,camera_inp=-1,depth_bit = False, path = "vid.mp4"):
        if depth_bit:
            self.feed = cv2.VideoCapture(camera_inp)
            self.depth = True
        else:
            self.feed = cv2.VideoCapture(path)
            self.depth = False



    def release(self):
        self.feed.release()

    def get_video_stream(self):
        return self.feed
    
    def displayPlates(self,frame,bounding_boxes):
        for bbox in bounding_boxes:
            cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2) 
            if(self.depth):
                depth = ""
            else:
                depth = ""
            
            label_conf = "blue" + depth
            cv2.putText(frame, label_conf, (int(bbox[0]), int(bbox[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
 
        cv2.imshow("Frame",frame)