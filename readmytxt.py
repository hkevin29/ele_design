# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:40:41 2021

@author: 49117
"""

def loadDatadet(infile,k):
    f=open(infile,'r',encoding='UTF-8')
    next(f) #跳过读取第一行
    sourceInLine=f.readlines()
    dataset=[]
    for line in sourceInLine:
        #print("{}\n".format(sourceInLine))
        #if(sourceInLine[0]=='#'):
            #continue
        temp1=line.strip('\n')
        temp2=temp1.split('\t')
        dataset.append(temp2)
    #循环结束后dataset形如[['4', '0'], ['12', '1'], ['60', '0'], ['71', '1']]

    for i in range(0,len(dataset)):     #len(dataset)等于数据行数
        for j in range(k):  #k等于数据列数
            #将float类型添加到string后面
            dataset[i].append(int(dataset[i][j]))
        del(dataset[i][0:k])    #删除前面string类数据
    #dataset形如[[4.0, 0.0], [12.0, 1.0], [60.0, 0.0], [71.0, 1.0]]
    return dataset  

def main_read():
    infile='D:\python file\Vdero_test_together\check_time.txt'
    global k
    k=2     #2列数据
    global check_time
    check_time=loadDatadet(infile,k)
    print('检测时间结点和区域为',check_time)
    time=[]
    area=[]
    #txt文件处理time和area分别为检测时间和检测区域
    for i in range(0,len(check_time)):  #len(dataset)=数据行数=检测点个数
        time.append(check_time[i][0])   #每行来读入时间
        area.append(check_time[i][1])   #每列来读入区域
    print("检测时间为{}（单位秒）",format(time))
    print("检测区域为{}（0-5）",format(area))

    
if __name__ == '__main__':
    main_read()
    
