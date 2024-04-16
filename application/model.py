from datetime import datetime
from sqlalchemy.types import DateTime, Integer, TIMESTAMP, LargeBinary, String
from sqlalchemy.dialects.mysql import MEDIUMINT, TINYINT
from application import db

class User(db.Model):
    __tablename__ = "users"

    userID = db.Column(Integer, primary_key=True) 
    username = db.Column(String(50), unique=True, nullable=False) 
    password = db.Column(String(100), nullable=False) 
    userTypeID = db.Column(TINYINT, db.ForeignKey('user_types.userTypeID'), nullable=False) 

class UserType(db.Model):
    __tablename__ = "user_types"

    userTypeID = db.Column(TINYINT, primary_key=True) 
    name = db.Column(String(50), nullable=False) 
    