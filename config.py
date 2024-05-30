import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or  b'\xef;\xcc\xd8\xe6\xa0;\x97\xa4T\xb9\xdc2\xb6\x95\xf7'
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///default.db'

