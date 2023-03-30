import cv2
#if your system does not recognise this module, please ensure you have pip, then run 'pip install opencv-python'

img = cv2.imread('pythonlog.png')

#given time one and time two
#assume the image has two borders on either side
#assume the space between the borders is evenly distributed along ten seconds
def croptime(img, one, two):

    #error returns
    if one >= two:
        print("Abort CropTime(): check first variable is lower than the second")
        return img
    if two > 10:
        print("Abort CropTime(): check second variable is less than 10")
        return img
    if one < 0:
        print("Abort CropTime(): check first variable is higher than 0")
        return img

    #for now, assuming borders (measured in pixels) are nill
    bStart = 0
    bEnd = 0
    h, w = img.shape[:2]
    neww = w - bStart - bEnd

    #use ratios to assume location of timestamps
    #find key to ratio
    ratiokey = neww/10
    #pixel of the start border plus the amount of pixels needed to get to the seconds mark
    three = bStart + one*ratiokey 
    #pixel of the start border plus the amount of pixels needed to get to the next seconds mark
    four = bStart + two*ratiokey

    #crop using found values
    cropwidth(img, three, four)


def resize(img, h, w):
    img = cv2.resize(img, (h,w))
    return img

def cropheight(img, one, two):
    h, w = img.shape[:2]
    img = img[one:two, 0:h]
    return img

def cropwidth(img, one, two):
    h, w = img.shape[:2]
    img = img[0:w, one:two]
    return img

def save(img):
    cv2.imwrite('copy.png', img)

def display(img):
    cv2.imshow('Displaying pl images', img)
    cv2.waitKey(0)
