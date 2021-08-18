from . import apiBlueprint

from flask import request, url_for, current_app

apiBlueprint.route("/testAPIBlueprint")
def test():
    return "Hello from the the API Blueprint! Test succeeded"