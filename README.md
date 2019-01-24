# Image Preprocessing and Breaking Captcha
Break simple captcha with image preprocessing using openCV on python with tesseract
- Test various preprocessing procedures
- Recognize text via tesseract
- Compute accuracy of text recognition on given dataset

[Interactive version](#interactive-version)

[Command line version](#command-line-version)

# Interactive Version
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/01%20Functions.png)
## 1. Preprocess image
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/02-1%20Preprocess%20image.png)
- Can read an image from local directoy by entering full path, or download an image from a link by entering a url
- If the path or link is wrong, it will download an image from the default link

![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/02-2%20Choose%20order.png)
- There are 4 preprocessing steps you can choose from
- Enter steps you wish to include in your processing, in wanted order
![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/02-3%20Preprocess%20Result.png)
- The images after each step, including the original image, will show up, as well as the text read from tesseract
## 2. Show success rate for dataset
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/03-2%20Success%20Rate.png)
- You must provide a full dataset to verify the accuracy of preprocessing. This means the dataset must include images in .png format, and their titles must be the target label of self
- The current path in which the program is running is given, in case your dataset is in the same directory.
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/03-1%20Choose%20path.png)
- After entering your dataset, you can choose which steps you want to take.
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/03-3%20Rate%20Result.png)
- If your label contains multiple letters, the former accuracy indicates the ratio of correct letters to total letters.
- If you're concerned with actual accuracy, the later indicates the ratio of correctly recognized captcha texts.

## 3. Test Binarisation
![1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/04-1%20Binarisation.png)
- The result of testing binarisation is shown immediately with a random image.
- The result will show 4 images, including the original image that was processed.
- 'simple binary 125' is the result of using simple thresholding with the threshold vlue of 125. 'simple binary' is the result of simple thresholding, but with the threshold value chosen from the image. 'adaptive' is the result of using adaptive thresholding.

## 4. Test Morphology
![2.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/05-1%20Morhpology.png)
- The result of testing morphology is shown immediately with a random image.
- The result will show 4 images, including the original image that was processed.
- 'dilation' is the result of dilation, in which the area of white pixels increase. 'erosion' is the result of erosion, in which the area of black pixels increase. 'closed' is the result of closing, in which images are processed with dilation and then erosion in that order.

## 5. Test Blurring
![3.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/06-1%20Blurring.png)
- The result of testing blurring is shown immediately with a random image.
- The result will show 4 images, including the original image that was processed.
- Each image is processed with the filter given in the description

## 6. Quit
- End operation

# Command Line Version
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/14-1.png)
- operation must be chosen (1, 2, 3, 4, 5)
- path and order are optional arguments -> default is given
    - for operation 2(computing success rate), path to dataset must be given
### Examples
- `python CaptchaBreaker.py 1` : operation 1 with no optional arguments
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/14-2.png)

    -> Process random image from default link in default processing order(binarise -> crop -> close -> blur)
- `python CaptchaBreaker.py 1 --order 132` : operation 1 with order arugment
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/14-3.png)

    -> Process random image from default link in given processing order(binarise -> close -> crop)
- `python Captchabreaker.py 2 --path \Users\argos\PycharmProjects\CaptchaBreak\images --order 123` : operation 2 with path and order arguments
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/14-4.png)

    -> Process images given in dataset by path in given processing order(binarse -> crop -> close), and print recognition success rate
- `python Captchabreaker.py 3 --path \Users\argos\PycharmProjects\CaptchaBreak\images\003369.png` : operation 3 with path argument
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/14-5.png)

    -> Test binarisation on given image
### Other examples
- `python CaptchaBreaker.py 2` : operation 2 without path to dataset
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/14-6.png)

    -> error due to empty dataset
- `python CaptchaBreaker.py 4 --order 13483` : operation 4 with order argument
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/14-7.png)

    -> no error. the program will operate successfully while ignoring the order argument

