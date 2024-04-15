from flask import abort, Blueprint, render_template, request, flash
import flask

authenticate_session = Blueprint('authenticate_session', __name__)

# starting
@authenticate_session.route('/')
@authenticate_session.route('/authenticate-session/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == '' or password == '' :
            flash('Please fill all fields!', category='error')
        else:
            flash('Account logged in!', category='success')

    return render_template('authenticate_session/index.html', title="Session Authentication")