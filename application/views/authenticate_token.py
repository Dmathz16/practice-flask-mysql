from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for, current_app

import flask
import jwt
import datetime

from application import db, bcrypt
from application.lib import request_input, request_args
from application.model import User

authenticate_token = Blueprint('authenticate_token', __name__)

title   = 'Token Authentication'
view    = 'authenticate-token'

@authenticate_token.route('/authenticate-token/')
def index():
    data = { "title": title, "view": view }
    return render_template('authenticate_token/index.html', data=data)

@authenticate_token.route('/authenticate-token/api/', methods=['POST'])
def post():

    error   = ''
    token   = ''

    requests = {
        "username": request_input("username"), 
        "password": request_input("password"), 
    }
    if requests.get("username") and requests.get("password"):
        
        user = User.query.filter_by(username=requests.get("username")).first()
        
        if user is None:
            error = 'Incorrect username.'
        elif not bcrypt.check_password_hash(user.password, requests.get("password")):
            error = 'Incorrect password.'
        else:
            payload = {
                'id': user.userID,
                # 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10)  # Token expiration time
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Token expiration time
            }
            token = jwt.encode(payload, current_app.config.get('SECRET_KEY'), algorithm='HS256')
    else:
        error = 'Please fill all fields.'
    
    return {
        'id': token, 
        'error': error 
    }

@authenticate_token.route('/authenticate-token/api/', methods=['GET'])
def get():
    
    payload = jwt.decode(request_args("id"), current_app.config.get('SECRET_KEY'), algorithms=["HS256"])
    
    user = User.query.filter(User.userID==payload['id']).first()
    
    username = ''
    if user is not None:
        username = user.username
    return { 'username': username }

@authenticate_token.route('/authenticate-token/api/', methods=['PUT'])
def put():
    return "put"

@authenticate_token.route('/authenticate-token/api/', methods=['DELETE'])
def delete():
    return "delete"