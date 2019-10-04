import cv2
import numpy as np


def show(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def to_binary(img):
    threshold = 220  # 170 <= threshold <= 220 for best results
    _, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return img


def rotate(img, angle):
    rows, cols = img.shape
    matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    return cv2.warpAffine(img, matrix, (cols, rows))


def straighten(img):
    angle = 0
    max_rate = 0
    max_angle = 0

    while angle < 90:
        rotated = rotate(img, angle)

        # Get amount of white in each row
        row_sums = []
        for i in range(rotated.shape[0]):
            row_sum = sum(rotated[i, :])
            row_sums.append(row_sum)

        # Normalize range to (0, 1)
        row_sums = list((np.array(row_sums) / max(row_sums)) * 1)
        print(row_sums)

        # Get first instance of white
        i = 0
        while i < len(row_sums) - 1 and row_sums[i + 1] < 0.03:
            i += 1

        # Calculate how rapidly image changes from black to white
        # The greater the rate, the straighter the image is
        k = i
        while k < len(row_sums) and row_sums[k] < 0.97:
            k += 1
        rate = 1.0 / (k - i)
        # dx = 4
        # rate = 0 if i + dx >= len(row_sums) else (row_sums[i + dx] - row_sums[i]) / dx

        # Get angle of straightest image
        if rate > max_rate:
            max_rate = rate
            max_angle = angle

        angle += 0.2

    return rotate(img, max_angle)


def main():
    # Read image
    img = cv2.imread('data/cropped_image.png', cv2.IMREAD_GRAYSCALE)
    img = to_binary(img)
    img = straighten(img)
    show(img)


if __name__ == '__main__':
    main()
