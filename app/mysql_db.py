'''
This module is used for interacting with database

Author: yashwith alva
Date: 6-11-2023
'''

# Named the file as mysql_db because may end up using the mongo database.

from flask import current_app
import mysql.connector
from mysql.connector import errorcode

###############################################
# get SQL database
###############################################
def get_sqldb():
    try:
        return mysql.connector.connect(
            host = current_app.config['MYSQL_HOST'],
            port = current_app.config['MYSQL_PORT'],
            user = current_app.config['MYSQL_USER'],
            password = current_app.config['MYSQL_PASSWORD'],
            database = current_app.config['MYSQL_DB']
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something went wrong with the username and password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)
            
################################################
# Close DB connection
################################################

        
################################################
# Incase if there is an initialization
################################################
