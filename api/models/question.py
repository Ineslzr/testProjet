from array import array
from api import app,mysql
import json

class Question():
    def __init__(self):
        return 

    @staticmethod
    def getQuestions(id_quiz):
        cur = mysql.connection.cursor()
        cur.execute("SELECT qu.id_question,qu.intitule FROM quiz q, questions qu where q.id_quiz = qu.id_quiz and q.id_quiz = 1")
        fetchdata = cur.fetchall()
        cur.close()
        return fetchdata
