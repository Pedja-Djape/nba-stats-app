from flask import Blueprint

mainBlueprint = Blueprint("main",__name__)

from . import views