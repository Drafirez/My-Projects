
class DevelopmentConfig():
    SECRET_KEY = 'my_secret_key'
    
    MYSQL_PORT= 3307
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '12345678'
    MYSQL_DB = 'flask_login'

config = {
    'development': DevelopmentConfig
}