import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# open image and convert it to grayscale
img=Image.open('./img/100.png')
gray_img=img.convert('L')
gray_img_array=np.asarray(gray_img)
margin_of_error = 2;
map = [];

def initializedict():
	for i in range(260):
		map.append(0)

initializedict()

pixel_value = []
delta_value = []
pixel_number = []
current_pixel = 0
for x in range(len(gray_img_array)):
		average = 0
		for y in range(len(gray_img_array[x])):
			average += gray_img_array[x][y]
			current_pixel += 1
		# find average value for every x value
		average /= len(gray_img_array[x])
		average = int(round(average))
		for i in range(average - margin_of_error, average + margin_of_error):
			map[i] +=1
		pixel_value.append(average)
		if(len(pixel_value) > 1):
			delta_value.append(pixel_value[len(pixel_value) - 1] - pixel_value[len(pixel_value) - 2])
		pixel_number.append(current_pixel)

plt.plot(delta_value)
plt.plot(pixel_number, pixel_value)
plt.show()
