from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from app.auth.forms import LoginForm, RegistrationForm
from operations.core import user_modify, user_lookup
from models.core.user import User

from app.auth import auth
from flask import request

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """ Register a User """
    form = RegistrationForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            user = User()
            form.populate_obj(obj=user)
            user_modify.add(user)
            flash("Successfully Registered")
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ Log in User """
    form = LoginForm()
    if form.validate_on_submit():
        user = user_lookup.by_email(form.email.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)

            return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password.')

    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """ Logout user """
    logout_user()

    return redirect(url_for('home.index'))
