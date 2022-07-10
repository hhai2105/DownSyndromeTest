from utils import *
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from scipy.optimize import curve_fit
import os

# open image and convert it to grayscale

directory = "../img/original/"
arr = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    img=Image.open(f)
    concentrationValue = filename.split(".")[0]
    c_value, t_value = preprocess(img)
    arr.append((c_value, t_value, int(concentrationValue)))

# plt.scatter([value[2] for value in arr], [value[1] for value in arr])
# mymodel = np.poly1d(np.polyfit([value[2] for value in arr], [value[1] for value in arr], 3))
# myline = np.linspace(1, 1000, 100)
# plt.plot(myline, mymodel(myline))
# plt.show()

x = [np.log(value[2] + 1) for value in arr]
y = [value[1] for value in arr]

def f(x, p_0, p_1):
    return p_0 * x + p_1


guesses = (1, 1)

yerr = [.1 for i in x]
(p_0, p_1), cc = curve_fit(f, x, y, p0=guesses, sigma=yerr)


xmod = np.linspace(0, np.log(1000), 100) #Generate x values between initial and end
ymod = f(xmod, p_0, p_1)

plt.scatter(x,y)
plt.plot(xmod,ymod)
plt.show()
