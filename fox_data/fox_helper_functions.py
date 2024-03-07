from LSBSteg import encode
import time
from riddle_solvers import show_response_riddles, show_testcase_riddles
import requests
import configparser

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


def splitAndEncode(msg, img, chunks_count):
    def is_last_chunk(i):
        return i == chunks_count - 1

    chunk_len = len(msg) // chunks_count
    encoded_chunks = []
    for i in range(chunks_count):
        if is_last_chunk(i):
            msg_chunk = msg[i * chunk_len :]
        else:
            msg_chunk = msg[i * chunk_len : (i + 1) * chunk_len]
        img_copy = img.copy()
        encoded_chunks.append(encode(img_copy, msg_chunk))
    return encoded_chunks


def riddles_exec(team_id, riddles_list):
    for riddle_id, solver in riddles_list.items():
        riddle_st = time.time()
        testcase = get_riddle(team_id, riddle_id)
        if riddle_id in show_testcase_riddles:
            print(f"Riddle {riddle_id}: {testcase}")
        if testcase is None:
            continue
        else:
            try:
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
