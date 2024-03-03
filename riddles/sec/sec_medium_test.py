from riddle_solvers import solve_sec_medium
from PIL import Image
import torchvision.transforms as transforms

image_path = "SteganoGAN/sample_example/encoded.png"
image = Image.open(image_path)
preprocess = transforms.Compose([
    transforms.ToTensor(),
])
image_tensor = preprocess(image)
print(type(image_tensor))
image_tensor = image_tensor.unsqueeze(0) #Could be added to function
result = solve_sec_medium(image_tensor)
print(result)