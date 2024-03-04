class cv_hard:

    def solve(self, img, question, loaded_processor, loaded_model):
        # Use the loaded processor to prepare inputs
        new_encoding = loaded_processor(img, question, return_tensors="pt")

        # Forward pass with the loaded model
        new_outputs = loaded_model(**new_encoding)
        new_logits = new_outputs.logits
        new_idx = new_logits.argmax(-1).item()
        res = loaded_model.config.id2label[new_idx]
        try:
            res = int(res)
            return res
        except ValueError:
            return 3
