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
app = Flask(__name__, static_url_path=STATIC_URL_PATH) #'')

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
    pdf_link=''
    if request.method == 'POST':
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filename)
                #pnr, tid, tdate, trip = tExpress.get_ticket_info(filename)
                pdf_file, results = tExpress.get_ticket_info(filename)
                pdf_link = pdf_file
                #pnr, tid, tdate, trip = u'05887138', u'2900510720726', u'2015-03-13', u'左營 16:54 - 台北 18:30'
                #results = u'order:%s ticket id:%s date:%s trip:%s' % (pnr, tid, tdate, trip)
                #results = ticket_info
                # return redirect(url_for('index'))
        except:
            errors.append(
                "Unable to get the ticket information. Please make sure it's valid and try again."
                )

    #else: results={} #ticket_info = u''

    return render_template('index.html', errors=errors, results=sorted(results.items()), link=pdf_link)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
