# Overview
## Introduction
### Captcha
- Completely Automated Public Turing test to tell Computers and Humans Apart
- A type of _challenge - response_ test used to determine whether the user is a human or a robot.
- Although many non-text based captchas are being developed, due to familarity, text-based captchas are most prominently used.
- Text based captchas 
![image](https://cdn-images-1.medium.com/max/771/1*aqxLRBdzFavMMw6wpoRXsg.png)

### Captcha model
- captcha database pulled from [http://www.gov.kr/captcha](http://www.gov.kr/captcha)

![http://www.gov.kr/captcha](http://www.gov.kr/captcha)
- 3 Security Features
    1. Noisy background (Anti-Recognition)
    2. Occluding Line (Anti-Recognition)
    3. Character Overlapping (Anti-Segmentation)

### OpenCV
- [Open Source Computer Vision Library](https://opencv.org/)
- Designed for real-time applications to efficient computation, providing a common infrastructure for computer vision applications and accelerating the use of machine perception in the commercial products.


## Functions
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/01%20Functions.png)
### 1. Preprocess image
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/02-1%20Preprocess%20image.png)
- Can read an image from local directoy by entering full path, or download an image from a link by entering a url
- If the path or link is wrong, it will download an image from the default link

![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/02-2%20Choose%20order.png)
- There are 4 preprocessing steps you can choose from
- Enter steps you wish to include in your processing, in wanted order
![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/02-3%20Preprocess%20Result.png)
- The images after each step, including the original image, will show up, as well as the text read from tesseract
### 2. Show success rate for dataset
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/03-2%20Success%20Rate.png)
- You must provide a full dataset to verify the accuracy of preprocessing. This means the dataset must include images in .png format, and their titles must be the target label of self
- The current path in which the program is running is given, in case your dataset is in the same directory.
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/03-1%20Choose%20path.png)
- After entering your dataset, you can choose which steps you want to take.
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/03-3%20Rate%20Result.png)
- If your label contains multiple letters, the former accuracy indicates the ratio of correct letters to total letters.
- If you're concerned with actual accuracy, the later indicates the ratio of correctly recognized captcha texts.

### 3. Test Binarisation
![1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/04-1%20Binarisation.png)
- The result of testing binarisation is shown immediately with a random image.
- The result will show 4 images, including the original image that was processed.
- 'simple binary 125' is the result of using simple thresholding with the threshold vlue of 125. 'simple binary' is the result of simple thresholding, but with the threshold value chosen from the image. 'adaptive' is the result of using adaptive thresholding.

### 4. Test Morphology
![2.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/05-1%20Morhpology.png)
- The result of testing morphology is shown immediately with a random image.
- The result will show 4 images, including the original image that was processed.
- 'dilation' is the result of dilation, in which the area of white pixels increase. 'erosion' is the result of erosion, in which the area of black pixels increase. 'closed' is the result of closing, in which images are processed with dilation and then erosion in that order.

### 5. Test Blurring
![3.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/06-1%20Blurring.png)
- The result of testing blurring is shown immediately with a random image.
- The result will show 4 images, including the original image that was processed.
- Each image is processed with the filter given in the description

### 6. Quit
- End operation

# Implementation
## Preprocessing - Binarisation
### 1. 기본 임계처리 (Simple Thresholding)
    
``cv2.threshold(src, thresh, maxval, type) -> retva, dst``
- **src** : input image -> GrayScale 이미지어야 함(Single-Channel image)
- **thresh** : 임계값
- **maxval** : 임계값을 넘었을 때 적용할 값 (Binary Thresholding 에 이용)
    - grayscale value = 255 -> white
- **type** : Thresholding type
    - cv2.THRESH_BINARY
        - thresh를 넘으면 maxval로 전환 :` if src(x, y) > thresh then dst(x, y) = maxval` else dst(x, y) = 0
    - cv2.THRESH_BINARY_INV
    - cv2.THRESH_TRUNC
        - thresh를 넘으면 thresh로 전환 :` if src(x, y) > thresh then dst(x, y) = thresh` else dst(x, y) = src(s, y)
        - maxvalue 필요 없음
    - cv2.THRESH_TOZERO
    - cv2.THRESH_TOZERO_INV
