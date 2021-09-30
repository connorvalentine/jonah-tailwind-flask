from flask import render_template
from flask import flash

from flask import Blueprint
import json


from app.forms import BetaSignUpForm

# now we add the structure of the flask app, which is just the login page right now
jonah_app = Blueprint('main', __name__)


@jonah_app.route('/', methods=['GET', 'POST'])
def index():
    form = BetaSignUpForm()
    if form.validate_on_submit():
        flash('You touched the button you fool')

    return render_template("login_page.html", form=form)

@jonah_app.route('/page2', methods=['GET', 'POST'])
def index():
    return render_template("page2.html")
