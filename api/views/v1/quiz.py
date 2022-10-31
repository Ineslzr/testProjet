from api import app,mysql
from api.models import *
from flask import jsonify


@app.route("/Quiz")
def CreateQuiz():      
    nom_quiz = Quiz.getNom() 
    questions = Question.getQuestions(1)
    
    quiz = {"questions" : questions }

    y = 0
    while y < len(quiz["questions"]): 
       quiz["questions"][y]["choix"] = Choix.getChoix(questions[y]["id_question"])
       y = y+1

    return jsonify(quiz)
