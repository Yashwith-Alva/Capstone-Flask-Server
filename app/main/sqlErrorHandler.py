'''
Prints error from mysql in readable form
'''
from flask import jsonify
from app.utils.logger import logger

def logSqlError(err):
    logger.warning(f"Error code: {err.errno}")        # error number
    logger.warning(f"SQLSTATE value: {err.sqlstate}") # SQLSTATE value
    logger.warning(f"Error message: {err.msg}")       # error message
