from flask import render_template
from flask_login import login_required

from app.home import home

@home.route('/')
def index():
    """ Home Page """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """ Dashboard after logging in """
    return render_template('home/dashboard.html', title="Dashboard")
