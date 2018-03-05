""" Views associated with user managemetn """

from flask import render_template, request, redirect, url_for
from flask_login import login_required
from flask.ext.login import current_user

from app.user_management import user_mgmt
from app.user_management.forms import EditUserForm, AddAllergyForm
from operations.core import user_modify, user_lookup, user_allergy_modify, allergy_lookup
from models.core.user_allergy import UserAllergy

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


@user_mgmt.route('/user/allergy', methods=['POST', 'GET'])
def add_allergy():
    """ Add an allergy to the User """
    form = AddAllergyForm(request.form)

    # Set the allergies to be shown
    user_allergies = [a.allergy.id for a in allergy_lookup.get_user_allergies(current_user.id)]
    form.allergy_id.choices = [(a.id, a.name) for a in allergy_lookup.get_non_allergies(user_allergies)]

    if request.method == "POST":
        if form.validate_on_submit():
            user_allergy_modify.add(current_user.id, request.form)
            return redirect(url_for('user_mgmt.view'))    

    return render_template('user_management/add_allergy.html', var={'form':form} )
