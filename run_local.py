
import flask
from flask import request, jsonify
from flask import send_file
from Surf_counter.model_server import ServeModel
import urllib.request
import os   

#######
##Description for the app
#######

app_model='yolo-tiny.h5'

model_links={'yolo-tiny.h5':'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5',
             'yolo.h5': 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5'}

model_path = "./models/" + app_model 
urllib.request.urlretrieve(model_links[app_model], model_path)

sv=ServeModel(app_model)
count=sv.serveit()
print("COunt")
print(count)