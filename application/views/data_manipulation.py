from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for
from flask_bcrypt import check_password_hash
import flask

from sqlalchemy.exc import IntegrityError

from application import db, bcrypt
from application.lib import request_input
from application.model import User

data_manipulation = Blueprint('data_manipulation', __name__)

title = 'Data Manipulation'

@data_manipulation.route('/data-manipulation/')
def index():
    data = { "title": title }
    return render_template('data_manipulation/index.html', data=data)