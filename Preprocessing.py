import numpy as np
import pytesseract
import cv2


# Binarisation & Noise Removal
def bw(original_image):
    t1 = original_image[0][0]
    t2 = original_image[0][original_image.shape[1]-1]
    t3 = original_image[original_image.shape[0]-1][0]
    t4 = original_image[original_image.shape[0]-1][original_image.shape[1]-1]
    t = min(t1, t2, t3, t4)
    if t == 255:
        bw_img = cv2.adaptiveThreshold(original_image, 255,
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY, 15, 2)
    else:
        thresh, bw_img = cv2.threshold(original_image, t, 255,
                                       cv2.THRESH_BINARY)
    return bw_img


# Image Cropping
def crop_image(original_image):
    cut = 5     # Boundary of image that is definitely not text
    x_list, y_list = [], []
    corners = cv2.goodFeaturesToTrack(original_image, 200, 0.01, 6)
    corners = np.int0(corners)
    for i in corners:
        x, y = i.ravel()
        if x > cut and y > cut:
            x_list.append(x)
            y_list.append(y)
    xl = min(x_list)
    xr = max(x_list)
    yt = min(y_list)
    yb = max(y_list)

    cr_img = cv2.copyMakeBorder(original_image[yt:yb, xl:xr],
                                5, 5, 5, 5, cv2.BORDER_CONSTANT, value=255)
    return cr_img


# Closing (Dilation -> Erosion)
def morph_image(original_image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 4))
    mor_img = cv2.morphologyEx(original_image, cv2.MORPH_CLOSE, kernel)
    return mor_img


# Blur image
def blur_image(original_image):
    return cv2.medianBlur(original_image, 3)


# Return original image
def return_image(original_image):
    return original_image


def tesseract(given_image):
    pytesseract.pytesseract.tesseract_cmd =\
        r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    return pytesseract.image_to_string(given_image, lang='eng', config="-psm 6 digits")

