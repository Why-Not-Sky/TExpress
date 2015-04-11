# -*- coding: utf-8 -*-
# encoding: utf-8
###coding=utf-8

import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory

from werkzeug import secure_filename

import tExpress

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg'])
STATIC_URL_PATH = '/Users/sky_wu/Dropbox/work/p1-program/myprojects/TExpress' #os.path.abspath(os.path.dirname(__file__))

#app = Flask(__name__)
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='') #STATIC_URL_PATH) #'')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('', path)

@app.route('/data/<path:path>')
def send_data(path):
    return send_from_directory('data', path)

@app.route("/", methods=['GET', 'POST'])
def index():
    # ps -fA | grep python
    errors = []
    results={}
    #results={'3-\xe4\xb9\x98\xe8\xbb\x8a\xe5\x8d\x80\xe9\x96\x93': '\xe5\xb7\xa6\xe7\x87\x9f 00:54 - \xe5\x8f\xb0\xe5\x8c\x97 18:30', '6-\xe7\xa5\xa8\xe8\x99\x9f': '2900510720726', '5-\xe8\xa8\x82\xe4\xbd\x8d\xe4\xbb\xa3\xe8\x99\x9f': '05887138', '2-\xe8\xbb\x8a\xe6\xac\xa1': '222', '1-\xe4\xb9\x98\xe8\xbb\x8a\xe6\x97\xa5\xe6\x9c\x9f': '2015-03-13', '4-\xe7\xa5\xa8\xe6\xac\xbe': 'NT$ 1630'}
    pdf_link=''
    if request.method == 'POST':
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filename)
                pdf_file, results = tExpress.get_ticket_info(filename)
                pdf_link = pdf_file
        except:
            errors.append(
                "Unable to get the ticket information. Please make sure it's valid and try again."
                )

    return render_template('index.html', errors=errors, results=sorted(results.items()), link=pdf_link)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)
