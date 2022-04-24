'''
Function:
    视频播放器
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from PyQt5.QtWidgets import QMainWindow, QTextEdit,QAction, QFileDialog, QApplication, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import QIcon

#from readmytxt import*



'''视频播放器'''
class VideoPlayer(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(VideoPlayer, self).__init__(parent)
        # 初始化窗口
        self.setWindowTitle('视频播放器')
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'images/icon.png')))
        self.setGeometry(300, 50, 810, 600)#窗口大小
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
        if self.player.duration() == 0: return
        self.play_btn.hide()
        self.pause_btn.show()
        self.player.play()
    '''暂停视频'''
    def pausevideo(self):
        if self.player.duration() == 0: return
        self.play_btn.show()
        self.pause_btn.hide()
        self.player.pause()
    '''禁音'''
    def mute(self):
        if self.player.isMuted():
            self.mute_btn.setIcon(QIcon(os.path.join(os.getcwd(), 'images/sound.png')))
            self.player.setMuted(False)
            self.volume_label.setText('50')
            self.volume_slider.setValue(50)
            self.player.setVolume(50)
        else:
            self.player.setMuted(True)
            self.volume_label.setText('0')
            self.volume_slider.setValue(0)
            self.mute_btn.setIcon(QIcon(os.path.join(os.getcwd(), 'images/mute.png')))
    '''打开视频文件'''
    def openvideo(self):
        # 打开并显示视频路径
        filepath = QFileDialog.getOpenFileName(self, '请选择视频', '.')
        #global my_videopath
        #my_videopath=str(filepath[0]) #视频的路径变量
        #print(my_videopath) #测试用
        #print(type(my_videopath)) #测试用
        
        #   Saliency_map() #显著性检测函数输出txt文件
        if filepath[0]:
            self.video_line_edit.setText(filepath[0])
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
        
        #检测时间
        #检测时间
        #检测时间
        #检测时间
        #checking_time()
        #print("123")
        
        second = int(position / 1000 % 60)
        minute = int(position / 1000 / 60)
        left = str(minute).zfill(2) + ':' + str(second).zfill(2)
        self.play_progress_label.setText(left + ' /' + right)
        self.play_progress_slider.setValue(position)
        return vediotime_now
    '''视频时长显示更改'''
    def setVideoLength(self):
        left, _ = self.play_progress_label.text().split('/')
        duration = self.player.duration()
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
        desktop_path = ""  # 新创建的txt文件的存放路径
        full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
        file = open(full_path, 'w')
        file.write(msg)   #msg也就是下面的Hello world!
    # file.close()
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
    msg=kind_of_study_report()
    app = QApplication(sys.argv)
    client = VideoPlayer()
    client.show()
    sys.exit(app.exec_())
'''run'''
if __name__ == '__main__':
    msg=kind_of_study_report()
    main()
    