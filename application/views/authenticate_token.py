from flask import Blueprint, render_template

authenticate_token = Blueprint('authenticate_token', __name__)

@authenticate_token.route('/authenticate-token/')
def index():
    return render_template('authenticate_token/index.html', title="Token Authentication")