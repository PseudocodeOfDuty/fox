from flask import Flask
from flask_cors import CORS 
from fox_data.fox_models_load import *
from fox_submission_solver import riddle_solvers,riddles_exec,TEAM_ID,end_fox
import time


app = Flask(__name__)
CORS(app)

@app.route('/fox/solve-rest')
def solveRest():
    last_7riddles = riddle_solvers[3:]
    riddles_exec(TEAM_ID,last_7riddles)
    end_fox(TEAM_ID)


if __name__ == '__main__':
    app.run()
