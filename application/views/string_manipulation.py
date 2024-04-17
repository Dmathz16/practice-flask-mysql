from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for
from flask_bcrypt import check_password_hash
import flask

from sqlalchemy.exc import IntegrityError

from application import db, bcrypt
from application.lib import request_input
from application.model import User

string_manipulation = Blueprint('string_manipulation', __name__)

title = 'String Manipulation'

@string_manipulation.route('/string-manipulation/')
def index():
    data = { "title": title }
    return render_template('string_manipulation/index.html', data=data)