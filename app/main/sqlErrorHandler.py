'''
Prints error from mysql in readable form
'''
from flask import jsonify

def logSqlError(err):
    print(f"Error code: {err.errno}")        # error number
    print(f"SQLSTATE value: {err.sqlstate}") # SQLSTATE value
    print(f"Error message: {err.msg}")       # error message
    print(f"Error {err}")                    # errno, sqlstate, msg values
    print(f"Error: {str(err)}")              # errno, sqlstate, msg values
    
def db_conn_error():
    return jsonify({
        "status" : "error",
        "message" : "Database is not connected"
    }), 500