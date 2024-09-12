import apriltag
import cv2
import numpy as np


#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


	# slide a window across the image
def reader(img):
    tagList = []
    global img2
    for y in range(0, img.shape[0], 350):
        for x in range(0, img.shape[1], 350):
           
            result, img2 = detector.detect(img[y:y + 450, x:x + 450], return_image = True)
            if ((len(result) != 0) and result not in tagList): 
                tagList.append(result)
                print(result)
                cv2.imwrite("output.jpg",img2)



if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    detector = apriltag.Detector()
    img = cv2.imread("data/Track 10-22/90_0.png", cv2.IMREAD_GRAYSCALE)
    reader(img)
    cap.release()
    cv2.destroyAllWindows()
