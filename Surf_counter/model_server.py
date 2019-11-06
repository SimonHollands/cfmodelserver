from imageai.Detection import ObjectDetection
from os import listdir
from os.path import isfile, join
import os, shutil
import urllib.request
from s3pushpull import s3pushpull
import io
import pandas as pd


class ServeModel:
    def __init__(self, app_model):
        self.s3 = s3pushpull()
        self.model_path = "./models/" + app_model
        self.detector = ObjectDetection()

        if app_model == "yolo-tiny.h5":
            self.detector.setModelTypeAsTinyYOLOv3()
        else:
            self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath(self.model_path)

    def serveit(self, surfbreak):
        self.output_path = "pred.jpg"
        self.s3key_for_img = (f'''S3:/data/{surfbreak}/frame_last.jpg''')
        self.current_jpg = self.s3.download_aws('temp.jpg', self.s3key_for_img)
        self.detector.loadModel()

        detection_ = self.detector.detectObjectsFromImage(
            input_image='temp.jpg',
            output_image_path=self.output_path,
            minimum_percentage_probability=30,
        )
        self.s3.upload_aws(self.output_path, f'''S3:/data/{surfbreak}/pred.jpg''')

        not_allowed = ["airplane", "bicycle"]
        count = 0
        for x in detection_:
            if x["name"] not in not_allowed:
                count = count + 1

        return str(count)
