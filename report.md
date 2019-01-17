# Captcha Breaker - Breaking captcha with image preprocessing
_첨부파일: CaptchaBreak, requirements.txt, dataset(images)_
# Overview
## Introduction
## Captcha model


# Implementation
```uml
Main --|> ManageProcessing
Main --|> TestProcess
```

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
| 1 | ![Figure_1.png](/files/2393443817327490649) |
| 2 | ![Figure_1.png](/files/2393444067160455901) |
| 3 | ![Figure_1.png](/files/2393458252611345665) |
| 4 | ![Figure_1.png](/files/2393458533140251734) |
| 5 | ![Figure_1.png](/files/2393458791123155122) |

## Result
|  | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | 78.83 / 63.67 | 79.28% / 63.67% | 84.00% / 66.00% | 85.17% / 72.67% | 75.44% / 58.33% |
| **B** | 79.00% / 60.00% | 80.00% / 63.67% | 84.00% / 66.00% | 85.17% / 72.67% | 75.61% / 58.67% |

## Analysis
