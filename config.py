import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI =  'mysql://apps:apps@127.0.0.1/apps'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
#    MAIL_USE_SSL = True
    MAIL_USERNAME = 'khurtinatat98@gmail.com'
    MAIL_DEFAULT_SENDER = 'khurtinatat98@gmail.com'
    MAIL_PASSWORD = 'sienta326'
#    ADMINS = ['khurtinatat98@gmail.com']

