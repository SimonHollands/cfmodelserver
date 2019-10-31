import flask
from flask import request, jsonify
from flask import send_file
from Surf_counter.model_server import ServeModel
import urllib.request
import os   
#######
##Description for the app
#######
app_model='yolo.h5'

model_links={'yolo-tiny.h5':'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5',
             'yolo.h5': 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5'}

model_path = "./models/" + app_model 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

print("Read Model")
urllib.request.urlretrieve(model_links[app_model], model_path)
sv=ServeModel()

@app.route('/model')
def api_model():
    '''Grab predictions from model server '''
    print("Here  starting Api Model ! ")
    count=sv.serveit()
    return str(count)

@app.route('/', methods=['GET'])
def home():
    print("Here  at home ! ")

    '''Home page'''
    return '''<h1>Surfing a Deep Learning Model</h1>
<p>A Yolo Model for detecting surfers.</p>'''

if __name__ == '__main__':
    app.run(threaded=False,use_reloader=False)
