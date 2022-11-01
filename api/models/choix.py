from api import app,mysql
import json

class Choix():
    def __init__(self):
        return 

    @staticmethod
    def getChoix(id_question):
        id_q=str(id_question)
        cur = mysql.connection.cursor()
        cur.execute("SELECT c.intitule, c.isCorrect FROM choix c, questions qu where c.id_question = qu.id_question and qu.id_question ="+ id_q+";")
        fetchdata = cur.fetchall()
        cur.close()

        #c = {}
        #i = 0
        #while i < len(fetchdata): 
            #c[i] = {"id" :fetchdata[i][0], "intitule" : fetchdata[i][1] }
            #i = i+1

        return fetchdata
