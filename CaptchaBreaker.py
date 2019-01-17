from Preprocessing import bw
from load import gather
import process_manage
import testProcess


def menu():
    print('Choose operation')
    print('1. Show how images are processed')
    print('2. Show success rate for dataset')
    print('3. Test Binariation')
    print('4. Test Morphology')
    print('5. Test Blurring')
    print('6. Quit')
    sel = int(input())
    while True:
        if 0 < sel < 7:
            return sel
        else:
            print('Please choose again')
            sel = int(input())


if __name__ == '__main__':
    while True:
        choice = menu()
        image = gather('http://www.gov.kr/captcha')
        if choice == 1:
            sel_order = process_manage.choose_process()
            res = process_manage.process(image, sel_order)
            res.show()
        elif choice == 2:
            process_manage.show_rate()
        elif choice == 3:
            testProcess.test_binarisation(image)
        elif choice == 4:
            image = bw(image)
            testProcess.test_morphology(image)
        elif choice == 5:
            image = bw(image)
            testProcess.test_blur(image)
        elif choice == 6:
            raise SystemExit
