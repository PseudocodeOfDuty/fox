from LSBSteg import encode
import time
from fox_submission_solver import get_riddle,show_reponse_riddles,show_testcase_riddles,solve_riddle

def splitAndEncode(msg,img,chunks_count):
    def is_last_chunk(i):
        return i==chunks_count-1
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

def riddles_exec(team_id,riddles_list):
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
            if riddle_id in show_reponse_riddles:
                print(f"Riddle {riddle_id}: {solution}")
            response = solve_riddle(team_id, solution)
            print(f"Response {riddle_id}: {response}")
            riddle_ed = time.time()
            print(f"Solved {riddle_id} in {riddle_ed-riddle_st} seconds")
