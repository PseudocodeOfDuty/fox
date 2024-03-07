import requests
from fox_data.fox_helper_functions import *
from fox_data.fox_messaging_classes import *
from fox_data.fox_models_load import *
from riddle_solvers import riddle_solvers,show_testcase_riddles,show_reponse_riddles
from strategy_picker import FoxStrategyPicker
import time
import numpy as np
import configparser
import json

CONFIG_PATH = "fox_config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

API = config["DEFAULT"]["API"]
TEAM_ID = config["DEFAULT"]["TEAM_ID"]
FAKE_MSG = config["DEFAULT"]["FAKE_MSG"]
REAL_CHUNKS_COUNT = int(config["DEFAULT"]["REAL_CHUNKS_COUNT"])
FAKE_CHUNKS_COUNT = int(config["DEFAULT"]["FAKE_CHUNKS_COUNT"])
EMPTY_CHUNKS_COUNT = int(config["DEFAULT"]["EMPTY_CHUNKS_COUNT"])
PROTOCOL_LENGTH = int(config["DEFAULT"]["PROTOCOL_LENGTH"])
CHANNELS_COUNT = int(config["DEFAULT"]["CHANNELS_COUNT"])



def init_fox(team_id):
    payload = {"teamId": team_id}
    response = requests.post(
        API + "/fox/start", json=payload, headers={"content-type": "application/json"}
    )
    if response.status_code == 200 or response.status_code == 201:
        try:
            response_json = response.json()
            message = response_json["msg"]
            image_carrier = np.array(response_json["carrier_image"])
            # print(f"msg: {message}")
            # print(f"carrier {image_carrier}")
            return message, image_carrier
        except Exception as e:
            print("Error parsing response in init:", e)
            return None
    else:
        print("Error in init:", response.status_code)
        return None


def generate_message_array(real_msg, image_carrier,decoder=True):
    reals = split_encode(real_msg, image_carrier, REAL_CHUNKS_COUNT)
    fakes = split_encode(FAKE_MSG, image_carrier, FAKE_CHUNKS_COUNT)
    empty = make_empty(image_carrier)
    msgs = FoxStrategyPicker(reals,fakes,empty)
    for i in range(PROTOCOL_LENGTH):
        msgs_channel = EncodedMSG.extractMSGs(msgs[i])
        entities_channel = EncodedMSG.extractEntities(msgs[i])
        if decoder:
            print([decode(np.array(m)) for m in msgs_channel])
            print(entities_channel)   
        while True:
            status = send_message(TEAM_ID, msgs_channel, entities_channel)
            if status == "success":
                break


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


def send_message(team_id, messages, message_entities):
    payload = {
        "teamId": team_id,
        "messages": messages,
        "message_entities": message_entities,
    }
    try:
        response = requests.post(
            API + "/fox/send-message",
            json=payload,
            headers={"content-type": "application/json"},
        )
    except Exception as e:
        print(e)
        return None
    if response.status_code == 200 or response.status_code == 201:
        try:
            response_json = response.json()
            status = response_json["status"]
            return status
        except Exception as e:
            print("Error parsing response in send message:", e)
            return None
    else:
        print("Error in send message:", response.status_code)
        return None


def end_fox(team_id):
    st_end = time.time()
    payload = {
        "teamId": team_id,
    }
    try:
        response = requests.post(
            API + "/fox/end-game",
            json=payload,
            headers={"content-type": "application/json"},
        )
    except Exception as e:
        print("Error parsing response in send message:", e)
        return None
    if response.status_code == 200 or response.status_code == 201:
        try:
            print(response.content)
        except Exception as e:
            print("Error parsing response:", e)
            return None
    else:
        print("Error:", response.status_code)
        return None
    ed_end = time.time()  
    print(f"End run in {ed_end-st_end} seconds")  


def submit_fox_attempt(team_id):
    st_init = time.time()
    message, image_carrier = init_fox(team_id)
    ed_init = time.time()  
    print(f"Init run in {ed_init-st_init} seconds")  
    riddle_idx = 0
    for riddle_id, solver in riddle_solvers.items():
        riddle_st = time.time()
        if riddle_idx==3:
            msg_st = time.time()
            generate_message_array(message, image_carrier)
            msg_ed = time.time()
            print(f"Sent msgs in {msg_ed-msg_st} seconds") 
        riddle_idx += 1
        testcase = get_riddle(team_id, riddle_id)
        if riddle_id in show_testcase_riddles:
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
                print("Error in solver:", e)
                continue
            if riddle_id in show_reponse_riddles:
                print(f"Riddle {riddle_id}: {solution}")
            response = solve_riddle(team_id, solution)
            print(f"Response {riddle_id}: {response}")
            riddle_ed = time.time()
            print(f"Solved {riddle_id} in {riddle_ed-riddle_st} seconds")
    end_fox(team_id)


# total_st = time.time()
# submit_fox_attempt(TEAM_ID)
# total_ed = time.time()
# print(f"Total Time: {total_ed-total_st} seconds")

