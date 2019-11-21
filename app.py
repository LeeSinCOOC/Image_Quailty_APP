import cv2 as cv


def change(imagepath,savepath):
    image = cv.imread(imagepath)
    img = cv.imwrite(savepath,image,[int(cv.IMWRITE_JPEG_QUALITY),95])

def change_dir(src,dir):
    image