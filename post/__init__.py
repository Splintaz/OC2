# OC2 (Office Command and Control) allows you to send remote commands and receive encrypted data with a Word/Excel/PowerPoint Macro.
# Created by https://github.com/Splintaz/
from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "officepac" # Change the secret key for security reasons

    from .views import views
    app.register_blueprint(views, url_prefix="/")
    
    return app
