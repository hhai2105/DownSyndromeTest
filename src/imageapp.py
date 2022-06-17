from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt


def order_points(points):
    rect = np.zeros((4,2), dtype="float32")
    
    # find top left and bottom right 
    s = points.sum(axis = 1)
    rect[0] = points[np.argmin(s)]
    rect[2] = points[np.argmax(s)]

    # find top right and bottom left
    # largest difference in x and y

    diff = np.diff(points, axis = 1)
    rect[1] = points[np.argmin(diff)]
    rect[3] = points[np.argmax(diff)]
    return rect

def four_point_transform():
    global image
    global cv2image 
    global points
    global warped
    ps = np.array([point[:2] for point in points])
    rect = order_points(ps)
    (tl, tr, br, bl) = rect
    # find maxWidth of image
    widthA=np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB=np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = int(max(widthA, widthB))
    # find maxHeight of image
    heightA=np.sqrt(((br[0] - tr[0]) ** 2) + ((br[1] - tr[1]) ** 2))
    heightB=np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight=int(max(widthA, widthB))
    dst = np.float32([
        [0,0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]])
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(cv2image, M, (maxWidth, maxHeight))
    print(warped)
    warped = Image.fromarray(warped)
    warped = ImageTk.PhotoImage(warped)
    image_warp_area.create_image(0, 0, image=warped, anchor="nw")

def select_area():
    global points
    image_area.bind("<Button-1>", get_x_and_y)
    image_area.bind("<Button-3>", undo)

def undo(event):
    global points
    holder = points.pop()
    image_area.delete(holder[2])

def get_x_and_y(event):
    global lasx, lasy
    global points 
    if(len(points) < 4):
        lasx, lasy = event.x, event.y
        points.append((lasx, lasy, image_area.create_oval((lasx, lasy, lasx + 1, lasy + 1), fill='red', width=3)))

def openAndPut():
    path = filedialog.askopenfilename()
    global image
    global cv2image
    global warped
    if path:
        image = Image.open(path)
        cv2image = cv2.imread(path)
        cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGB)
        image = ImageTk.PhotoImage(image)
        image_area.create_image(0, 0, image=image, anchor="nw")

points = []
app = Tk()
app.title("image cropping tool")
title = Label(app, text="croptheimage")
title.pack()
image_area = Canvas(app, cursor="cross")
image_area.pack()
image_warp_area = Canvas(app)
image_warp_area.pack()
open_image = Button(app, width=20, text="OPEN IMAGE", command=openAndPut)
open_image.pack()
crop_area = Button(app, width=20, text="SELECT AREA",command=select_area)
crop_area.pack()
show_area = Button(app, width=20, text="SHOW AREA", command=four_point_transform)
show_area.pack()
save_image = Button(app, width=20, text="SAVE IMAGE")
save_image.pack()
app.mainloop()