- **retval** : thresh 값으로 사용한 값
- **dst** : output image
     
### 2. 적응 임계처리 (Adaptive Thresholding)
``cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)``
- **adaptiveMethod** : thresholding value 값을 정하는 방법
    - cv2.ADAPTIVE_THRESH_MEAN_C : 주변영역(block size)의 평균값으로 결정
    - cv2.ADAPTIVE_THRESH_GAUSSIAN_C : 주변역역의 합(정규 분포에 따라 weight가 달라짐)
- **blockSize** : thresholding를 적용할 이미지 영역 사이즈
- **C** : 변수

### 3. Otsu의 이진화
- thresh 값을 정하는 방법
- Bimodial image은 히스토그램으로 표현했을 때 peak가 2개 있는 이미지를 뜻하는데, 그 두개의 peak의 중간값을 대략적인 thresh 값으로 설적하여 이진화를 진행하다.
- thresh 값으로는 0을 전달하며, retval에는 otsu의 알고리즘으로 계산한 값이 리턴된다.
- Optimization 가능

### 4. 시험 적용
- 이미지의 배경과 숫자를 분리하기 위해 사용 (Grayscale image를 받아 처리)
1. 기본 임계 처리 + Binary + 임계값 = 125
2. 기본 임계 처리 + Binary + 임계값 임의 설정
    - CAPTCHA 이미지의 (0, 0) pixel값은 숫자가 아닌 부분 중 가장 어두운 부분이므로 이를 임계값으로 설정하면 숫자와 배경을 분리할 수 있다.
3. 적응 임계 처리 + Gaussian
    ```python
    def bw_test(image):
        # Simple Thresholding + Binary(Threshold = 125)
        thresh, binary = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)
        # Simple Thresholding + Binary(Threshold = value of left bottom pixel)
        t = image[image.shape[0]-1, image.shape[1]-1]
        thresh, binary_thresh = cv2.threshold(image, t, 255, cv2.THRESH_BINARY)
        # Adaptive Thresholding + Gaussian + Binary
        gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

        titles = ['original', 'simple binary 125', 'simple binary', 'adaptive']
        images = [image, binary, binary_thresh, gaussian]
        for i in range(4):
            plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
    ```
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/07-1%20Test%20Binarisation.png)

### 5. 적용
```python
def bw(image):
    t1 = image[0][0]
    t2 = image[0][image.shape[1]-1]
    t3 = image[image.shape[0]-1][0]
    t4 = image[image.shape[0]-1][image.shape[1]-1]
    t = min(t1, t2, t3, t4)
    if t == 255:
        bw_img = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 15, 2)
    else:
        thresh, bw_img = cv2.threshold(image, t, 255, cv2.THRESH_BINARY)
    return bw_img
```
- 임계값을 (0, 0) 픽셀값이 아닌 네 꼭짓점의 픽셀 값 중 최소값으로 지정한다.
    -> 그라디에이션의 방향이 달라져도 이진화 가능
- 최소값이 255일 경우 이미지 미처리
    -> 배경색이 하얀색일 경우 적응임계처리를 이용하여 적당한 임계값을 선택하도록 한다.
    
## Preprocessing - Cropping
```python
def crop_image(image):
    cut = 5     # Boundary of image that is definitely not text
    x_list, y_list = [], []
    corners = cv2.goodFeaturesToTrack(image, 200, 0.01, 6)
    corners = np.int0(corners)
    for i in corners:
        x, y = i.ravel()
        if x>cut and y>cut:
            x_list.append(x)
            y_list.append(y)
    xl = min(x_list)
    xr = max(x_list)
    yt = min(y_list)
    yb = max(y_list)

    return image[yt:yb, xl:xr]
```
- Corner들에 맞게 Cropping 은 되지만 가로선에 영향을 많이 받음

