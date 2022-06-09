from utils import *
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# open image and convert it to grayscale

img=Image.open('../img/100.png')
pix=createPixelArray(img)
print(type(pix))
BI = createBinaryImageArray(pix)
print(BI)

createBinaryImageFromArray(BI)


