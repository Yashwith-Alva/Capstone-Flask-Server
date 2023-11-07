import os
from app import create_app
from app.mysql_db import get_sqldb
from flask import g

os.environ['FLASK_APP'] = 'run.py'
os.environ['FLASK_ENV'] = 'development'

app = create_app()

if __name__ == '__main__':
    app.run()