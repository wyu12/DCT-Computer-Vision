import apriltag
import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('Data/Olympus50(400ISO)/P7210050.JPG', cv2.IMREAD_GRAYSCALE)
at = img[1025:1175, 3350:3500]

# Run detection on whole image, zoomed apriltag, and rotated apriltag
detector = apriltag.Detector()

# detection on whole image
"""
FAILS (image too large?)
try:
    res_whole = detector.detect(img)
    print "Result (whole image):"
    print res_whole
except:
    print "Detection on whole image failed"
"""
print "Detection on whole image fails (too large?)"

# detection on zoomed apriltag (unrotated)
res_at = detector.detect(at)
print "Result (zoomed apriltag, unrotated):"
print res_at

# detection on zoomed apriltag (rotated)
rows,cols = at.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),-10,1)
rot = cv2.warpAffine(at,M,(cols,rows))
fit = rot[35:89, 45:99]

res_fit = detector.detect(fit)
print "Result (zoomed apriltag, rotated):"
print res_fit

# Plot whole image
plt.figure(0)
plt.imshow(img, cmap="gray")
plt.title("Whole image")

# Plot zoomed apriltag, unrotated
plt.figure(1)
plt.title("Zoomed apriltag, unrotated")
plt.imshow(at, cmap="gray")

# Plot zoomed apriltag, rotated
plt.figure(2)
plt.title("Zoomed apriltag, rotated")
plt.imshow(fit, cmap="gray")

plt.show(block=False)
