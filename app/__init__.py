""""
This file will be used for creating flask application.
This file must register the init file down the hierarchy.

Author: yashwith alva
Date: 6-11-2023
"""

from flask import Flask
from app.config import get_config
from app.main import main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    
    with app.app_context():
        app.register_blueprint(main_blueprint)
    
    return app

