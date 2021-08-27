
from . import apiBlueprint

@apiBlueprint.route("/hi")
def pleaaase():
    return "Hello from the api"