from flask import Flask
from app.views import posts_view


def create_app():
    app = Flask(__name__)
    
    
    posts_view.init_app(app)
    
    return app