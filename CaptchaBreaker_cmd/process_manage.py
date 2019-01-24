import numpy as np
from matplotlib import pyplot as plt
import fnmatch, os, glob
import Preprocessing
from load import get_image_path


class Result:
    def __init__(self, order, images, text):
        """Store processing order, images, and text recognized by tesseract.

        :param order: list of preprocessing functions in processed order
        :param images: list of images in processed order
        :param text: text recognized by tesseract
        """
        self.order = order
        self.images = images
        self.text = text

    def show(self):
        """Show processing steps with titles and images in order.

        :return: none
        """
        titles = ['Original']
        images = [self.images[0]]
        for i in range(4):
            if self.order[i] == Preprocessing.bw:
                titles.append('Binarise')
                images.append(self.images[i+1])
            elif self.order[i] == Preprocessing.crop_image:
                titles.append('Crop')
                images.append(self.images[i+1])
            elif self.order[i] == Preprocessing.morph_image:
                titles.append('Close')
                images.append(self.images[i+1])
            elif self.order[i] == Preprocessing.blur_image:
                titles.append('Blur')
                images.append(self.images[i+1])
            elif self.order[i] == Preprocessing.return_image:
                continue
        titles.append('Text')
        empty = np.zeros((images[-1].shape[0], images[-1].shape[1], 3), np.uint8)
        empty[:] = (255, 255, 255)
        images.append(empty)

        for i in range(len(titles)):
            plt.subplot(1, len(titles), i + 1), plt.imshow(images[i], 'gray')
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        ax = plt.gca()
        plt.text(0.5, 0.5, self.text, horizontalalignment='center',
                 verticalalignment='center', transform=ax.transAxes,
                 fontsize=13)
        plt.show()


def get_order(sel_order):
    """Return list of processing functions in given order.

    :param sel_order: order of processing in string of integers
    :return: list of processing functions
    """
    steps = [Preprocessing.bw, Preprocessing.crop_image,
             Preprocessing.morph_image, Preprocessing.blur_image]
    order = []
    for i in range(4):
        try:
            order.append(steps[int(sel_order[i]) - 1])
        except:
            order.append(Preprocessing.return_image)
    return order


# define preprocessing (종류와 순서 결정)
def process(original_image, sel_order):
    """Create Result class with original image and processing order.

    :param original_image: original image before any processing
    :param sel_order: string of integers indicating processing order
    :return: Result class
    """
    order = get_order(sel_order)
    images = [original_image]
    images.append(order[0](original_image))
    images.append(order[1](images[1]))
    images.append(order[2](images[2]))
    images.append(order[3](images[3]))
    text = Preprocessing.tesseract(images[4])
    return Result(order, images, text)


# Compute and display success rate for images in given path
def show_rate(path, sel_order):
    """Show success rate of text recognition of given dataset and process order

    :param path: local directory to dataset(image + label)
    :param sel_order: string of integers indicating processing order
    :return: none
    """
    try:
        total = len(fnmatch.filter(os.listdir(path), '*.png'))
    except:
        print('Path error. Try again.')
        raise SystemExit

    order = get_order(sel_order)
    count = letter_correct = correct = 0
    for f in glob.glob(path + '/*.png'):
        count += 1
        original_image, label = get_image_path(f)
        try:
            processed_image = process(original_image, order)

            if processed_image.text == label:
                correct += 1
            for i in range(min(len(processed_image.text), len(label))):
                if processed_image.text[i] == label[i]:
                    letter_correct += 1
        except:
            print('Error occurred in processing image ', label)

        print('\r{0: .2f}% complete..'.format((count*100) / total), end='')

    print('')
    print('Out of {0} letters {1} were correctly read.'
          'Success Rate: {2:.2f}%'
          .format(total*6, letter_correct, (letter_correct * 100) / (total*6)))
    print('Out of {0} captcha images, {1} were correctly read.'
          'Success Rate: {2:.2f}%'
          .format(total, correct, (correct * 100) / total))
