# -*- coding: utf-8 -*-
# encoding: utf-8
###coding=utf-8

import os
from flask import Flask, request, redirect, url_for, render_template

from werkzeug import secure_filename

import tExpress

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    # ps -fA | grep python
    errors = []
    results={}
    if request.method == 'POST':
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filename)
                #pnr, tid, tdate, trip = tExpress.get_ticket_info(filename)
                results = tExpress.get_ticket_info(filename)
                #pnr, tid, tdate, trip = u'05887138', u'2900510720726', u'2015-03-13', u'左營 16:54 - 台北 18:30'
                #results = u'order:%s ticket id:%s date:%s trip:%s' % (pnr, tid, tdate, trip)
                #results = ticket_info
                # return redirect(url_for('index'))
        except:
            errors.append(
                "Unable to get the ticket information. Please make sure it's valid and try again."
                )

    #else: results={} #ticket_info = u''

    return render_template('index.html', errors=errors, results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
