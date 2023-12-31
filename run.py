'''
Main application entry point
It calls the blueprint in app directory.

Author: yashwith alva
Date: 7-11-2023
'''

import os
from app import create_app
from flask import g

os.environ['FLASK_APP'] = 'run.py'
os.environ['FLASK_ENV'] = 'testing'

app = create_app()

@app.route("/")
def index():
    return "Homepage"

if __name__ == '__main__':
    app.run(host='0.0.0.0')