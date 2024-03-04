from transformers import ViltProcessor, ViltForQuestionAnswering
import joblib
from PIL import Image

# Load or initialize your model and processor
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# Save the processor and model using joblib
joblib.dump(processor, "vqa_processor.joblib")
model.save_pretrained("vqa_model")
