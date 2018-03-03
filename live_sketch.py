import cv2
import numpy as np

def sketch(image):
    #convert image to greyscale
    img_gray = cv2.cvtcColor(image, cv2.COLOR_BGR2GRAY)

    #clean up image using Gaussian Blur
    img_gray_blur = cv2.GaussianBlue(img_gray, (5,5), 0)

    #Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
