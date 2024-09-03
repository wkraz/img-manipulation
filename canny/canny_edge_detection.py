import cv2 
import matplotlib.pyplot as plt
import sys


if len(sys.argv) != 2:
    raise Exception("Error, must input a file name")

sys_img = sys.argv[1]

img = cv2.imread(sys_img, cv2.IMREAD_GRAYSCALE)

# apply Canny edge detection
edges = cv2.Canny(img, 100, 200)

plt.figure()

# get rid of the file type: .jpeg
img_title = ''
for letter in sys_img:
    if letter == '.':
        break
    img_title = img_title + letter
print(img_title)
    
plt.title(img_title)

# add .png to the end of the title
img_new = img_title + '.png'
print(img_new)

# save the image in a png with just the edges
plt.imsave(img_new, edges, cmap='gray', format='png')
plt.imshow(edges, cmap='gray')
plt.show()