""""
This file will be used for creating flask application.
This file must register the init file down the hierarchy.

Author: yashwith alva
Date: 6-11-2023
"""

from flask import Flask
from app.config import get_config
from app.mysql_db import init_sqldb
from app.main import main_blueprint

def create_app(config_name):
    app = Flask(__name__)
    
    with app.app_context():
        init_sqldb()
        app.config.from_object(get_config())
        app.register_blueprint(main_blueprint)
    
    return app

