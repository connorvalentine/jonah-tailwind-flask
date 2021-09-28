from flask import Flask
from flask import render_template
from flask import flash
from app.flask_app_pages import server_bp
'''Imports from our repo '''


class BaseConfig:
    # this is used to intialize flask.
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Some-secret-here...'

# This section is the creation of the flask app which will route the users to the dash apps
server = Flask(__name__, template_folder='app/templates', static_url_path="/app/static", static_folder='app/static')
server.config.from_object(BaseConfig)

# add the flask pages 
server.register_blueprint(server_bp)


if __name__ == "__main__":
    server.run(debug=True)
