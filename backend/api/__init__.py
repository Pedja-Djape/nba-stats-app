from flask import Blueprint

apiBlueprint = Blueprint("api",__name__,url_prefix="/api")

from . import views

