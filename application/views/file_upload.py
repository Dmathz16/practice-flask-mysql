from flask import abort, Blueprint, render_template, send_file, flash, redirect, current_app, request, url_for
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait, landscape, A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

import io, os

from werkzeug.utils import secure_filename

file_upload = Blueprint('file_upload', __name__)

title   = 'Generate PDF'
view    = 'file-upload'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@file_upload.route('/file-upload/', methods=['GET', 'POST'])
def index():
    data = { "title": title, "view": view }
    
    if request.method == 'POST':
        
        # check if the post request has the file part
        if 'fileExt' not in request.files:
            flash('No file part', category='error')
        file = request.files['fileExt']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', category='error')
        else:
            if file and allowed_file(file.filename):
                _, file_extension = os.path.splitext(file.filename) 
                new_filename = 'new_name' + file_extension 
                file.save(os.path.join(current_app.config.get('UPLOAD_FOLDER'), new_filename)) 
            else:
                flash('Invalid file extension', category='error') 
    
    return render_template('file_upload/index.html', data=data)