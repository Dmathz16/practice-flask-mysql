from datetime import datetime
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMINT, TINYINT, TEXT, VARCHAR, DATETIME
from application import db

class User(db.Model):
    __tablename__ = "users"

    userID = db.Column(INTEGER, primary_key=True) 
    username = db.Column(VARCHAR(50), unique=True, nullable=False) 
    password = db.Column(VARCHAR(100), nullable=False) 
    userTypeID = db.Column(TINYINT, db.ForeignKey('user_types.userTypeID'), nullable=False) 

class UserType(db.Model):
    __tablename__ = "user_types"

    userTypeID = db.Column(TINYINT, primary_key=True) 
    name = db.Column(VARCHAR(50), nullable=False) 

class Configuration(db.Model):
    __tablename__ = "configurations"

    name = db.Column(INTEGER, primary_key=True) 
    description = db.Column(DATETIME, unique=True, nullable=False) 
    