from flask import abort, Blueprint, render_template, request, flash, session, g, redirect, url_for
from flask_bcrypt import check_password_hash
import flask

from cryptography.fernet import Fernet


from sqlalchemy.exc import IntegrityError

from application import db, bcrypt
from application.lib import request_input
from application.model import User

data_encryption = Blueprint('data_encryption', __name__)

title = 'Data Encryption'

# key = Fernet.generate_key()
key = b'xkN6Y1kflm0mdRtNTHvJ_FjiBYMVIQM84jMXsYX4huk='
f = Fernet(key)

def encrypt_data(data):
    encrypted_data = f.encrypt(data.encode('utf-8'))
    return encrypted_data.decode('utf-8')

def decrypt_data(data):
    decrypted_data = f.decrypt(data.encode('utf-8'))
    return decrypted_data.decode('utf-8')

@data_encryption.route('/data-encryption/', methods=['GET', 'POST'])
def index():
    data = { "title": title }
    
    
    forEncryption   = ''
    forDecryption   = ''
    encrypted       = ''
    decrypted       = ''
    
    if request.method == 'POST':
        
        requests = {
            "username": request_input("username"), 
            "password": request_input("password"), 
        }
        
        forEncryption = request_input("forEncryption")
        if forEncryption != '':
            encrypted = encrypt_data(forEncryption)
        
        forDecryption = request_input("forDecryption")
        if forDecryption != '':
            decrypted = decrypt_data(forDecryption)
    
    data['forEncryption'] = forEncryption
    data['forDecryption'] = forDecryption
    data['encrypted'] = encrypted
    data['decrypted'] = decrypted
    
    return render_template('data_encryption/index.html', data=data)