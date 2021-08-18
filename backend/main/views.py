from . import mainBlueprint
from flask import render_template, request, redirect, url_for, current_app
from time import time


@mainBlueprint.route("/")
def index():
    return current_app.send_static_file("index.html")

@mainBlueprint.route("/time")
def getCurrentTime():
    return {"time": time()}