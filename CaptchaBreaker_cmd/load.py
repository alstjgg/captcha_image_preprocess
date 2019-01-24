import requests
import cv2
import numpy as np


# Download captcha images from link and save
def get_image_link(link):
    """Download image from given url.

    :param link: given url where image is located
    :return: image downloaded from url
    """
    req = requests.get(link)
    try:
        req.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % exc)
    loaded_image = req.content
    loaded_image = cv2.imdecode(np.asarray(bytearray(loaded_image)), 1)
    loaded_image = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)
    return loaded_image


# Get image from external file(path)
def get_image_path(path):
    """Load image from local directory.

    :param path: given path where image is stored
    :return: image loaded from directory
    """
    loaded_image = cv2.imread(path)
    loaded_image = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)
    label = ((path.split('/')[-1]).split('\\')[-1]).split('.')[0]
    return loaded_image, label


# Determine if input is link or path & return image
def get_image(which):
    """Decide if parameter is a link or directory, and load image from it.

    :param which: link or directory to where image is located
    :return: image pulled from link or directory
    """
    try:
        image = get_image_link(which)
        return image
    except:
        try:
            image, label = get_image_path(which)
            return image
        except:
            print('Load error. Try again')
