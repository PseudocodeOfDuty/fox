import hashlib
import json

with open("riddles/cv/hard/images/cv_hard_testcase5_f.json", "r") as f:
    data = json.load(f)
    print(data[0])

data_str = json.dumps((data[0], data[1]), sort_keys=True).encode("utf-8")
hash_value = hashlib.sha256(data_str).hexdigest()
print(hash_value)
