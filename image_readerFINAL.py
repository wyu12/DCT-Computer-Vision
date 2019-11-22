import apriltag
import cv2
import numpy as np
import sys
#import matplotlib.pyplot as plt
import os
import multiprocessing

try:
    fname = sys.argv[1]
except:
    fname = "data/apriltags.png"

detector = apriltag.Detector()

img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
thresh, img= cv2.threshold(img,127,255,cv2.THRESH_BINARY)

options=apriltag.DetectorOptions(border=1,debug=True,refine_edges=True)
detector.options=options
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result, img2 = detector.detect(img, return_image = True)
print(result)
print(len(result))

output_fname = fname.split(".")[0] + "_output.jpg"
if len(result) > 0:
    cv2.imwrite(output_fname, img2)

# write to logfile
write = True
if write:
    with open("log.csv", "a+") as f:
        for res in result:
            f.write(fname +","+ res.tag_family +","+ str(res.tag_id)+","+output_fname+"\n")

# draw a bounding quadrilateral (optional)
for res in result:
    pts = np.array(res.corners, dtype=np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (255, 0, 0), 3)

# display image
cv2.imshow('frame', img)
