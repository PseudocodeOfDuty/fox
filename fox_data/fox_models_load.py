# from transformers import ViltForQuestionAnswering
# import joblib
import os

if os.name == "nt":
    ML_MID_MODEL = "riddles/ml/AdaBoostModel_win.joblib"
    CV_HARD_MODEL = "riddles/cv/hard/vqa_processor_win.joblib"
elif os.name == "posix":
    ML_MID_MODEL = "riddles/ml/AdaBoostModel_linux.joblib"
    CV_HARD_MODEL = "riddles/cv/hard/vqa_processor_linux.joblib"
else:
    raise ValueError("Unsupported operating system")

loaded_processor_cv_hard = "lol" # joblib.load(CV_HARD_MODEL)
loaded_model_cv_hard = "lol" # ViltForQuestionAnswering.from_pretrained("riddles/cv/hard/vqa_model")
loaded_model_ml_medium = "lol" # joblib.load(ML_MID_MODEL)