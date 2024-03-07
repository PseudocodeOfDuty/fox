import requests
from fox_data.fox_helper_functions import *
from fox_data.fox_classes import *
from fox_data.fox_models_load import *
from riddle_solvers import riddle_solvers
import random
import time
import numpy as np
import configparser
import requests
import threading


CONFIG_PATH = "fox_config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

API = config["DEFAULT"]["API"]
TEAM_ID = config["DEFAULT"]["TEAM_ID"]
FAKE_MSG = config["DEFAULT"]["FAKE_MSG"]
REAL_CHUNKS_COUNT = int(config["DEFAULT"]["REAL_CHUNKS_COUNT"])
FAKE_CHUNKS_COUNT = int(config["DEFAULT"]["FAKE_CHUNKS_COUNT"])
PROTOCOL_LENGTH = int(config["DEFAULT"]["PROTOCOL_LENGTH"])
CHANNELS_COUNT = int(config["DEFAULT"]["CHANNELS_COUNT"])


def init_fox(team_id):
    st_init = time.time()
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
            ed_init = time.time()  
            print(f"Init run in {ed_init-st_init} seconds")  
            return message, image_carrier
        except Exception as e:
            print("Error parsing response in init:", e)
            return None
    else:
        print("Error in init:", response.status_code)
        return None


def generate_message_array(real_msg, image_carrier):
    msg_st = time.time()
    reals = split_encode(real_msg, image_carrier, REAL_CHUNKS_COUNT)
    fakes = split_encode(FAKE_MSG, image_carrier, FAKE_CHUNKS_COUNT)

    reals_loc = random.sample(range(CHANNELS_COUNT), REAL_CHUNKS_COUNT)

    msgs = [[None for _ in range(CHANNELS_COUNT)] for _ in range(PROTOCOL_LENGTH)]

    for i in range(PROTOCOL_LENGTH):
        msgs[i][reals_loc[i]] = EncodedMSG(reals[i], Entity.REAL)

    fake_filling_i = 0

    for i in range(PROTOCOL_LENGTH):
        for j in range(CHANNELS_COUNT):
            if msgs[i][j] == None:
                msgs[i][j] = EncodedMSG(fakes[fake_filling_i], Entity.FAKE)
                fake_filling_i += 1

    assert fake_filling_i == FAKE_CHUNKS_COUNT

    for i in range(PROTOCOL_LENGTH):
        msgs_channel = EncodedMSG.extractMSGs(msgs[i])
        entities_channel = EncodedMSG.extractEntities(msgs[i])
        # print([decode(np.array(m)) for m in msgs_channel])
        # print(entities_channel)
        while True:
            status = send_message(TEAM_ID, msgs_channel, entities_channel)
            if status == "success":
                break
    msg_ed = time.time()
    print(f"Sent msgs in {msg_ed-msg_st} seconds") 


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
    pass

def submit_fox_attempt(team_id):
    t1 = threading.Thread(target=call_riddle_api)
    message, image_carrier = init_fox(team_id)
    first_3riddles = riddle_solvers[:3]
    riddles_exec(first_3riddles)
    t1.start()
    generate_message_array(message, image_carrier)
    t1.join()
    end_fox(team_id)
    
def test_submit_fox_attempt(team_id):
    t1 = threading.Thread(target=test_call_riddle_api)
    t1.start()
    print("Done")
    print("waiting for response")
    t1.join()
    print("response received")