from api import app,mysql
from api.models import *
from flask import jsonify


@app.route("/Choix")
def getChoix(): 
    choix = Choix.getChoix(1) 
    return jsonify(choix)