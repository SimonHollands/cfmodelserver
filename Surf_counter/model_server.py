from imageai.Detection import ObjectDetection
#import imageai
from os import listdir
from os.path import isfile, join
import os, shutil 
import urllib.request

class ServeModel:
    #model_path = "./models/yolo.h5"
    model_path = "./models/yolo-tiny.h5"
        
    output_path = "./output/breakwaterFull.jpg"
    print("reading yolo model")
    #url = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5'
    url = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5'
    
    urllib.request.urlretrieve(url, model_path)
    print("Done reading model")

    print("Loading models")
    detector = ObjectDetection()
    #detector.setModelTypeAsYOLOv3()
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()
    print("Done Loading Model")

    def __init__(self):
        self.surfimages = ['./data/breakwater/'+ f for f in listdir('./data/breakwater') if f[0] !='.' and isfile(join('./data/breakwater', f))]
    
    def serveit(self):
        self.surfimages = ['./data/breakwater/'+ f for f in listdir('./data/breakwater') if f[0] !='.' and isfile(join('./data/breakwater', f))]
        detection_ = self.detector.detectObjectsFromImage(input_image=self.surfimages[0],output_image_path=self.output_path,
        minimum_percentage_probability=30)

        not_allowed=['airplane','bicycle']
        count=0
        for x in detection_:
            if x['name'] not in not_allowed:
                count=count+1

        return str(count)

