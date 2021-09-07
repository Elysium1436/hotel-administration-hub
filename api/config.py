import os


class Config:
    DEBUG = False


class TestingConfig(Config):
    DB_NAME = 'mongoenginetest'
    HOST = 'mongomock://localhost'
    ALIAS = 'testdb'


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass
