from Preprocessing import bw
from load import determine
import process_manage
import testProcess


def menu():
    print('Choose operation')
    print('1. Preprocess image')
    print('2. Show success rate for dataset')
    print('3. Test Binariation')
    print('4. Test Morphology')
    print('5. Test Blurring')
    print('6. Quit')
    while True:
        try:
            sel = int(input())
            if 0 < sel < 7:
                return sel
            else:
                print('Please choose again')
        except ValueError:
            print('Please choose again')


if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == 1:
            print('Enter full path or link for image')
            print('* Default link : http://www.gov.kr/captcha')
            get_input = str(input())
            image = determine(get_input)
            sel_order = process_manage.choose_process()
            res = process_manage.process(image, sel_order)
            res.show()
        elif choice == 2:
            process_manage.show_rate()
        elif choice == 3:
            image = determine('http://www.gov.kr/captcha')
            testProcess.test_binarisation(image)
        elif choice == 4:
            image = determine('http://www.gov.kr/captcha')
            image = bw(image)
            testProcess.test_morphology(image)
        elif choice == 5:
            image = determine('http://www.gov.kr/captcha')
            image = bw(image)
            testProcess.test_blur(image)
        elif choice == 6:
            raise SystemExit
