class ml_medium:

    def solve(self, new_point, loaded_model):
        predicted_label = loaded_model.predict([new_point])[0]
        return int(predicted_label)