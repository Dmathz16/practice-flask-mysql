from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for
from flask_bcrypt import check_password_hash
import flask

from sqlalchemy.exc import IntegrityError

from application import db, bcrypt
from application.lib import request_input
from application.model import User

authenticate_session = Blueprint('authenticate_session', __name__)

# starting
@authenticate_session.route('/')
def welcome():
    return redirect(url_for('authenticate_session.index'))

@authenticate_session.route('/authenticate-session/', methods=['GET', 'POST'])
def index():
    
    # insert data to have a test account
    try:
        user = User(
            username="admin", 
            password=bcrypt.generate_password_hash('123'), 
        )
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
    
    if request.method == 'POST':
        data = {
            "username": request_input("username"), 
            "password": request_input("password"), 
        }
        print(data)
        if data.get("username") and data.get("password"):
            
            print(data.get("username"))
            user = User.query.filter_by(username=data.get("username")).first()
            print(user)
            
            if user is None:
                flash('Incorrect username', category='error')
            elif not bcrypt.check_password_hash(user.password, data.get("password")):
                flash('Incorrect password.', category='error')
            else:
                session.clear()
                session['user_id'] = user.userID
                return redirect(url_for('authenticate_session.index'))
        else:
            flash('Please fill all fields.', category='error')
            
    return render_template('authenticate_session/index.html', title="Session Authentication")

@authenticate_session.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(userID=user_id).first()
        
@authenticate_session.route('/authenticate-session/logout')
def logout():
    session.clear()
    return redirect(url_for('authenticate_session.index'))