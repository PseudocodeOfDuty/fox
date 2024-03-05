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

    def solve(self, img, question, loaded_processor, loaded_model):
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
