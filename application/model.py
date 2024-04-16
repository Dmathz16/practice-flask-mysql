from datetime import datetime
from sqlalchemy.types import DateTime, Integer, TIMESTAMP, LargeBinary, String
from application import db

class User(db.Model):
    __tablename__ = "users"

    userID = db.Column(Integer, primary_key=True) 
    username = db.Column(String(50), unique=True, nullable=False) 
    password = db.Column(String(100), nullable=False) 