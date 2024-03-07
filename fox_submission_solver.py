import requests
from fox_data.fox_helper_functions import *
from fox_data.fox_classes import *
from fox_data.fox_models_load import *
from riddle_solvers import riddle_solvers,show_testcase_riddles,show_response_riddles
import random
import time
import numpy as np
import configparser

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
    """
    In this fucntion you need to hit to the endpoint to start the game as a fox with your team id.
    If a sucessful response is returned, you will recive back the message that you can break into chunkcs
    and the carrier image that you will encode the chunk in it.
    """
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
    """
    In this function you will need to create your own startegy. That includes:
        1. How you are going to split the real message into chunkcs
        2. Include any fake chunks
        3. Decide what 3 chuncks you will send in each turn in the 3 channels & what is their entities (F,R,E)
        4. Encode each chunck in the image carrier
    """
    msg_st = time.time()
    reals = splitAndEncode(real_msg, image_carrier, REAL_CHUNKS_COUNT)
    fakes = splitAndEncode(FAKE_MSG, image_carrier, FAKE_CHUNKS_COUNT)

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
    """
    Use this function to call the api end point to send one chunk of the message.
    You will need to send the message (images) in each of the 3 channels along with their entites.
    Refer to the API documentation to know more about what needs to be send in this api call.
    """
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
    """
    Use this function to call the api end point of ending the fox game.
    Note that:
    1. Not calling this fucntion will cost you in the scoring function
    2. Calling it without sending all the real messages will also affect your scoring fucntion
      (Like failing to submit the entire message within the timelimit of the game).
    """
    payload = {
        "teamId": team_id,
    }
    # Send a POST request to the API endpoint
    try:
        response = requests.post(
            API + "/fox/end-game",
            json=payload,
            headers={"content-type": "application/json"},
        )
    except Exception as e:
        print("Error parsing response in send message:", e)
        return None

    # Check if the request was successful (status code 200)
    if response.status_code == 200 or response.status_code == 201:
        # Parse the response JSON and extract the test case
        try:
            print(response.content)
        except Exception as e:
            print("Error parsing response:", e)
            return None
    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code)
        return None
    ed_end = time.time()  
    print(f"End run in {ed_end-st_end} seconds")    
    pass


def submit_fox_attempt(team_id):
    """
     Call this function to start playing as a fox.
     You should submit with your own team id that was sent to you in the email.
     Remeber you have up to 15 Submissions as a Fox In phase1.
     In this function you should:
        1. Initialize the game as fox
        2. Solve riddles
        3. Make your own Strategy of sending the messages in the 3 channels
        4. Make your own Strategy of splitting the message into chunks
        5. Send the messages
        6. End the Game
    Note that:
        1. You HAVE to start and end the game on your own. The time between the starting and ending the game is taken into the scoring function
        2. You can send in the 3 channels any combination of F(Fake),R(Real),E(Empty) under the conditions that
            2.a. At most one real message is sent
            2.b. You cannot send 3 E(Empty) messages, there should be atleast R(Real)/F(Fake)
        3. Refer To the documentation to know more about the API handling
    """
    message, image_carrier = init_fox(team_id)
    first_3riddles = riddle_solvers[:3]
    riddles_exec(first_3riddles)
    #Call API RIDDLE SOLVER
    generate_message_array(message, image_carrier)
    