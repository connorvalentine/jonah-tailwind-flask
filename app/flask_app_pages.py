from flask import render_template
from flask import flash

from flask import Blueprint

from app.forms import BetaSignUpForm


# now we add the structure of the flask app, which is just the login page right now
server_bp = Blueprint('main', __name__)

@server_bp.route('/', methods=['GET', 'POST'])
def index():
    form = BetaSignUpForm()
    if form.validate_on_submit():

        flash('you pressed the button u fool')

    return render_template("login_page.html", form=form)
