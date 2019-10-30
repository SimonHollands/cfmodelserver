import flask
from flask import request, jsonify
from flask import send_file
from Surf_counter.model_server import ServeModel

app = flask.Flask(__name__)
app.config["DEBUG"] = True
sv=ServeModel()

@app.route('/model')
def api_model():
    '''Grab predictions from model server'''
    count=sv.serveit()
    return count
    
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Surfing a Deep Learning Model</h1>
<p>A Yolo Model for detecting surfers.</p>'''


if __name__ == '__main__':
    app.run(threaded=False,use_reloader=False)