# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:48:21 2021

@author: 49117
"""
#from VideoPlayer import*
#from example import*

#if __name__ == '__main__':
#   videoplay()
#   main1()
import minemine
import threading
import time

#from VideoPlayer import*

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import QMainWindow, QTextEdit,QAction, QFileDialog, QApplication, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import QIcon

from readmytxt import* #读取txt文件


#from example import* #眼球追踪文件 含注释的example
from example_main import* #眼球追踪文件 不含注释的example_main

import os
import sys
sys.path.append(r'D:\\python file\\Vdero_test_together\\3.0')
from report_main import *



#20行到271行为视频播放器
'''视频播放器'''
class VideoPlayer(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(VideoPlayer, self).__init__(parent)
        # 初始化窗口
        self.setWindowTitle('视频播放器')
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'images/icon.png')))
        self.setGeometry(0, 45, 1920, 985)#窗口大小
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        palette = QPalette()  
        palette.setColor(QPalette.Background, Qt.white)
        self.setPalette(palette)
        # 定义组件
        # --视频播放插件
        self.video_widget = QVideoWidget(self)
        self.video_widget.setGeometry(QRect(5, 5, 800, 520))
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.black)
        self.video_widget.setPalette(palette)
        self.video_widget.setStyleSheet('background-color:#000000')
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.video_widget)
        self.player.setVolume(50)
        # --当前的视频路径
        self.video_line_edit = QLineEdit('')
        # --选择视频按钮
        self.select_video_btn = QPushButton('选择视频')
        
        # 添加按钮 生成学习报告
        self.select_video_btn2 = QPushButton('生成学习报告')
    
        
        # --播放按钮
        self.play_btn = QPushButton(self)
        self.play_btn.setIcon(QIcon(os.path.join(os.getcwd(), 'images/play.png')))
        self.play_btn.setIconSize(QSize(25, 25))
        self.play_btn.setStyleSheet('''QPushButton{border:none;}QPushButton:hover{border:none;border-radius:35px;}''')
        self.play_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_btn.setToolTip('播放')
        self.play_btn.setFlat(True)

        # --暂停按钮
        global flag_vedioplay
        flag_vedioplay = 0
        self.pause_btn = QPushButton('')
        self.pause_btn.setIcon(QIcon(os.path.join(os.getcwd(), 'images/pause.png')))
        self.pause_btn.setIconSize(QSize(25, 25))
        self.pause_btn.setStyleSheet('''QPushButton{border:none;}QPushButton:hover{border:none;}''')
        self.pause_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pause_btn.setToolTip('暂停')
        self.pause_btn.setFlat(True)
        self.pause_btn.hide()
        # --播放进度
        self.play_progress_label = QLabel('00:00 / 00: 00')
        self.play_progress_slider = QSlider(Qt.Horizontal, self)
        self.play_progress_slider.setMinimum(0)
        self.play_progress_slider.setSingleStep(1)
        self.play_progress_slider.setGeometry(QRect(0, 0, 200, 10))
        # --音量控制
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.mute_btn = QPushButton('')
        self.mute_btn.setIcon(QIcon(os.path.join(os.getcwd(), 'images/sound.png')))
        self.mute_btn.setIconSize(QSize(25, 25))
        self.mute_btn.setStyleSheet('''QPushButton{border:none;}QPushButton:hover{border:none;}''')
        self.mute_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mute_btn.setToolTip('禁音')
        self.mute_btn.setFlat(True)
        self.volume_label = QLabel('50')
        # --布局
        v_layout = QVBoxLayout()
        v_layout.setSpacing(0)
        v_layout.addStretch()
        h_layout = QHBoxLayout()

        h_layout.setSpacing(15)
        h_layout.addWidget(self.video_line_edit, 2, Qt.AlignVCenter | Qt.AlignVCenter)
        h_layout.addWidget(self.select_video_btn, 0, Qt.AlignCenter | Qt.AlignVCenter)
        
        #生成学习报告按钮
        h_layout.addWidget(self.select_video_btn2, 0, Qt.AlignCenter | Qt.AlignVCenter)
        
        v_layout.addLayout(h_layout)
        h_layout = QHBoxLayout()
        h_layout.setSpacing(2)
        h_layout.addWidget(self.play_btn, 0, Qt.AlignCenter | Qt.AlignVCenter)
        h_layout.addWidget(self.pause_btn, 0, Qt.AlignCenter | Qt.AlignVCenter)
        h_layout.addWidget(self.play_progress_label, 0, Qt.AlignCenter | Qt.AlignVCenter)
        h_layout.addWidget(self.play_progress_slider, 15, Qt.AlignVCenter | Qt.AlignVCenter)
        h_layout.addWidget(self.mute_btn, 0, Qt.AlignCenter | Qt.AlignVCenter)
        h_layout.addWidget(self.volume_slider, 0, Qt.AlignCenter | Qt.AlignVCenter)
        h_layout.addWidget(self.volume_label, 0, Qt.AlignCenter | Qt.AlignVCenter)
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)
        # 事件绑定
        self.player.durationChanged.connect(self.setVideoLength)
        self.player.positionChanged.connect(self.setPlayProgress)
        self.select_video_btn.clicked.connect(self.openvideo)
        self.select_video_btn2.clicked.connect(lambda:self.make_report('学习报告', msg))
        
        self.play_btn.clicked.connect(self.playvideo)
        self.pause_btn.clicked.connect(self.pausevideo)
        self.mute_btn.clicked.connect(self.mute)
        self.volume_slider.valueChanged.connect(self.setVolume)
        self.play_progress_slider.sliderPressed.connect(self.playProgressSliderPressed)
        self.play_progress_slider.sliderReleased.connect(self.playProgressSliderReleased)
    '''播放进度条按下ing事件'''
    def playProgressSliderPressed(self):
        if self.player.state() != 0: self.player.pause()
    '''播放进度条按下释放事件'''
    def playProgressSliderReleased(self):
        if self.player.state() != 0:
            self.player.setPosition(self.play_progress_slider.value())
            self.player.play()

    '''播放视频'''
    def playvideo(self):
        global flag_vedioplay
        flag_vedioplay = 1
        if self.player.duration() == 0: return
        self.play_btn.hide()
        self.pause_btn.show()
        self.player.play()
    '''暂停视频'''
    def pausevideo(self):
        global flag_vedioplay
        flag_vedioplay = 0
        if self.player.duration() == 0: return
        self.play_btn.show()
        self.pause_btn.hide()
        self.player.pause()
    '''禁音'''
    def mute(self):
        if self.player.isMuted():
            self.mute_btn.setIcon(QIcon(os.path.join(os.getcwd(), 'images/sound.png')))
            self.player.setMuted(False)
            self.volume_label.setText(str(self.v))
            self.volume_slider.setValue(self.v)
            self.player.setVolume(self.v)
        else:
            self.v=self.volume_slider.value()
            self.player.setMuted(True)
            self.volume_label.setText('0')
            self.volume_slider.setValue(0)
            self.mute_btn.setIcon(QIcon(os.path.join(os.getcwd(), 'images/mute.png')))
    '''打开视频文件'''
    def openvideo(self):
        # 打开并显示视频路径
        filepath = QFileDialog.getOpenFileName(self, '请选择视频', '.')

        #   Saliency_map() #此处加入显著性检测函数输出txt文件
        if filepath[0]: #当选择了视频
            self.video_line_edit.setText(filepath[0])
            print(filepath[0])
            desktop_path = r"D:\\python file\\Vdero_test_together\\3.0\\"  # 新创建的txt文件的存放路径
            full_path = desktop_path + 'myvediopath.txt'  # 也可以创建一个.doc的word文档
            file = open(full_path, 'w')
            file.write(filepath[0])
        # 将视频路径初始化进视频播放插件
        filepath = self.video_line_edit.text()
        if not os.path.exists(filepath): return
        fileurl = QUrl.fromLocalFile(filepath)
        if fileurl.isValid():
            self.player.setMedia(QMediaContent(fileurl))
            self.player.setVolume(50)
            
            '''打开txt文件''' 
    def showDialog1(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
            
    '''设置音量'''
    def setVolume(self):
        value = self.volume_slider.value()
        if value:
            self.player.setMuted(False)
            self.player.setVolume(value)
            self.volume_label.setText(str(value))
            self.volume_slider.setValue(value)
            self.mute_btn.setIcon(QIcon(os.path.join(os.getcwd(), 'images/sound.png')))
        else:
            self.player.setMuted(True)
            self.volume_label.setText('0')
            self.volume_slider.setValue(0)
            self.mute_btn.setIcon(QIcon(os.path.join(os.getcwd(), 'images/mute.png')))
    '''播放进度设置'''
    def setPlayProgress(self):
        #该函数1秒执行1次
        _, right = self.play_progress_label.text().split('/')
        position = self.player.position() + 1
        #输出视频播放时间
        global vediotime_now
        vediotime_now=position//1000
        print("当前视频播放到{}秒\n".format(vediotime_now))
        
        second = int(position / 1000 % 60)
        minute = int(position / 1000 / 60)
        left = str(minute).zfill(2) + ':' + str(second).zfill(2)
        self.play_progress_label.setText(left + ' /' + right)
        self.play_progress_slider.setValue(position)
        return vediotime_now
    '''视频时长显示更改'''
    def setVideoLength(self):
        global allvedio_len
        left, _ = self.play_progress_label.text().split('/')
        duration = self.player.duration()
        allvedio_len = duration // 1000
        self.play_progress_slider.setMaximum(duration)
        second = int(duration / 1000 % 60)
        minute = int(duration / 1000 / 60)
        right = str(minute).zfill(2) + ':' + str(second).zfill(2)
        self.play_progress_label.setText(left + '/ ' + right)
        
    '''关闭窗口'''
    def closeEvent(self, event):
        self.player.stop()
    '''生成报告函数'''
    def make_report(self, name, msg):
        #生成函数旧模板
        #desktop_path = ""  # 新创建的txt文件的存放路径
        #full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
        #file = open(full_path, 'w')
        #file.write(msg)   #msg也就是下面的Hello world!
        main_pic()
        main_cut()
        main_ocr2()
        minemine.realmain()


    '''改变窗口大小'''
    def resizeEvent(self, event):
        size = event.size()
        self.video_widget.setGeometry(5, 5, size.width() - 5, size.height() - 80)
        
    '''根据不同情况生成学习报告'''
def kind_of_study_report():
    if (True):
        msg="优秀"
    else:
        msg="不及格"
    return msg

def main():
    #视频播放
    global msg
    msg=kind_of_study_report()
    app = QApplication(sys.argv)
    client = VideoPlayer()
    client.show()
    sys.exit(app.exec_())
    
def videoplay():
    #视频播放
    global msg 
    global vediotime_now
    global client
    msg=kind_of_study_report()
    app = QApplication(sys.argv)
    client = VideoPlayer()
    client.show()
    sys.exit(app.exec_())
##到此↑↑↑↑↑以上是播放器代码

'''以下是读取txt文件代码'''

def loadDatadet(infile,k):
    f=open(infile,'r',encoding='UTF-8')
    #next(f) #跳过读取第一行
    sourceInLine=f.readlines()
    dataset=[]
    for line in sourceInLine:
        #print("{}\n".format(sourceInLine))
        #if(sourceInLine[0]=='#'):
            #continue
        temp1=line.strip('\n')
        temp2=temp1.split(' ')
        dataset.append(temp2)
    #循环结束后dataset形如[['4', '0'], ['12', '1'], ['60', '0'], ['71', '1']]

    for i in range(0,len(dataset)):     #len(dataset)等于数据行数
        for j in range(k):  #k等于数据列数
            #将float类型添加到string后面
            dataset[i].append(int(float(dataset[i][j])))
        del(dataset[i][0:k])    #删除前面string类数据
    #dataset形如[[4.0, 0.0], [12.0, 1.0], [60.0, 0.0], [71.0, 1.0]]
    return dataset  

def main_read():
    infile='D:\python file\Vdero_test_together\Salieney Map\information.txt'
    global k
    k=2     #2列数据
    global check_time
    global mytime
    global area
    check_time=loadDatadet(infile,k)
    print('检测时间结点和区域为',check_time)
    mytime=[]
    area=[]
    #txt文件处理time和area分别为检测时间和检测区域
    for i in range(0,len(check_time)):  #len(dataset)=数据行数=检测点个数
        mytime.append(check_time[i][0])   #每行来读入时间
        area.append(check_time[i][1])   #每列来读入区域
    print("检测时间为{}（单位秒）",format(mytime))
    print("检测区域为{}（0-5）",format(area))
    
'''以上是读取txt文件代码'''


'''以下是时间检测测试代码'''
def checking_time():
    global allvedio_len
    global vediotime_now
    global check_time
    global err_time
    global face
    global area_looking
    global client
    err_time=[]
    vediotime_now=0
    #time.sleep(5)
    while(True): 
        if(vediotime_now!=0): break #视频进度不为零才执行以下的代码
    #print("\n测试check_time{}".format(check_time))
    check_right=0
    check_wrong=0
    count_time=0
    while(True):
        time.sleep(1)
        #print(flag_vedioplay)
        if(vediotime_now==allvedio_len):
            print("视频播放完毕！")
            break

        #以下是未检测到人脸自动暂停功能
        if(face==None):
            count_time=count_time+1
        else:
            count_time=0
        if(count_time==5):#5秒未检测到人脸，视频暂停
            client.pausevideo()
            count_time = 0
        # 以上为未检测到人脸自动暂停功能


        if(flag_vedioplay == 1):    #flag_vedioplay == 1表示视频播放键按下
            if(vediotime_now in mytime):#时间监测点到达
                time_index=mytime.index(vediotime_now) #找其位序
                print("视线当前正在注视区域是：{}".format(area_looking))
                if (area_looking == 0):  # 未检测到眼球注视区
                    print("不执行检测")
                else:
                    if(area[time_index]==0):    #表示看哪都可以
                        check_right = check_right + 1
                        print("正确次数check_right为{}\n".format(check_right))
                    else: #表示area[time_index]！=0
                        if(area[time_index]==area_looking): #检测正确
                            print("检测结果正确")
                            check_right = check_right + 1
                            print("正确次数check_right为{}\n".format(check_right))
                        else:  #检测错误
                            check_wrong = check_wrong + 1
                            err_time.append(vediotime_now)
                            print("错误时间是：{}".format(err_time))
                            print("错误次数check_wrong为{}\n检测错误发生的时间是：第{}秒\n".format(check_wrong, vediotime_now))
                    # check_wrong = check_wrong + 1
                    # err_time.append(vediotime_now)
                    # print("错误时间是：{}".format(err_time))
                    # print("错误次数check_wrong为{}\n检测错误发生的时间是：第{}秒\n".format(check_wrong, vediotime_now))
    #由检测错误的时间产生err.txt文件
    f = open("D:\\python file\\Vdero_test_together\\3.0\\err2.txt", "w") #用来OCR的err.txt文件 err2.txt白写，用的是err
    for line in err_time:
        line=str(line)
        f.write(line + '\n')
    f.close()

    f = open("D:\\python file\\Vdero_test_together\\err2.txt", "w")  #同上的用来VB端的err.txt文件
    for line in err_time:
        line=str(line)
        f.write(line + '\n')
    f.close()

'''以上是时间检测测试代码'''

'''以下是一些功能测试的函数'''        
def test_send_para():
    ##以下测试传参：视频进度参数vediotime_now、txt文件参数mytime、area
    global vediotime_now
    global area
    global mytime
    time.sleep(10)
    print(mytime)
    print(area)
    for i in range(0,10):
        print("测试测试传递参数vediotime_now为{}".format(vediotime_now))
        time.sleep(1)

def myprint():
    global vediotime_now
    vediotime_now=0
    time.sleep(10)
    print("测试测试！输出1次视频当前播放时间:{}".format(vediotime_now))
    
'''以上是一些功能测试的函数'''

'''以下是一些眼球追踪模块example'''
import math
import cv2
from gaze_tracking import GazeTracking
from gaze_tracking.tracking import eye_tracking
import time
# 眼动追踪对象
gaze = GazeTracking()
# p_ref为参考值在手机成像的距离(pixel) d_ref为参考值与屏幕的距离(cm)
p_ref, d_ref = 81, 52

# 获取摄像头
webcam = cv2.VideoCapture(0)


def example_main0():
        global face
        global area_looking
        # 获取帧
        _, frame = webcam.read()

        # face表示是否有人脸存在，frame表示处理后的帧， area_looking 表示注视区域, distance表示人脸距离屏幕的距离
        face, frame, area_looking, distance = eye_tracking(gaze, frame, p_ref, d_ref)

        #全局变量赋值
        #print("test:{}".format(all_area_looking))
        #print("test:{}".format(all_face))


        # 显示图片
        cv2.putText(frame, str(area_looking), (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (0, 255, 0), 2)
        cv2.imshow("Demo", frame)
        # if cv2.waitKey(1) == 27:
        #     break
def example_main():
    while (True):
        example_main0()
        # time.sleep(1)  # 每一秒执行一次
        # print("当前注视区域是：{}".format(area_looking))
        # if (face == None):
        #     print("未检测到人脸")
        # else:
        #     print("有人脸")
        if cv2.waitKey(1) == 27:
            break
'''以上是一些眼球追踪模块example'''

'''以下是一些衔接眼球检测的数据'''
def test_eye_and_face():
    global face
    global area_looking
    global eye_time
    #global vediotime_now
    # global flag_vedioplay
    # if (flag_vedioplay == 1):  # flag_vedioplay == 1表示视频播放键按下
    while(True):
        time.sleep(1)
        #eye_time=eye_time+1
        print("当前注视区域是：{}".format(area_looking))
        print("眼球检测模块时间是：{}".format(eye_time))
        if(face==None):
          print("未检测到人脸")
        else:
           print("有人脸")


if __name__ == '__main__':
    #global vediotime_now #这两行不要也可以，记得两边声明global才能传参
    #vediotime_now = 0
    global area
    global mytime
    global face
    global area_looking
    
    t1 = threading.Thread(target=example_main, args=())    #眼球追踪 若是example则target=main1；若是example_main则example_main
    t2 = threading.Thread(target=videoplay, args=())    #播放器
    #t3 = threading.Thread(target=myprint, args=())  #测试播放器传参
    t4 = threading.Thread(target=main_read, args=())  #读入txt时间检测点
    #t5 = threading.Thread(target=test_send_para, args=())  #测试txt传参
    t6 = threading.Thread(target=checking_time, args=()) #时间检测函数
    #t7 = threading.Thread(target=test_eye_and_face, args=()) #眼球检测部分输出注释区与人脸检测
    
    t1.start() #眼球追踪开始
    t2.start()  #播放器开始
    #t3.start() #测试用     可删
    t4.start()  #读入txt文件用以检测时间
    #t5.start() #测试用     可删
    t6.start()  #时间检测比较开始
    #t7.start()  #眼球检测部分输出注释区与人脸检测

    

