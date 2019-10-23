import apriltag
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
import os

try:
    fname = sys.argv[1]
except:
    fname = "data/apriltags.png"

detector = apriltag.Detector()

img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result = detector.detect(img)
print(result)

# write to logfile
write = True
if write:
    with open("log.csv", "a+") as f:
        for res in result:
            f.write(fname +","+ res.tag_family +","+ str(res.tag_id)+"\n")

# draw a bounding quadrilateral (optional)
for res in result:
    pts = np.array(res.corners, dtype=np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (255, 0, 0), 3)

# display image
cv2.imshow('frame', img)
