# coding=utf-8

class ApplicationConfig:
    # databases info
    POSTGRES_USERNAME = 'postgres'
    POSTGRES_PW = 'password'
    POSTGRES_SERVER = 'database:5432'
    POSTGRES_DBNAME00 = 'clearnet'
    SQLALCHEMY_DATABASE_URI_0 = "postgresql+psycopg2://{}:{}@{}/{}".format(POSTGRES_USERNAME,
                                                                           POSTGRES_PW,
                                                                           POSTGRES_SERVER,
                                                                           POSTGRES_DBNAME00)
    SQLALCHEMY_BINDS = {'clearnet': SQLALCHEMY_DATABASE_URI_0}


    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # Mail Configuration
    MAIL_SERVER = 'test.test.fuckgoogle'
    MAIL_PORT = 465
    MAIL_USERNAME = 'test@test.com'
    MAIL_PASSWORD = 'test'
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_DEBUG = True
    MAIL_DEFAULT_SENDER = '"test.com" <test@test.com>'










