import requests
from fox_handlers.fox_riddle_handler import *
from fox_handlers.fox_messaging_handler import *
from solvers.riddle_solvers import riddle_solvers
from fox_handlers.fox_strategy_handler import FoxStrategyPicker
import time
import numpy as np
import configparser
import threading

CONFIG_PATH = "fox_config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

API = config["DEFAULT"]["API"]
TEAM_ID = config["DEFAULT"]["TEAM_ID"]
CHANNELS_COUNT = int(config["DEFAULT"]["CHANNELS_COUNT"])
IS_MP = int(config["DEFAULT"]["MP"])
RIDDLE_CHECKPOINT = int(config["DEFAULT"]["RIDDLE_CHECKPOINT"])


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

def generate_message_array(real_msg, image_carrier,decoder=True):
    st_msg = time.time()
    fsp = FoxStrategyPicker(real_msg,image_carrier)
    msgs = fsp.msgs
    for i in range(fsp.protocol_length):
        msgs_channel = EncodedMSG.extractMSGs(msgs[i])
        entities_channel = EncodedMSG.extractEntities(msgs[i])
        if decoder:
            print([decode(np.array(m)) for m in msgs_channel])
            print(entities_channel)   
        while True:
            status = send_message(TEAM_ID, msgs_channel, entities_channel)
            if status == "success":
                break
    ed_msg = time.time()
    print(f"Messaging Time: {ed_msg-st_msg}")



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
        print("Error in end:", response.status_code)
        return None
    ed_end = time.time()  
    print(f"End run in {ed_end-st_end} seconds")    
    pass

def submit_fox_attempt(team_id):
    print("not mp")
    st_submit = time.time()
    message, image_carrier = init_fox(team_id)
    first_3riddles = dict(list(riddle_solvers.items())[:RIDDLE_CHECKPOINT])
    riddles_exec(TEAM_ID,first_3riddles)
    generate_message_array(message, image_carrier)
    last_7riddles = dict(list(riddle_solvers.items())[RIDDLE_CHECKPOINT:])
    riddles_exec(TEAM_ID, last_7riddles)
    end_fox(team_id)
    ed_submit = time.time()
    print(f"Total Time: {ed_submit-st_submit} seconds")

def mp_submit_fox_attempt(team_id):
    print("mp")
    st_submit = time.time()
    t1 = threading.Thread(target=call_riddle_api)
    message, image_carrier = init_fox(team_id)
    first_3riddles = dict(list(riddle_solvers.items())[:RIDDLE_CHECKPOINT])
    riddles_exec(TEAM_ID,first_3riddles)
    print("Calling riddles process")
    t1.start()
    generate_message_array(message, image_carrier)
    print("Waiting for riddles process")
    t1.join()
    end_fox(team_id)
    ed_submit = time.time()
    print(f"Total Time: {ed_submit-st_submit} seconds")
    
def test_mp():
    t1 = threading.Thread(target=test_call_riddle_api)
    t1.start()
    print("Done")
    print("waiting for response")
    time.sleep(2)
    print("just woke up")
    t1.join()
    print("response received")

def exec():
    if IS_MP==1:
        mp_submit_fox_attempt(TEAM_ID)
    else:
        submit_fox_attempt(TEAM_ID)