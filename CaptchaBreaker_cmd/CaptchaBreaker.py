from load import get_image
from Preprocessing import bw
import process_manage
import testProcess
import argparse


def menu(args):
    if args.option == 1:
        res = process_manage.process(get_image(args.path), args.order)
        res.show()
    elif args.option == 2:
        process_manage.show_rate(args.path, args.order)
    elif args.option == 3:
        testProcess.test_binarisation(get_image(args.path))
    elif args.option == 4:
        image = bw(get_image(args.path))
        testProcess.test_morphology(image)
    elif args.option == 5:
        image = bw(get_image(args.path))
        testProcess.test_blur(image)


# help descriptions
option_help = 'Choose operation' \
              '\n1. Preprocess image' \
              '\n2. Show success rate for dataset' \
              '\n3. Test binarisation' \
              '\n4. Test morphology' \
              '\n5. Test blurring'

path_help = 'Path to data or link to image'
order_help = 'Choose order of processing' \
             '\n1. Binarisation' \
             '\n2. Cropping' \
             '\n3. Closing' \
             '\n4. Blurring'

# parser
parser = argparse.ArgumentParser(description='Preprocess Captcha images',
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('option', type=int,
                    choices=range(1, 6), help=option_help)
parser.add_argument('--path', dest='path',
                    default='http://www.gov.kr/captcha',
                    help=path_help + '\n(default: %(default)s)')
parser.add_argument('--order', dest='order', default='1234',
                    help=order_help + '\n(default: %(default)s)')

args = parser.parse_args()
menu(args)
