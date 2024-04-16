from flask import Blueprint, render_template

from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for

from application import db, bcrypt
from application.lib import request_input
from application.model import User, UserType

crud_page = Blueprint('crud_page', __name__)

title = 'CRUD Page'

@crud_page.route('/crud-page/')
def index():
    
    data = { "title": title }
    
    # get user list
    users = User.query.with_entities(
        User.userID, User.username, UserType.name.label('utName')
    ).join(UserType).order_by(User.username.asc()).all()
    data["results"] = users
    
    return render_template('crud_page/index.html', data=data)

@crud_page.route('/crud-page/add/', methods=['GET', 'POST'])
def add():

    data = { "title": title }
    
    # get user type list
    user_types = UserType.query.all()
    data["user_types"] = user_types
    
    if request.method == 'POST':
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
            return redirect(url_for('crud_page.index'))
        else:
            flash('Please fill all fields.', category='error')
    
    return render_template('crud_page/add.html', data=data)

@crud_page.route('/crud-page/view/<int:id>/')
def view(id):
    data = { "title": title }
    
    user = User.query.with_entities(
        User.userID, User.username, UserType.name.label('utName')
    ).join(UserType).filter(User.userID==id).first()
    data['row'] = user
    data['id']  = id
    
    return render_template('crud_page/view.html', data=data)

@crud_page.route('/crud-page/edit/<int:id>/', methods=['GET', 'POST'])
def edit(id):
    data = { "title": title }
    
    # get user type list
    user_types = UserType.query.all()
    data["user_types"] = user_types
    
    user = User.query.with_entities(
        User.userID, User.username, User.userTypeID, UserType.name.label('utName')
    ).join(UserType).filter(User.userID==id).first()
    data['row'] = user
    data['id']  = id
    
    if request.method == 'POST':
        requests = { "userTypeID": request_input("userTypeID") }
        
        if requests.get("userTypeID"):
            user = User.query.filter_by(userID=id).first()
            user.userTypeID = requests.get("userTypeID")
            db.session.commit()
            return redirect(url_for('crud_page.view', id=id))
        else:
            flash('Please select user type.', category='error')
    
    return render_template('crud_page/edit.html', data=data)

@crud_page.route('/crud-page/delete/<int:id>/')
def delete(id):
    user = User.query.filter_by(userID=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('crud_page.index'))