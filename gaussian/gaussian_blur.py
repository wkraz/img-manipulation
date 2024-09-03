import cv2
import matplotlib.pyplot as plt
import sys
import numpy as np

if len(sys.argv) != 2:
    raise Exception("Error, must input a file name")

sys_img = sys.argv[1]

img = cv2.imread(sys_img)

# make our kernel
kernel = np.ones((5, 5), np.float32) / 25
# apply kernel to original image
blur = cv2.filter2D(img, -1, kernel)

plt.figure()

# get rid of the file type: ex: .jpeg
img_title = ''
for letter in sys_img:
    if letter == '.':
        break
    img_title = img_title + letter
    
plt.title(img_title)

# add .png to the end of the title
img_new = img_title + '.png'

# save the image in a png with just the edges
plt.imsave(img_new, blur, format='png')
plt.imshow(blur)
plt.show()
