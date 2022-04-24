#! /usr/bin/env python
# -*- coding=utf-8 -*-
# author: lihua time:2021/6/2

import os
from timeit import default_timer as timer

# start, end, area, deadline_tim, biggest_area


# 将信息写入文本文件
def infor_write(number, fps, area, biggest_area):
    # 每帧都调用此函数
    # 判断每一帧的播放时间并暂存显著性区域
    # 当达到一秒时进行将出现次数最多的区域写入文件

    if (number % int(fps)) == 0:
        # 将时间信息和区域信息写入文件
        with open('information.txt', 'a+') as h:
            h.write(str(int(number/int(fps))) + ' ' + str(biggest_area.index(max(biggest_area))) + '\n')
        biggest_area = [0, 0, 0, 0]  # 重新开始统计
    else:
        if area == 0:
            biggest_area[0] += 1
        elif area == 1:
            biggest_area[1] += 1
        elif area == 2:
            biggest_area[2] += 1
        elif area == 3:
            biggest_area[3] += 1
        else:
            pass
    return biggest_area


if __name__ == '__main__':
    # 文件路径改为os.path.abspath('..') + '\\information.txt'
    i = 0
    start, area, deadline_tim = 1.3e-06, 2, 1
    biggest_area = [0, 0, 0, 0]  # 统计每个区域出现的次数, 分别为全局、左、中、右
    while i < 30:
        end = timer()
        deadline_tim, biggest_area = infor_write(start, end, area, deadline_tim, biggest_area)
        i += 1
