from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for
from flask_bcrypt import check_password_hash

import flask
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from application import db, bcrypt
from application.lib import request_input
from application.model import Configuration

date_manipulation = Blueprint('date_manipulation', __name__)

title = 'Date Manipulation'

@date_manipulation.route('/date-manipulation/')
def index():
    data = { "title": title }
    
    user = Configuration.query.filter_by(name="Test Date").first()
    
    testDate = user.description
    testDateString = testDate.strftime("%Y-%m-%d %H:%M:%S")
    
    data['testDate'] = testDate
    
    # MM d, YYYY hh:ii AA
    data['test1A'] = testDate.strftime("%B %#d, %Y %I:%M %p")
    data['test1B'] = datetime.strptime(testDateString, "%Y-%m-%d %H:%M:%S").strftime("%B %#d, %Y %I:%M %p")
    
    # M dd/YY HH:ii aa
    data['test2A'] = testDate.strftime("%b %d/%y %I:%M %p").lower()
    data['test2B'] = datetime.strptime(testDateString, "%Y-%m-%d %H:%M:%S").strftime("%b %d/%y %I:%M %p").lower()
    
    # MM/dd/YYYY HH:ii:ss
    data['test3A'] = testDate.strftime("%m/%d/%Y %H:%M:%S")
    data['test4B'] = datetime.strptime(testDateString, "%Y-%m-%d %H:%M:%S").strftime("%m/%d/%Y %H:%M:%S")
    
    return render_template('date_manipulation/index.html', data=data)