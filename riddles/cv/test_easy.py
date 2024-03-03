import cv2

from cv.reconstructor import reconstructor as r

# Read the image
image_path = "shredded.jpg"
img = cv2.imread(image_path)

# Check the shape of the image array
print("Shape of the image array:", img.shape)
print(type(img))

roro = r()
roro.solve(img)
