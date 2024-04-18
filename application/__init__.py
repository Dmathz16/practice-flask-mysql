import os, locale

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

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
def create_app():
    
    app = Flask(__name__)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'My Secret Key'
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    db.init_app(app)
    bcrypt.init_app(app)
    
    from application.views.authenticate_session import authenticate_session
    from application.views.authenticate_token import authenticate_token
    from application.views.form_validation import form_validation
    from application.views.crud_page import crud_page
    from application.views.crud_modal import crud_modal
    from application.views.date_manipulation import date_manipulation
    from application.views.string_manipulation import string_manipulation
    from application.views.number_manipulation import number_manipulation
    from application.views.data_encryption import data_encryption
    from application.views.file_upload import file_upload
    from application.views.generate_pdf import generate_pdf
    from application.views.generate_excel import generate_excel
    
    app.register_blueprint(authenticate_session)
    app.register_blueprint(authenticate_token)
    app.register_blueprint(form_validation)
    app.register_blueprint(crud_page)
    app.register_blueprint(crud_modal)
    app.register_blueprint(date_manipulation)
    app.register_blueprint(string_manipulation)
    app.register_blueprint(number_manipulation)
    app.register_blueprint(data_encryption)
    app.register_blueprint(file_upload)
    app.register_blueprint(generate_pdf)
    app.register_blueprint(generate_excel)
    
    return app
