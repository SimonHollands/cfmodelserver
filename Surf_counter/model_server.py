from imageai.Detection import ObjectDetection
#import imageai
from os import listdir
from os.path import isfile, join
import os, shutil 
import urllib.request
from s3pushpull import s3pushpull

class ServeModel:
    def __init__(self):
        self.s3=s3pushpull()
        #model_path = "./models/yolo.h5"
        self.model_path = "./models/yolo-tiny.h5"
            
        self.output_path = "./output/breakwaterFull.jpg"
        print("reading yolo model")
        #url = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5'
        self.url = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5'
        urllib.request.urlretrieve(self.url, self.model_path)
        print("Loading models")
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath(self.model_path)
        self.detector.loadModel()
        print("Done Loading Model")
    
    def serveit(self):
        self.surfimages3 = list(self.s3.get_matching_s3_keys(prefix='S3:/data/'))
        self.surfimages_local = [x[4:] for x in self.surfimages3]
        print("Local images: ")
        print(self.surfimages_local )

        for s3image in self.surfimages3[:1]:
            print("Trying to download:")
            print (s3image)
            print (s3image[4:])

            self.s3.download_aws(s3image[4:],s3image)

        detection_ = self.detector.detectObjectsFromImage(input_image=self.surfimages_local[0],output_image_path=self.output_path,
        minimum_percentage_probability=30)

        # s3=s3pushpull()
        # d=list(s3.get_matching_s3_keys(prefix='S3:/data/breakwater'))

        not_allowed=['airplane','bicycle']
        count=0
        for x in detection_:
            if x['name'] not in not_allowed:
                count=count+1

        return str(count)

