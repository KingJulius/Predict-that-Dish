import util
import os
from flask import Flask, request, jsonify, session, render_template, url_for
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/upload', methods=['POST'])
def upload():
    target=os.path.join(UPLOAD_FOLDER,'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    response = jsonify({
        'pred_label': util.get_predicted_item(destination)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

 
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/get_labels', methods=['GET'])
def get_labels():
    response = jsonify({
        'lables': util.get_labels()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @app.route('/predict_label', methods=['GET'])
# def predict_label():
#     response = jsonify({
#         'pred_label': util.get_predicted_item("./static/uploads/test.jpg")
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    print("Starting Python Flask Server For Dish Prediction...")
    util.load_saved_artifacts()
    app.run()
