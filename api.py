import flask
from flask import request, jsonify
from flask import send_file
from Surf_counter.model_server import ServeModel
import urllib.request
#######
##Description
#######

app = flask.Flask(__name__)
app.config["DEBUG"] = True
model_path = "./models/yolo-tiny.h5"  
print("reading yolo model")
#url = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5'
url = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5'
print("Read Yolo")
urllib.request.urlretrieve(url, model_path)
sv=ServeModel()

@app.route('/model')
def api_model():
    '''Grab predictions from model server '''
    print("Here  starting Api Model ! ")
    count=sv.serveit()
    count=2
    return str(count)

@app.route('/', methods=['GET'])
def home():
    print("Here  at home ! ")

    '''Home page'''
    return '''<h1>Surfing a Deep Learning Model</h1>
<p>A Yolo Model for detecting surfers.</p>'''

if __name__ == '__main__':
    app.run(threaded=False,use_reloader=False)
