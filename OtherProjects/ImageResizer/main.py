import cv2
import matplotlib.pyplot as plt

src = "img.jpg"
dest = "resize_image.jpeg"

image = cv2.imread(src)
# cv2.imshow("title", image)
scale_percent = int(input())
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

# Resizing Image
output = cv2.resize(image, (new_width, new_height))
cv2.imwrite(dest, output)
cv2.waitKey(0)
