from flask import Blueprint, render_template

crud_page = Blueprint('crud_page', __name__)

title = 'CRUD Page'
view = 'crud_page'

@crud_page.route('/crud-page/')
def index():
    return render_template('crud_page/index.html', title=title, view=view)

@crud_page.route('/crud-page/add/')
def add():
    return render_template('crud_page/add.html', title=title, view=view)

@crud_page.route('/crud-page/view/')
def view():
    return render_template('crud_page/view.html', title=title, view=view)