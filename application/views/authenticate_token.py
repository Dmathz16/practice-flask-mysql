from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for

import flask

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
    id      = 0

    print(request_input("username"))

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
            id = user.userID
    else:
        error = 'Please fill all fields.'
    
    return {
        'id': id, 
        'error': error 
    }

@authenticate_token.route('/authenticate-token/api/', methods=['GET'])
def get():
    username = ''
    user = User.query.filter(User.userID==request_args("id")).first()
    if user is not None:
        username = user.username
    return { 'username': username }

@authenticate_token.route('/authenticate-token/api/', methods=['PUT'])
def put():
    return "put"

@authenticate_token.route('/authenticate-token/api/', methods=['DELETE'])
def delete():
    return "delete"