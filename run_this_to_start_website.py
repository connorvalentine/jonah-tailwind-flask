# Python packages we need for this script:
from flask import Flask

# Import from subfolders:
from app.flask_app_pages import jonah_app

 # this is used to intialize flask.
class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Some-secret-here...'

# This section is the creation of the flask application and server where it lives
server = Flask(__name__, template_folder='app/templates', static_url_path="/app/static", static_folder='app/static')
server.config.from_object(BaseConfig)

# add the flask html files in templates folder to the site (called blueprints)
server.register_blueprint(jonah_app)


# If this python script is the main one being run, start the server.
if __name__ == "__main__":
    server.run(debug=True)
