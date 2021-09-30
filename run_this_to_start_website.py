# This first line tells python to import jonah_app from our python script called 
# flak_app_pages.py which is in the app folder 
from app.flask_app_pages import jonah_app

# If this python script is the main one being run, it will start the server.
if __name__ == "__main__":
    jonah_app.run(use_reloader=True, debug=True)
