"""
Author: yashwith alva
Date: 6-11-2023
"""

from flask import Blueprint
from app.mysql_db import get_sqldb

main_blueprint = Blueprint('main', __name__)
from . import routes