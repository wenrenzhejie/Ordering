from flask import Blueprint
route_api = Blueprint("api_page",__name__)
from web.controllers.api.Member import *

@route_api.route("/")
def index():
    return "mina api V1.0"