from flask import Flask
from flask_cors import CORS
from fox_handlers.fox_models_handler import *
from solvers.riddle_solvers import mp_riddle_solvers
from solvers.fox_submission_solver import riddles_exec
import configparser
import time

CONFIG_PATH = "fox_config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

TEAM_ID = config["DEFAULT"]["TEAM_ID"]


app = Flask(__name__)
CORS(app)


@app.route("/fox/solve-rest")
def solveRest():
    print("Riddles process started execution")
    last_7riddles = dict(list(mp_riddle_solvers.items())[3:])
    riddles_exec(TEAM_ID, last_7riddles)
    print("Riddles process done")
    return "Done"

@app.route("/fox/solve-rest-test")
def solveRestTest():
    print("Solving riddles")
    time.sleep(5)
    print("Riddles solved")
    return "Done"

if __name__ == "__main__":
    app.run()
