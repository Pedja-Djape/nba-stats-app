from backend import create_app

app = create_app()

app.route("/")
def index():
    return {"what": "yes"}