#camera.py# import the necessary packages
import cv2# defining face detector
import torch
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6
class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()
    def get_frame(self,model):
       #extracting frames
        ret, frame = self.video.read()
        #print("frame",frame)
        #frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor, interpolation=cv2.INTER_AREA)
        #print("frame1",frame)
        model=model
        img = torch.from_numpy(frame.astype('float32')).permute(2,0,1)
        img = img / 255.
        print(img.shape)

        predictions = model(img[None,...])

        CONF_THRESH = 0.9
        boxes = predictions[0]['boxes'][predictions[0]['scores'] > CONF_THRESH]
        boxes_dict = {}
        boxes_dict['boxes'] = boxes

        img_with_boxes = plot_preds(frame, boxes_dict)
        print(img_with_boxes.shape)
                  
	

        ret, jpeg = cv2.imencode('.jpg', img_with_boxes)
        return jpeg.tobytes()

def plot_preds(numpy_img, preds):
  boxes = preds['boxes'].detach().numpy()
  for box in boxes:
    numpy_img = cv2.rectangle(
        cv2.UMat(numpy_img), 
        (box[0],box[1]),
        (box[2],box[3]), 
        255,3)
  return numpy_img.get()
