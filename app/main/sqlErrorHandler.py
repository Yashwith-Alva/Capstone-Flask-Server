'''
Prints error from mysql in readable form
'''
from flask import jsonify
from app.logger import logger

def logSqlError(err):
    logger.error(f"Error code: {err.errno}")        # error number
    logger.error(f"SQLSTATE value: {err.sqlstate}") # SQLSTATE value
    logger.error(f"Error message: {err.msg}")       # error message
    logger.error(f"Error {err}")                    # errno, sqlstate, msg values
    logger.error(f"Error: {str(err)}")              # errno, sqlstate, msg values
    
def db_conn_error():
    return jsonify({
        "status" : "error",
        "message" : "Database is not connected"
    }), 500