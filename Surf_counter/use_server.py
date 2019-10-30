from imageai.Detection import ObjectDetection
#import imageai
from os import listdir
from os.path import isfile, join
import os, shutil 
import urllib.request

#url = "https://cfmodelserver.herokuapp.com/model"
#urllib.request.urlopen('http://python.org/') as response


from imageai.Detection import ObjectDetection
model_path = "./models/yolo-tiny.h5"
detector = ObjectDetection()
#detector.setModelTypeAsYOLOv3()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
