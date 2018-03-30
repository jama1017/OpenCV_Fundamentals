import cv2
import numpy as np

# Load image
image = cv2.imread("images/blobs.jpg", 0)
cv2.imshow('Original Image',image)
cv2.waitKey(0)

# Intialize the detector using the default parameters
detector = cv2.SimpleBlobDetector()

# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Total Number of Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

# Display image with blob keypoints
cv2.imshow("Blobs using default parameters", blobs)
cv2.waitKey(0)
