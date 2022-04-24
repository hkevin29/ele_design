#coding=utf-8 
import os
import cv2
def save_img2(video_path,f_save_path,err,length):  #提取视频中图片 按照每秒提取   间隔是视频帧率
    vc = cv2.VideoCapture(video_path) #读入视频文件
    fps = vc.get(cv2.CAP_PROP_FPS)   #获取帧率
    print(fps)    #帧率可能不是整数  需要取整
    rval=vc.isOpened()      #判断视频是否打开  返回True或Flase
    print(rval)
    c = 1
    while rval:  # 循环读取视频帧
        rval, frame = vc.read()  # videoCapture.read() 函数，第一个返回值为是否成功获取视频帧，第二个返回值为返回的视频帧：
        pic_path = "11" + '/'
        if length==0:
            rval=0
        if rval:
            #gg存储低级秒
            gg1=c % round(fps)#确保为整数秒
            gg2=c//round(fps)#当前输出在第几秒

            if (gg1 == 0):  # 每隔fps帧进行存储操作  ,可自行指定间隔
                if gg2 in err:
                    cv2.imwrite(f_save_path + str(gg2) + '.jpg', frame)  # 存储为图像,保存名为 
                    print("picture yes")
                    length=length-1
                    

            cv2.waitKey(1)  # waitKey()--这个函数是在一个给定的时间内(单位ms)等待用户按键触发;如果用户没有按下 键,则接续等待(循环)
            c = c + 1
        else:
            break       
    vc.release()
    print('save_success' )

def main_pic():
    txtpath = "D:\python file\Vdero_test_together\\3.0\myvediopath.txt"
    with open(txtpath, 'r') as f:
        video_path=f.read()
    #video_path = r'D:\python file\Vdero_test_together\3.0\\kys.mp4'    #视频所在的路径
    f_save_path = 'D:\\python file\\Vdero_test_together\\3.0\\11\\'        #保存图片帧的目录
    infile='D:\\python file\\Vdero_test_together\\3.0\\err.txt'

    #读取出错的编号
    with open(infile, 'r') as f:
        g=f.read()
        gg0=g.splitlines()
    gg1 = map(eval, gg0)
    err=[]
    for i in gg1:
        err.append(i)
    length=len(err)
    save_img2(video_path,f_save_path,err,length)

if __name__ == '__main__':
    main_pic()
