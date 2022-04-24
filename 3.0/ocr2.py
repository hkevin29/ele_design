from os import error
import os
import os.path
import sys
import json
import base64

IS_PY3 = sys.version_info.major == 3
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus  # 防止https证书校验不正确
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
API_KEY = 'XUggii4BIiDsxMgMoFES6VsR'
SECRET_KEY = 'YpOqRhD0zqzW5z3mvylpxPCQ2jDAS0co'
OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'
"""
    获取token
"""


def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    if (IS_PY3):
        result_str = result_str.decode()
    result = json.loads(result_str)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print('please overwrite the correct API_KEY and SECRET_KEY')
        exit()


"""
    读取文件
"""


def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()


"""
    调用远程服务
"""


def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)


def main_ocr2():
    resulttxt = "result2.txt"
    rootdir = r'D:\\python file\\Vdero_test_together\\3.0\\11_1'
    infile = 'D:\\python file\\Vdero_test_together\\3.0\\err.txt'

    teacher_report_path = r'D:\\python file\\Vdero_test_together\\3.0\\11'


    # 读取出错的编号
    with open(infile, 'r') as f:
        g = f.read()
        gg0 = g.splitlines()
    gg1 = map(eval, gg0)
    err = []
    for i in gg1:
        err.append(i)

    textlist = []
    for parent, dirnames, filenames in os.walk(rootdir):  # 遍历每一张图片
        picturenumber = len(filenames)  # 图片数量
        filepath = parent  # 文件路径
        filenames
        print("定位")
        print(filenames)

        for filename in err:
            currentPath = os.path.join(parent, str(filename) + ".jpg")
            print("文件为:" + currentPath)

            token = fetch_token()
            # 拼接通用文字识别高精度url
            image_url = OCR_URL + "?access_token=" + token
            text = ""
            # try:
            file_content = read_file(currentPath)
            # 调用文字识别服务
            result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))
            # 解析返回结果
            result_json = json.loads(result)
            if 'words_result' in result_json:
                # print("yes")
                for words_result in result_json["words_result"]:
                    text = text + words_result["words"]
                if text not in textlist:
                    textlist.append(text)
                    print(textlist)
                else:
                    print("OCR调用成功，列表已存在")
            else:
                print("第一次调用OCR失败")
                print("正在进行第二次OCR的调用")
                result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))
                # 解析返回结果
                result_json = json.loads(result)
                if 'words_result' in result_json:
                    print("第二次调用成功")
                    for words_result in result_json["words_result"]:
                        text = text + words_result["words"]
                    if text not in textlist:
                        textlist.append(text)
                        print(textlist)
                    else:
                        print("OCR调用成功，列表已存在")
                else:
                    print("第二次调用OCR失败")
                    print("正在进行第三次OCR的调用")
                    result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))
                    # 解析返回结果
                    result_json = json.loads(result)
                    if 'words_result' in result_json:
                        print("第三次调用成功")
                        for words_result in result_json["words_result"]:
                            text = text + words_result["words"]
                        if text not in textlist:
                            textlist.append(text)
                            print(textlist)
                        else:
                            print("OCR调用成功，列表已存在")
                    else:
                        print("第三次调用OCR失败")
                        print("正在进行第四次OCR的调用")
                        if 'words_result' in result_json:
                            print("第四次调用成功")
                            for words_result in result_json["words_result"]:
                                text = text + words_result["words"]
                            if text not in textlist:
                                textlist.append(text)
                                print(textlist)
                            else:
                                print("OCR调用成功，列表已存在")
                        else:
                            print("第四次调用OCR失败")
                            print("正在进行第五次OCR的调用")
                            if 'words_result' in result_json:
                                print("第五次调用成功")
                                for words_result in result_json["words_result"]:
                                    text = text + words_result["words"]
                                if text not in textlist:
                                    textlist.append(text)
                                    print(textlist)
                                else:
                                    print("OCR调用成功，列表已存在")
                            else:
                                print("第五次调用OCR失败")
                                print("以上调用OCR失败")


            # except:
            # pass

    with open(resulttxt, 'w+', encoding='utf-8') as f:
        print(picturenumber, file=f)
        print(teacher_report_path, file=f) #修改为cut之前的图片的路径
        for line in textlist:
            f.writelines(line + '\n')
        f.writelines(" ")
    print("OCR调用完成!")

if __name__ == '__main__':
    main_ocr2()