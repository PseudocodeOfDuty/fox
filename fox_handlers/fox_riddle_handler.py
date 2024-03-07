import time
from solvers.riddle_solvers import show_response_riddles, save_testcase_riddles
from fox_handlers.fox_models_handler import *
import requests
import configparser
import json

CONFIG_PATH = "fox_config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

API = config["DEFAULT"]["API"]
TEAM_ID = config["DEFAULT"]["TEAM_ID"]


def get_riddle(team_id, riddle_id):
    payload = {"teamId": team_id, "riddleId": riddle_id}
    response = requests.post(
        API + "/fox/get-riddle",
        json=payload,
        headers={"content-type": "application/json"},
    )
    if response.status_code == 200 or response.status_code == 201:
        try:
            response_json = response.json()
            test_case = response_json["test_case"]
            return test_case
        except Exception as e:
            print("Error parsing response:", e)
            return None
    else:
        print("Error:", response.status_code)
        return None


def solve_riddle(team_id, solution):
    payload = {"teamId": team_id, "solution": solution}
    try:
        response = requests.post(
            API + "/fox/solve-riddle",
            json=payload,
            headers={"content-type": "application/json"},
        )
    except Exception as e:
        print(e)
        return None
    if response.status_code == 200 or response.status_code == 201:
        try:
            response_json = response.json()
            budget_increase = response_json["budget_increase"]
            total_budget = response_json["total_budget"]
            status = response_json["status"]
            return budget_increase, total_budget, status
        except Exception as e:
            print("Error parsing response:", e)
            return None
    else:
        print("Error:", response.status_code)
        return None


def riddles_exec(team_id, riddles_list):
    for riddle_id, solver in riddles_list.items():
        riddle_st = time.time()
        testcase = get_riddle(team_id, riddle_id)
        if riddle_id in save_testcase_riddles:
            # print(f"Riddle {riddle_id}: {testcase}")
            try:
                filename = f"{riddle_id}_testcase.json"
                with open(filename, "w") as file:
                    json.dump(testcase, file)
            except:
                print(f"Error in printing {riddle_id}")
        if testcase is None:
            continue
        else:
            try:
                if riddle_id == "cv_hard":
                    solution = solver(testcase, loaded_processor_cv_hard, loaded_model_cv_hard)
                elif riddle_id == "ml_medium":
                    solution = solver(testcase, loaded_model_ml_medium)
                else:
                    solution = solver(testcase)
            except Exception as e:
                print(f"Error solving riddle {riddle_id}:", e)
                continue
            if riddle_id in show_response_riddles:
                print(f"Riddle {riddle_id}: {solution}")
            response = solve_riddle(team_id, solution)
            print(f"Response {riddle_id}: {response}")
            riddle_ed = time.time()
            print(f"Solved {riddle_id} in {riddle_ed-riddle_st} seconds")

def call_riddle_api():
    response = requests.get('http://127.0.0.1:5000/fox/solve-rest')
    return response.text

def test_call_riddle_api():
    response = requests.get('http://127.0.0.1:5000/fox/solve-rest-test')
    return response.text
