import apriltag
import cv2
import numpy as np
import matplotlib.pyplot as plt

#cap = cv2.VideoCapture(0)
detector = apriltag.Detector()

img = cv2.imread("data/apriltags.png", cv2.IMREAD_GRAYSCALE)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result = detector.detect(img)
print(result)

# draw a bounding quadrilateral (optional)
if len(result) > 0:
    for res in result:
        pts = np.array(res.corners, dtype=np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 0), 3)

# display image
cv2.imshow('frame', img)
