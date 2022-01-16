from flask import request
from . import mainBlueprint
from flask import current_app
from time import time

def shutdownServer():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()

@mainBlueprint.route("/")
def index():
    return current_app.send_cleclstatic_file("index.html")

@mainBlueprint.route("/time")
def getCurrentTime():
    return {"time": time()}

@mainBlueprint.route("/ready")
def ready():
    return {"ready": 0}
