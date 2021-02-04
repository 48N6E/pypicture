import os
from PIL import Image


class imgs:
    def __init__(self):
        self.addr = os.path.abspath('')+'\\img\\'
        self.im = Image.open(os.path.abspath('')+'\\img\\'+'2017111390333098.jpg')


    def imageDetail(self):
        detail = {}
        detail['图像的格式'] = self.im.format
        detail['图像的大小'] = self.im.size
        detail['图像的宽度'] = self.im.width
        detail['图像的高度'] = self.im.height
        print(detail)
        return detail

    def createColorBlock(self):
        im = Image.new('RGB', (100, 100), 'red')
        # 保存这个图像
        im.save(os.path.abspath('')+'\\img\\'+'red.png')

    def mixedImage(self):
        # 打开im1
        im1 = Image.open(os.path.abspath('')+'\\img\\'+'2017111390333098.jpg').convert(mode='RGB')
        # 创建一个和im1大小一样的图像
        im2 = Image.new('RGB', im1.size, 'red')
        # 混合图片，并显示
        Image.blend(im1, im2, 0.5).show()

    def pixelMixed(self):
        # 定义一个方法
        def func(x):
            return x * 2
        # 对图像im每个像素点进行func中的操作，其中func不能加()
        Image.eval(self.im, lambda x: x * 2).show()
        return Image.eval(self.im, func)