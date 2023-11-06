"""
Author: yashwith alva
Date: 6-11-2023
"""

from flask import Blueprint
main_blueprint = Blueprint('main', __name__)
from . import routes