![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/08-1%20Cropp.png)
![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/08-2%20Cropp.png)
- Closing을 한 후 Cropping을 할 경우

![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/08-3%20Cropp.png)
![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/08-4%20Cropp.png)

-> 더 적합해 보임
    
## Preprocessing - Closing
### 1. Morphology - Erosion & Dilation
- **Morphological image processing**: Collection of non-linear operations related to the shape or morphology of features in an image.
- A` structuring element s` is positioned at all possible locations in the `input image f`
  -> It is compared with the corresponding neighbourhood of pixels
  -> Test whether the element "fits", "hits" or "intersects" the neighbourhood
![image](https://www.cs.auckland.ac.nz/courses/compsci773s1c/lectures/ImageProcessing-html/morph-probing.gif)

- **Erosion**: removes small-scale details from a binary image
    `for all pixel in image, if s fits f then 1 else 0`
    
![image](https://www.cs.auckland.ac.nz/courses/compsci773s1c/lectures/ImageProcessing-html/mor-pri-erosion.gif)
- **Dilation**: adds a layer of pixels to both the inner and outer boundaries of regions
    `for all pixel in image, if s hits f then 1 else 0`
    
![image](https://www.cs.auckland.ac.nz/courses/compsci773s1c/lectures/ImageProcessing-html/mor-pri-dilation.gif)
- **Opening**:Erosion followed by Dilation
    -> Open up a gap between objects connected by a thin line. Any regions that have survived the erosion are restored to their original size by the dilation:
- **Closing**: Dilation followed by Erosion
    -> Fill holes in the regions while keeping the initial region sizes
- 결론: 현재 우리의 이미지는 하얀 바탕에 검은 글씨이므로 <span style="color:#e11d21">Captcha Image Closing</span> 필요
- 쟁점
    - Structuring Element를 어떤 모양으로 해야할까
    - Structuring Element의 크기를 어떻게 정해야 할까
    -> _**Kernel을 어떻게 결정할까**_
    > these operations can filter out from an image any details that are smaller in size than the structuring element, e.g. opening is filtering the binary image at a scale defined by the size of the structuring element. **Only those portions of the image that fit the structuring element are passed by the filter**; smaller structures are blocked and excluded from the output image. The size of the structuring element is most important to eliminate noisy details but not to damage objects of interest.
    -> 얇은선(가로선)보다 크고 굵은선(숫자)보다는 작은 크기의 kernel
  출처: [Morphological Image Processing](https://www.cs.auckland.ac.nz/courses/compsci773s1c/lectures/ImageProcessing-html/topic4.htm)


### 2. Erosion & Dilation
- `cv2.erode(src, kernel, dst, anchor, iterations, borderType, borderValue)`
- `cv2.dilation(src, kernel, dst, anchor, iterations, borderType, borderValue)`
1. src: source image
2. kernel: structuring element
    - `cv2.getStructuringElemet()`로 생성 가능
    - `kernel = np.ones((3,3),np.uint8)`의 간단한 kernel을 생성하여 결과 이미지를 확인 해 볼 수 있음
3. anchor: kernel의 중심 (default: (-1. -1))
4. iterations: 적용 횟수

Original | Dilation | Erosion
:---: | :---: | :---:
![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/09-1%20original.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/09-2%20dilated.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/09-3%20eroded.png)

-> Kernel (Structureing Element)를 적절하게 선택해야 함

### 3. Morphology
- `cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst`
1. op –Morphological operation의 종류
    - MORPH_OPEN - an opening operation
    - <span style="color:#e11d21">MORPH_CLOSE - a closing operation</span>
    - MORPH_GRADIENT - a morphological gradient. Dilation과 erosion의 차이.
    - MORPH_TOPHAT - “top hat”. Opeining과 원본 이미지의 차이
    - MORPH_BLACKHAT - “black hat”. Closing과 원본 이미지의 차이
2. borderType – Pixel extrapolation method
3. borderValue – Border value in case of a constant border
4. Kernel shape
    - MORPH_RET : 사각형 모양
    - MORPH_ELLIPSE : 타원형 모양
    - MORPH_CROSS : 십자 모양

### 4. 적용
```python
def test_morphology(image, kernel_size):
    show_image('', image)
    for n in range(3):
        if n == 0:
            shape = cv2.MORPH_RECT
        elif n == 1:
            shape = cv2.MORPH_ELLIPSE
        elif n == 2:
            shape = cv2.MORPH_CROSS

        kernel = cv2.getStructuringElement(shape, kernel_size)
        show_image('', cv2.dilate(image, kernel, iterations=1))
        show_image('', cv2.erode(image, kernel, iterations=1))
        show_image('', cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel))
```
_with kernel_size = (3, 3)_

| Kernel shape | Original | Dilation | Erosion | Closing | Text |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 사각형 | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-1.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-2.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-3.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-4.png) | 220728 |
| 타원형 | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-5.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-6.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-7.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-8.png) | 220738 |
| 십자형 | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-9.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-10.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-11.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-12.png) | 220738 |

_with kernel_size = (4, 4)_

| Kernel shape | Original | Dilation | Erosion | Closing | Text |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 사각형 | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-13.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-14.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-15.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-16.png) | 754811 |
| 타원형 | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-17.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-18.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-19.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-20.png) | 754811 |
| 십자형 | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-21.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-22.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-23.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-24.png) | 754811 |

