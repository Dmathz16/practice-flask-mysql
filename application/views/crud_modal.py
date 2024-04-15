from flask import Blueprint, render_template

crud_modal = Blueprint('crud_modal', __name__)

@crud_modal.route('/crud-modal/')
def index():
    return render_template('crud_modal/index.html', title="CRUD Modal")