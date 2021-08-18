from flask import Blueprint

apiBlueprint = Blueprint("main",__name__,url_prefix="/api")

from . import views