_with kernel_size = (2, 4)_
-> 사각형 Kernel에만 적용
-> 세로선보다 가로선은 지우는 것에 초점을 두었기 때문

| 회차 | Original | Dilation | Erosion | Closing | Text|
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-25.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-26.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-27.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-28.png) | 819252 |
| 2 | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-29.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-30.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-31.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-32.png) | 542332 |
| 3 | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-33.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-34.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-35.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/10-36.png) | 112496 |

## Preprocessing - Blurring
- Used to reomove noise
- [OpenCV Smoothing](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html)
### 1. Averaging
`blur = cv2.blur(img,(5,5))`
### 2. Gaussian Filtering
`blur = cv2.GaussianBlur(img,(5,5),0)`
### 3. Median Filtering
`median = cv2.medianBlur(img,5)`
- Effective in removing salt-and-pepper noise
### 4. Bilateral Filtering
`blur = cv2.bilateralFilter(img,9,75,75)`
- Remove noise while preserved edges

| Original | Averaging | Gaussian Filtering | Median Filtering | Bilateral Filtering |
| :---: | :---: | :---: | :---: | :---: |
| ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-01.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-02.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-03.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-04.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-05.png) |
| ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-6.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-07.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-08.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-09.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-10.png) |
| ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-11.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-12.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-13.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-14.png) | ![image.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/11-15.png) |



