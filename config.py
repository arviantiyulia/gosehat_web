import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://andwjjsbvfhzxh:e88dcd61f880c6d6cd983d5118365fd23a745fd3b0b9c5e04567eb3af5519a14@ec2-184-73-169-151.compute-1.amazonaws.com/dbk8mnhi8mgcv8'