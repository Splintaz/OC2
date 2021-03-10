from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "wordpac" # Change the secret key for security reasons

    from .views import views
    app.register_blueprint(views, url_prefix="/")
    
    return app
