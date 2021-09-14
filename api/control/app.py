from flask import Flask, request
from flask_restx.marshalling import marshal
from ..config import config_dict
import os
from flask_restx import Api, Resource, fields
from dotenv import load_dotenv
from ..service import user_service, database_setup
from .blueprints.rest_api.api_utils import jwt
from .blueprints.rest_api.main_api import api

load_dotenv()

app = Flask(__name__)
app.config.from_object(config_dict[os.getenv("CONFIG")])

database_setup.global_init()


jwt.init_app(app)
api.init_app(app)
