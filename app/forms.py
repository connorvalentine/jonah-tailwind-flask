from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

''' DOCUMENTATION: 

    WTForms is a way for us to inject html into our Flask pages using python(the login page is the only one for now).\
    WTForms docs: https://wtforms.readthedocs.io/en/2.3.x/fields/
    How to use with flask: https://flask.palletsprojects.com/en/2.0.x/patterns/wtforms/

    -- First you use the form in webapp.py in the app directory.The index() function will generate the html for the login page
    -- This injects HTML into the 
    --You call LoginForm in the html file for the login page

    -- there are 
'''
class BetaSignUpForm(FlaskForm):
    email = StringField('email', validators=[
            DataRequired()])
    submit = SubmitField("Add me to the Beta waitlist")