# Code Structure
![CodeStructure](https://goo.gl/fZK7Je)
# Success Rate Analysis
## Test cases
- Page Segmentation Mode에 따라
    A. psm - 7 (Treat the image as a single text line)
    B. psm - 6 (Assume a single uniform block of text)

- Preprocessing 단계 종류 및 순서에 따라
    1. Binarisation -> Cropping -> Closing -> Blurring
    2. Binarisation -> Closing -> Cropping -> Blurring
    3. Binarisation -> Cropping -> Closing
    4. Binarisation -> Closing -> Cropping
    5. Binarisation -> Closing

|  | Processing Example |
| --- | :---: |
| 1 | ![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/12-1.png) |
| 2 | ![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/12-2.png) |
| 3 | ![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/12-3.png) |
| 4 | ![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/12-4.png) |
| 5 | ![Figure_1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/12-5.png) |

## Result
| Letter Accuracy / Text Accuracy | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | 78.83 / 63.67 | 79.28% / 63.67% | 84.00% / 66.00% | 85.17% / 72.67% | 75.44% / 58.33% |
| **B** | 79.00% / 60.00% | 80.00% / 63.67% | 84.00% / 66.00% | 85.17% / 72.67% | 75.61% / 58.67% |

## Analysis
- 한 줄의 텍스트로 이미지를 인식하는 psm-7에 비해 하나의 텍스트 블럭으로 인식하는 psm-6 옵션을 사용했을 때 거의 모든 경우에 살짜 더 높거나 같은 인식률을 보였다. 많게는 1.8% 정도까지의 글자 인식률 상승을 볼 수 있다.
- 다양한 조합으로 image preprocessing을 해본 결과, Binarisation, Closing, Cropping 순으로 진행할 때 가장 높은 인식률을 보였다. Binarisation, Closing 순으로 진행한 5번이 모든 경우 중 가장 인식률이 저조한 것으로 보아 Cropping은 큰 역할을 했다고 볼 수 있다.
- 1,2번 과정과 3, 4번 과정을 비교해보았을 때, Blurring의 단게가 추가되면 오히려 인식률이 감소하는 것을 볼 수 있다. Blurring의 경우 image noise를 제거하기 위해 추가시킨 단계로서, 현재 사용하는 captcha image와 같이 제거해야 할 noise가 없는 이미지에서는 오히려 경계선을 흐리게 만들어 인식을 어렵게 하고 있다.

    | With Blurring| Accuracy | Without Blurring | Accuracy | 
    | --- | --- | --- | --- |
    | Binarisation -> Cropping -> Closing -> Blurring | 79.00% / 60.00% | Binarisation -> Cropping -> Closing |  84.00% / 66.00% |
    | Binarisation -> Closing -> Cropping -> Blurring | 80.00% / 63.67% | Binarisation -> Closing -> Cropping |85.17% / 72.67%  |
- 1, 3번 과정과 2, 4번 과정을 비교하면, 같은 단계를 거치더라도 그 순서에 따라 인식률에 차이가 있음을 확인할 수 있다. 특히, Cropping 후 Closing을 하는 것보다, Closing 단계를 거친 후에 Cropping을 하는 것이 더 정확한다. 애초에 Cropping을 하는 이유가 Tesseract에게 text가 있는 부분만 인식하도록 하기 위해서이기 때문에, Occluding line을 제거해주는 Closing 단계를 거친 후 남은 부분을 잘라내는 것이 맞는 순서가 되겠다.
    
    | Crop -> Close | Accuracy | Close -> Crop | Accuracy |
    | --- | --- | --- | --- |
    | Binarisation -> Cropping -> Closing -> Blurring | 79.00% / 60.00% | Binarisation -> Closing -> Cropping -> Blurring | 80.00% / 63.67% |
    | Binarisation -> Cropping -> Closing | 84.00% / 66.00% | Binarisation -> Closing -> Cropping | 85.17% / 72.67% |

### 한계
- 주어진 captcha image을 기준으로 preprocessing을 진행하였기 때문에, 최대한 모든 경우를 생각하고 자동화를 시키려고 했지만 다른 image에 적용시키는 데에는 한계가 존재할 수 밖에 없다.
- 다른 captcha image를 처리한 결과

![1.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/13-1.png)
![3.png](https://github.com/alstjgg/captcha_image_preprocess/blob/master/doc_image/13-2.png)

# 추가 - argparse
## argparse
### 1. parser 만들기
### `parser = argparse.ArgumentParser()`
- prog=None
    - sys.argv[0]
    - 프로그램의 이름
- usage=None
    - 프로그램의 사용 방법 (어떤 인자를 전달할 것인가에 대한 옵션 등)
- description=None
    - 프로그램에 대한 간략한 설명
    - 옵션 위에 표시됨
- epilog=None
    - 프로그램에 대한 추가 설명
    - 옵션 뒤에 표시됨
- parents=[]
    - 다른 파서와 인자 공유
- formatter_class=argparse.HelpFormatter
    - class argparse.RawDescriptionHelpFormatter -> 줄바꿈이나 인덴트가 이상해도 그대로 출력
    - class argparse.RawTextHelpFormatter
    - class argparse.ArgumentDefaultsHelpFormatter -> 인자 정보 중 default 값에 대한 정보도 함께 출력
    - class argparse.MetavarTypeHelpFormatter -> 인자 설명 대한 정보 대신 type 정보를 출력
- prefix_chars='-'
    - '-'와 같이 명령 옵션의 접두어로 사용할 문자 설정
- fromfile_prefix_chars=None
- argument_default=None
- conflict_handler='error'
- add_help=True
    - `-h`나 `--h`를 사용하여 옵션을 출력할때, `-h`, `--help` 옵션은 출력되지 않음
- allow_abbrev=True

### 2. 인자 추가하기
### `parser.add_argument()`
- name or flags
    - 선택 인자인지, 위치 인자인지 결정
    - `-f`의 경우 선택 인자, `bar`의 경우 위치 인자 -> 접두사 `-`로 구별
- action
    - `store` -> 인자 값 저장
        - `store_const` -> `const` 인자에 인자 값 저장
        - `store_true`, `store_false` -> 주어진 인자에 `True` 또는 `False` 저장
    - `append`
        - 인자 값을 리스트에 추가 -> 옵션을 여러번 지정할 수 있음
        - `append_const`
    - `count`
        - 키워드 인자의 수를 세림 -> 상세도 증가
    - `help` -> 자동 추가
    - `version`
        - `add_argument`에서 지정된 `version=` 값을 출력
- nargs -> 소비되어야 하는 명령행 인자의 수
    - `N` -> 정수 리스트
    - `?`
    - `*` -> 모든 명령행 인자를 리스트에 저장
    - `+`
    - `argparse.REMAINDER` -> 남은 명령행 인자를 리스트에 저장
- const
    - `store_const`와 `append_const` action을 사용할 때 무조건 사용
- default -> 인자가 명령행에 없는 경우 생성되는 값
    - `argparse.SUPPRESS`의 경우 인자가 없으면 값 추가 안함
- type
    - 기본으로 `str`
    - `int`, `float`, `open`, 또는 직접 만든 형으로 변환 가능
- choices -> 값이 허용된 선택지 내인지 검사 (`typ`과 일치해야함)
- required -> 필수인 옵션 표시(`=True`)
- help - 인자가 하는 일에 대한 간단한 설명
- metavar -> 사용 메시지에 사용되는 인자의 이름 변경
- dest -> 인자를 어디에 저장할지 선택

### 3. 기타 유용한 기능
### `ArgumentParser.add_subparsers()`
-> 특정 명령에 대한 부속 명령
### `ArgumentParser.add_argument_group()`
-> 'optional arguments'와 'positional arguments' 외에 더 적절한 인자 그룹이 있는 경우 생성

### 4. 인자 파싱하기
### `args = parser.parse_args()`
- 인자 없이 호출 -> sys.argv에서 자동으로 인자 결정

***
## CaptchaBreaker 프로그램에 맞는 인자 선택
### 1. Operation -> positional
1. Preprocess image
2. Show success rate for dataset
3. Test Binarisation
4. Test Morphology
5. Test Blurring
### 2. Path/Link -> optional
- Path to data or link to image
### 3. Processing Order -> optional
1. Binarisation
2. Cropping
3. Closing
4. Blurring

## 적용
- main source code for applying argparse
```python
import argparse

parser = argparse.ArgumentParser(description='Preprocess Captcha images',
                                formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('option', type=int, choices=range(1, 6),
                    help=option_help)
parser.add_argument('--path', dest='path', default='http://www.gov.kr/captcha',
                    help=path_help + '\n(default: %(default)s)')
parser.add_argument('--order', dest='order', default='1234',
                    help=order_help + '\n(default: %(default)s)')

args = parser.parse_args()
```
- 실행 화면

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

