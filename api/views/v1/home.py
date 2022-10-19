from api import app,mysql


@app.route("/")
def Home():
    return {"Home": "Welcome"}