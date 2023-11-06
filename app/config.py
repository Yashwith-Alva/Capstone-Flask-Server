import os

class Config:
    SECRET_KEY = "yashwith_secret"
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Yashwith@2002'
    MYSQL_DB = 'arfoodmenu'
    
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Yashwith@2002'
    MYSQL_DB = 'arfoodmenu'
    PRESERVE_CONTEXT_EXCEPTION = True
    
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

def get_config():
    environment = os.getenv('FLASK_ENV', 'development')
    if environment == 'production':
        return ProductionConfig
    elif environment == 'testing':
        return TestingConfig
    else:
        return DevelopmentConfig


# Unlock the key for accessing API access.
#key = Config.SECRET_KEY