from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from . import db

db = SQLAlchemy()
bcrypt = Bcrypt()

DB_SERVER   = "localhost"
DB_PORT     = "3306"
DB_USERNAME = "root"
DB_PASSWORD = ""
DB_NAME     = "practice_flask"
    
def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'This is secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}'
    
    db.init_app(app)
    bcrypt.init_app(app)
    
    from application.views.authenticate_session import authenticate_session
    from application.views.authenticate_token import authenticate_token
    from application.views.crud_page import crud_page
    from application.views.crud_modal import crud_modal
    
    app.register_blueprint(authenticate_session)
    app.register_blueprint(authenticate_token)
    app.register_blueprint(crud_page)
    app.register_blueprint(crud_modal)
    
    return app
