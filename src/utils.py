import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from skimage import color

def createPixelArray(img):
    return np.array(img)

def createBinaryImageArray(img):
    BI = []
    for i in range(len(img)):
        line = []
        for j in range(len(img[i])):
            if img[i][j][0] > 1.06 * img[i][j][1] and img[i][j][0] > 1.09 * img[i][j][2]:
                line.append(1)
            else:
                line.append(0)
        BI.append(line)
    return np.reshape(BI, (len(BI), len(BI[0])))

def createBinaryImageFromArray(imgArray, filename="default.jpg"):
    data = Image.fromarray((imgArray * 255).astype(np.uint8))
    data.save(filename)

def initializedict():
    map = []
    for i in range(260):
        map.append(0)
    return map

def createDeltaArray(img):
    margin_of_error = .2
    gray_img=img.convert('L')
    gray_img_array=np.asarray(gray_img)
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

def preprocess(img):
    margin_of_error = .2
    gray_img=img.convert('L')
    gray_img_array=np.asarray(gray_img)
    average = [sum(line)/len(line) for line in gray_img_array]

    # 32 to 75 : T line
    # 194 to 234 : C line
    # max: 255
    c_value = average[int(len(average) * .125): int(len(average) * .3)]
    c_value = sum(c_value) / len(c_value)
    t_value = average[int(len(average) * .76): int(len(average) * .92)]
    t_value = 255 - min(t_value)
    return c_value, t_value

def fitfunction():
    pass
