
class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_PORT= 3307
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '12345678'
    MYSQL_DB = 'api_flask'


config = {
    'development': DevelopmentConfig
}