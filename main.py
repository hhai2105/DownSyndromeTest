import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./img/300.png')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

pixel_value = []
pixel_number = []
current_pixel = 0
print(img)
print(gray_img)
for x in range(len(gray_img)):
	for y in range(len(gray_img[x])):
		pixel_value.append(gray_img[x][y])
		pixel_number.append(current_pixel)
		current_pixel += 1

plt.plot(pixel_number,pixel_value)
plt.show()
