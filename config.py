import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'tasks.db')

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'Eu-Não-Sei-pilotar-ua-a-modtod-moto-do-fernando_60945'
