import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    TEST = False


class TestingConfig(Config):
    DB_NAME = 'mongoenginetest'
    HOST = 'mongomock://localhost'
    ALIAS = 'testdb'
    TEST = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY")


config_dict = {
    'TEST': TestingConfig,
    'DEV': DevelopmentConfig,
    'PRODUCTION': ProductionConfig
}
