# Named the file as mysql_db because may end up using the mongo database.

from flask import current_app
from flask import g
import mysql.connector
from mysql.connector import errorcode

###############################################
# get SQL database
###############################################
def get_sqldb():
    if 'db' not in g:
        # Establish a database connection
        try:
            g.db = mysql.connector.connect(
                host = current_app.config['MYSQL_HOST'],
                port = current_app.config['MYSQL_PORT'],
                user = current_app.config['MYSQL_USER'],
                password = current_app.config['MYSQL_PASSWORD'],
                database = current_app.config['MYSQL_DB']
            )
            return g.db
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something went wrong with the username and password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            else:
                print(err)
        else:
            print("NOT SUCCESSFULL ATTEMPT")
    # return g.db irrespective of the attempt.
    return g.db
    
################################################
# Close DB connection
################################################
def close_sqldb(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        
################################################
# Incase if there is an initialization
################################################
def init_sqldb():
    db = get_sqldb()
    cursor = db.cursor()
    
    db.commit()
    cursor.close()
