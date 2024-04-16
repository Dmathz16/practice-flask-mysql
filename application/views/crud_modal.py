from flask import Blueprint, render_template

crud_modal = Blueprint('crud_modal', __name__)

title = 'CRUD Modal'

@crud_modal.route('/crud-modal/')
def index():
    
    data = { "title": title }
    
    return render_template('crud_modal/index.html', data=data)