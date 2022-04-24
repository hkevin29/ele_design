#剪切图片
# coding: utf-8
from PIL import Image
import os
import os.path
import numpy as np
import cv2
#指明被遍历的文件夹
def cut(rootdir,save_path,err):
    i=0
    for parent, dirnames, filenames in os.walk(rootdir):#遍历每一张图片
        for filename in filenames:
            print('parent is :' + parent)
            print('filename is :' + filename)
            currentPath = os.path.join(parent, filename)
            print('the fulll name of the file is :' + currentPath)
    
            img = Image.open(currentPath)
            a,b=img.size
            print (img.format, img.size, img.mode)
            #img.show()
            i=i+1
            ii=str(i)

            box1 = (0, 0, 0.6*a, 0.1*b)#设置左、上、右、下的像素
            image1 = img.crop(box1) # 图像裁剪
            image1.save(save_path+'\\'+filename) #存储裁剪得到的图像

def main_cut():
    rootdir = r'D:\python file\Vdero_test_together\3.0\\11'      #图片来源的路径
    save_path =r"D:\python file\Vdero_test_together\3.0\\11_1"        #保存图片的目录
    infile='D:\python file\Vdero_test_together\\3.0\\err.txt'

    with open(infile, 'r') as f:    #读入出错的编号
        g=f.read()
        gg0=g.splitlines()
    gg1 = map(eval, gg0)
    err=[]
    for i in gg1:
        err.append(i)
       
    cut(rootdir,save_path,err)


    
if __name__ == '__main__':
    main_cut()