import cv2

from riddles.cv.easy.cv_easy_class import Reconstructor as r

# Read the image
image_path = "./riddles/cv/easy/shredded.jpg"
img = cv2.imread(image_path)

# Check the shape of the image array
print("Shape of the image array:", img.shape)
print(type(img))

roro = r()
print(roro.solve(img))

#Expected: [0, 11, 7, 1, 8, 9, 3, 5, 6, 4, 10, 2]
#Output:   [0, 11, 7, 1, 8, 9, 3, 5, 6, 4, 10, 2]
