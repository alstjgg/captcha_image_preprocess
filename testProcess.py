import cv2
from matplotlib import pyplot as plt


# Test image binarisation
def test_binarisation(given_image):
    # Simple Thresholding + Binary(Threshold = 125)
    thresh, binary = cv2.threshold(given_image, 125, 255,
                                   cv2.THRESH_BINARY)
    # Simple Thresholding + Binary(Threshold = value of left bottom pixel)
    t = given_image[0][0]
    thresh, binary_thresh = cv2.threshold(given_image, t, 255,
                                          cv2.THRESH_BINARY)
    # Adaptive Thresholding + Gaussian + Binary
    gaussian = cv2.adaptiveThreshold(given_image, 255,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 15, 2)

    titles = ['original', 'simple binary 125', 'simple binary', 'adaptive']
    images = [given_image, binary, binary_thresh, gaussian]
    for i in range(4):
        plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


# Test morphology
def test_morphology(given_image):
    shape = cv2.MORPH_RECT
    kernel_size = (2, 4)
    kernel = cv2.getStructuringElement(shape, kernel_size)

    titles = ['original', 'dilation', 'erosion', 'closed']
    images = [given_image,
              cv2.dilate(given_image, kernel, iterations=1),
              cv2.erode(given_image, kernel, iterations=1),
              cv2.morphologyEx(given_image, cv2.MORPH_CLOSE, kernel)]
    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


# Test blur
def test_blur(given_image):
    average = cv2.blur(given_image, (5, 5))
    gaussian = cv2.GaussianBlur(given_image, (5, 5), 0)
    median = cv2.medianBlur(given_image, 5)
    bilateral = cv2.bilateralFilter(given_image, 9, 75, 75)

    titles = ['original', 'averaging', 'gaussian blur',
              'median blur', 'bilateral filter']
    images = [given_image, average, gaussian, median, bilateral]

    plt.subplot(3, 2, 1), plt.imshow(images[0], 'gray')
    plt.title(titles[0])
    plt.xticks([]), plt.yticks([])

    for i in range(1, 5):
        plt.subplot(3, 2, i + 2), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()
