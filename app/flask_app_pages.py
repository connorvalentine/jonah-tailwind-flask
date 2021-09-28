from flask import render_template
from flask import flash

from flask import Blueprint
import json


from app.forms import BetaSignUpForm

# now we add the structure of the flask app, which is just the login page right now
page1_bp = Blueprint('main', __name__)


@page1_bp.route('/', methods=['GET', 'POST'])
def index():
    form = BetaSignUpForm()
    if form.validate_on_submit():
        flash('You touched the button you fool')

    return render_template("login_page.html", form=form)
