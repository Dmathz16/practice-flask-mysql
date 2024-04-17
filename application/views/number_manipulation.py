from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for
from flask_bcrypt import check_password_hash
import flask

from sqlalchemy.exc import IntegrityError

from application import db, bcrypt
from application.lib import request_input
from application.model import User

number_manipulation = Blueprint('number_manipulation', __name__)

title = 'Number Manipulation'

@number_manipulation.route('/number-manipulation/')
def index():
    data = { "title": title }
    return render_template('number_manipulation/index.html', data=data)