# these top lines are some of the python packages we need for this script

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

''' DOCUMENTATION: 

    We will use this form in our landing page to collect emails.
    They are not saved anywhere right now.

    WTForms is a way for us to inject html into our Flask pages using python(the login page is the only one for now).\
    WTForms docs: https://wtforms.readthedocs.io/en/2.3.x/fields/
    How to use with flask: https://flask.palletsprojects.com/en/2.0.x/patterns/wtforms/
'''
class BetaSignUpForm(FlaskForm):
    email = StringField('email', validators=[
            DataRequired()])
    submit = SubmitField("Add me to the Beta waitlist")
