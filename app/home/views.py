""" Views associated with home """

from flask import render_template
from flask_login import login_required

from app.home import home
from operations.core import user_lookup

@home.route('/')
def index():
    """ Home Page """

    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """ Dashboard after logging in """

    users = user_lookup.get_all()
    return render_template('home/dashboard.html', var={
        'users' : users
    })
