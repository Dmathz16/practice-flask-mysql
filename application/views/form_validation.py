from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for
from flask_bcrypt import check_password_hash
import flask

from sqlalchemy.exc import IntegrityError

from application import db, bcrypt
from application.lib import request_input
from application.model import User

form_validation = Blueprint('form_validation', __name__)

title = 'Form Validation'

@form_validation.route('/form-validation/')
def index():
    data = { "title": title }
    return render_template('form_validation/index.html', data=data)