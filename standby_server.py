from flask import Flask
from flask_cors import CORS
from fox_data.fox_models_load import *
from fox_submission_solver import riddle_solvers, riddles_exec
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
    # last_7riddles = riddle_solvers[3:]
    # riddles_exec(TEAM_ID, last_7riddles)
    print("Solving riddles")
    time.sleep(5)
    print("Riddles solved")
    return "Done"

@app.route("/fox/solve-rest-test")
def solveRestTest():
    print("Solving riddles")
    time.sleep(5)
    print("Riddles solved")
    return "Done"




if __name__ == "__main__":
    app.run()
