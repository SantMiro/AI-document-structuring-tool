from flask import Flask

from app.routes import upload_routes

def create_app():
    app = Flask(__name__)
    
    # Register Blueprints
    app.register_blueprint(upload_routes)
    
    return app
