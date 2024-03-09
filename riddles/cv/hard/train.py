<<<<<<< HEAD
from transformers import ViltProcessor, ViltForQuestionAnswering
import joblib
from PIL import Image

# Load or initialize your model and processor
# processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# Save the processor and model using joblib
# joblib.dump(processor, "vqa_processor.joblib")
model.save_pretrained("vqa_model")
=======
from transformers import ViltProcessor, ViltForQuestionAnswering
import joblib
from PIL import Image

# Load or initialize your model and processor
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
# model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# Save the processor and model using joblib
joblib.dump(processor, "vqa_processor.joblib")
# model.save_pretrained("vqa_model")
>>>>>>> e2f0945441337302e28f6df6663a2820597ca32c
