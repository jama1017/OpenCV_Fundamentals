import cv2
import numpy as np

def sketch(image):
    #convert image to greyscale
    img_gray = cv2.cvtcColor(image, cv2.COLOR_BGR2GRAY)

    #clean up image using Gaussian Blur
    img_gray_blur = cv2.GaussianBlue(img_gray, (5,5), 0)

    #Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    #Invert to binarize the image
    ret, mask = cv2.threshold(canny_edges, 70, 255, c2.THRESH_BINARY_INV)

    return mask

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow('Sketchy', sketch(frame))
    if cv2.waitKey(1) == 13: #13 is the Enter waitKey
        break

capture.release()
cv2.destroyAllWindows()
