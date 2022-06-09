import numpy as np
import cv2

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

def four_point_transform(img, points):
    rect = order_points(points)
    (tl, tr, br, bl) = rect
    # find maxWidth of image
    widthA=np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB=np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(widthA, widthB)
    # find maxHeight of image
    heightA=np.sqrt(((br[0] - tr[0]) ** 2) + ((br[1] - tr[1]) ** 2))
    heightB=np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight=max(widthA, widthB)
    dst = np.array([
        [0,0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1], dtype = "float32"
    ])
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(img, M, (maxWidth, maxHeight))
    
    return warpeed
