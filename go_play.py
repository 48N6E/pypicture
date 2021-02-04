import os
from PIL import Image
from classes import img

def pathAddr():
    addr = os.path.abspath('')+'\\img'
    return addr

def imageRead():
    image = Image.open(pathAddr()+'\\2017111390333098.jpg')
    image.show()

def imagedetail():
    image = Image

if __name__ == '__main__':
    pathAddr()
    #imageRead()
    text = img.imgs()
    text.imageDetail()
    #text.createColorBlock()
    #text.mixedImage()
    text.pixelMixed()

