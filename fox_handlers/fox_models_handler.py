from transformers import ViltForQuestionAnswering
import joblib
import os

if os.name == "nt":
    # ML_MID_MODEL = "riddles/ml/AdaBoostModel_win.joblib"
    ML_MID_MODEL = "riddles/ml/KNNModel.joblib"
    CV_HARD_MODEL = "riddles/cv/hard/vqa_processor_win.joblib"
elif os.name == "posix":
    # ML_MID_MODEL = "riddles/ml/AdaBoostModel_linux.joblib"
    ML_MID_MODEL = "riddles/ml/KNNModel.joblib"
    CV_HARD_MODEL = "riddles/cv/hard/vqa_processor_linux.joblib"
else:
    raise ValueError("Unsupported operating system")

loaded_processor_cv_hard = joblib.load(CV_HARD_MODEL)
loaded_model_cv_hard = ViltForQuestionAnswering.from_pretrained("riddles/cv/hard/vqa_model")
loaded_model_ml_medium = joblib.load(ML_MID_MODEL)