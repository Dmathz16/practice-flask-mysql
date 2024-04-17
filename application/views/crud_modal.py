from flask import Blueprint, render_template

from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for

from application import db, bcrypt
from application.lib import request_input
from application.model import User, UserType

crud_modal = Blueprint('crud_modal', __name__)

title = 'Management Modal (RESTful API)'

@crud_modal.route('/crud-modal/')
def index():
    
    data = { "title": title }
    
    # get user list
    users = User.query.with_entities(
        User.userID, User.username, UserType.name.label('utName')
    ).join(UserType).order_by(User.username.asc()).all()
    data["results"] = users
    
    user_types = UserType.query.all()
    data["user_types"] = user_types
    
    return render_template('crud_modal/index.html', data=data)

@crud_modal.route('/crud-modal/api/', methods=['POST'])
def post():
    error   = ''
    
    requests = {
        "username": request_input("username"), 
        "userTypeID": request_input("userTypeID"), 
    }
    
    if requests.get("username") and requests.get("userTypeID"):
        user = User(
            username    = requests.get("username"), 
            password    = bcrypt.generate_password_hash(requests.get("username")), 
            userTypeID  = requests.get("userTypeID")
        )
        db.session.add(user)
        db.session.commit()
    else:
        error = 'Please fill all fields.'
    
    return { 'error': error }

@crud_modal.route('/crud-modal/api/<int:id>/', methods=['GET'])
def get(id):
    
    user = User.query.with_entities(
        User.userID, User.username, User.userTypeID, UserType.name.label('utName')
    ).join(UserType).filter(User.userID==id).first()
    
    user_types = UserType.query.all()
    user_types_data = [{'userTypeID': user_type.userTypeID, 'name': user_type.name} for user_type in user_types]
    
    return { 
        'id': id, 
        'username': user.username, 
        'userTypeID': user.userTypeID, 
        'user_types': user_types_data 
    }

@crud_modal.route('/crud-modal/api/<int:id>/', methods=['PUT'])
def put(id):
    error   = ''
    
    requests = { 
        "id": request_input("id"), 
        "userTypeID": request_input("userTypeID") 
    }
        
    if requests.get("userTypeID"):
        user = User.query.filter_by(userID=id).first()
        user.userTypeID = requests.get("userTypeID")
        db.session.commit()
    else:
        error = 'Please select user type.'
    
    return { 'error': error }

@crud_modal.route('/crud-modal/api/<int:id>/', methods=['DELETE'])
def delete(id):
    error   = ''
    user = User.query.filter_by(userID=id).first()
    db.session.delete(user)
    db.session.commit()
    return { 'error': error }