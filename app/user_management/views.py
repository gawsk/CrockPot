""" Views associated with user managemetn """

from flask import render_template, request, redirect, url_for
from flask_login import login_required
from flask.ext.login import current_user

from app.user_management import user_mgmt
from app.user_management.forms import EditUserForm
from operations.core import user_modify, user_lookup


@user_mgmt.route('/user/')
def view():
    """ View your User profile """

    user_obj = user_lookup.by_id(current_user.id)
    return render_template('user_management/view.html', var={'user_obj':user_obj})


@user_mgmt.route('/user/edit', methods=['POST', 'GET'])
def edit():
    """ Edit your User profile """
    form = EditUserForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            user_modify.save(current_user.id, request.form)
            return redirect(url_for('user_mgmt.view'))
    else:
        form = EditUserForm(obj=current_user)

    return render_template('user_management/edit.html', var={'form':form} )
