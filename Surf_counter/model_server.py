from imageai.Detection import ObjectDetection
from os import listdir
from os.path import isfile, join
import os, shutil 
import urllib.request
from s3pushpull import s3pushpull

class ServeModel:
    def __init__(self,app_model):
        self.s3=s3pushpull()
        self.model_path = "./models/"+app_model            
        self.output_path = "pred.jpg"

        print("Loading models")
        self.detector = ObjectDetection()
        
        if app_model=='yolo-tiny.h5':
            self.detector.setModelTypeAsTinyYOLOv3()
        else:
            self.detector.setModelTypeAsYOLOv3()

        self.detector.setModelPath(self.model_path)
        print("Done Loading Model")
    
    def serveit(self):
        self.detector.loadModel()
        #self.surfimages3 = list(self.s3.get_matching_s3_keys(prefix='S3:/data/breakwater'))
        self.surfimages3=['S3:/data/breakwater/frame_last.jpg']
        self.surfimages_local = [x[4:] for x in self.surfimages3]
        print("Local images: ")
        print(self.surfimages_local )

        for s3image in self.surfimages3[:1]:
            self.s3.download_aws(s3image[4:],s3image)

        detection_ = self.detector.detectObjectsFromImage(input_image=self.surfimages_local[0], output_image_path=self.output_path,
        minimum_percentage_probability=30)
        self.s3.upload_aws(self.output_path, 'S3:/current_prediction/pred.jpg')
        
        not_allowed=['airplane','bicycle']
        count=0
        for x in detection_:
            if x['name'] not in not_allowed:
                count=count+1

        return str(count)

