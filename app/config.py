"""
This module is used for setting up different configuration for the app

Author: Yashwith Alva
Date: 6-11-2023
"""

import os

##########################################################
# Base config class used for configuring the app.
# All the config files are similar to POJO or struct(cpp)
##########################################################
class Config:
    SECRET_KEY = "yashwith_secret"
    DEBUG = False
    TESTING = False
    
##########################################################
# Development is configured to run on DEBUG mode
# TESTING is set to false
##########################################################
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Yashwith@2002'
    MYSQL_DB = 'arfoodmenu'
    
##########################################################
# Testing is set to run on debug mode with testing.
##########################################################
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Yashwith@2002'
    MYSQL_DB = 'arfoodmenu'
    PRESERVE_CONTEXT_EXCEPTION = True
    
##########################################################
# Production config has both testing and debug set to off
# Remember to change the port id and host to cloud
##########################################################
class ProductionConfig(Config):
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Yashwith@2002'
    MYSQL_DB = 'arfoodmenu'
    PROPOGATE_EXCEPTIONS = True
    
config_by_name = dict(
    dev = DevelopmentConfig,
    test = TestingConfig,
    prod = ProductionConfig
)

##########################################################
# Get config based on the environment app is running on
##########################################################
def get_config():
    environment = os.getenv('FLASK_ENV', 'development')
    if environment == 'production':
        return ProductionConfig
    elif environment == 'testing':
        return TestingConfig
    else:
        return DevelopmentConfig
