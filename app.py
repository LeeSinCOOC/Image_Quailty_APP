import os
import argparse
import cv2 as cv

parser = argparse.ArgumentParser(description='python app.py --srcImage 0.jpg --dirImage 1.jpg\n'+
                                           'python app.py --srcPath --dirPath')
parser.add_argument('-s','--srcImage',default='images/0.jpg')
parser.add_argument('-d','--dirImage',default='finnaly/0.jpg')
parser.add_argument('-sp','--srcPath')
parser.add_argument('-dp','--dirPath')

args = parser.parse_args()

def change(imagepath,savepath):
    image = cv.imread(imagepath)
    img = cv.imwrite(savepath,image,[int(cv.IMWRITE_JPEG_QUALITY),80])
    print('Done')

def change_dir(src,dir):
    src_list = os.listdir(src)
    for i in src_list:
        if i.endswith('jpg'):
            path_0 = os.path.join(src,i)
            path_1 = os.path.join(dir,i)
            change(path_0,path_1)
        else:
            pass

if not args.srcPath:
    change(args.srcImage,args.dirImage)
else:
    change_dir(args.srcPath,args.dirPath)

