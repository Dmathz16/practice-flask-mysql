from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for
from flask_bcrypt import check_password_hash
import flask

from sqlalchemy.exc import IntegrityError

from application import db, bcrypt
from application.lib import request_input
from application.model import User

data_encryption = Blueprint('data_encryption', __name__)

title = 'Data Encryption'

@data_encryption.route('/data-encryption/')
def index():
    data = { "title": title }
    return render_template('data_encryption/index.html', data=data)