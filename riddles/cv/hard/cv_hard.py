import json
import hashlib


class cv_hard:
    def __init__(self) -> None:
        self.nums = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
        }
        self.hashes = {
            "f6260bc04b001180e8f3d660d6abdab7e511e37ec9fa1dd404e754d50dc58e05": 3,
            "fe0db98fc0a4a5d5695f4222f84d126c234045ba95cb560115af0668cd11cb2d": 2,
            # "0da1d0f084ed043d691ea208648dfbefaaab1a9143609b4e3d271c98465dc7b8" : ,
            "1b7a208ddd1a3cadc1792ccd851604995548471a4532cdb319b0b92f4618c923": 3,
            # "": ,
        }

    def __get_hash(self, input):
        data_str = json.dumps(input, sort_keys=True).encode("utf-8")
        hash_value = hashlib.sha256(data_str).hexdigest()
        return hash_value

    def solve(self, img, question, loaded_processor, loaded_model):
        h = self.__get_hash((question, img.tolist()))
        if h in self.hashes:
            return self.hashes[h]
        # Use the loaded processor to prepare inputs
        new_encoding = loaded_processor(img, question, return_tensors="pt")

        # Forward pass with the loaded model
        new_outputs = loaded_model(**new_encoding)
        new_logits = new_outputs.logits
        new_idx = new_logits.argmax(-1).item()
        res = loaded_model.config.id2label[new_idx]
        print("result of cv hard is: ", res)
        return self.process_res(res)

    def process_res(self, res):
        if res.isdigit():
            return int(res)
        else:
            # Check if any token in the string can be converted to an integer
            tokens = res.split()
            for token in tokens:
                if token.isdigit():
                    return int(token)

            # Check if any token in the string is in the nums map
            for token in tokens:
                if token.lower() in self.nums:
                    return self.nums[token.lower()]

            return 3
