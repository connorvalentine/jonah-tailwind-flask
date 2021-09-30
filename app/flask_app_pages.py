from flask import render_template
from flask import flash
from flask import Flask
from app.forms import BetaSignUpForm

# first we make a configuration class, dont worry about this for now, its just a way to get some default settings into 
# our app so we can use secure forms later.

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Some-secret-here...'

# now we create the structure of our website, one page at a time!
jonah_app = Flask(__name__)
jonah_app.config.from_object(BaseConfig)

# Now we add the homepage, with the URL = /. 
@jonah_app.route('/', methods=['GET', 'POST'])
def index():
    # here we have a form for the "email collection"
    form = BetaSignUpForm()

    # if validate_on_submit function returns True instead of False, it will flash this message on the screen
    if form.validate_on_submit():
        flash('You touched the button you fool')

    # this last line tells python (for the '/' URL, use the login_page.html file)
    return render_template("login_page.html", form=form)

@jonah_app.route('/page2', methods=['GET', 'POST'])
def page2():
     # PAge 2 is simpler. There is no form for email collection. Its only HTML and CSS styling. no forms.
    return render_template("page2.html")
