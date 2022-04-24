
from picture1 import *
from cut import *
from ocr2 import *
import shutil
'D:\\python file\\Vdero_test_together\\3.0\\11\\'
shutil.rmtree('D:\\python file\\Vdero_test_together\\3.0\\11\\')
os.mkdir('D:\\python file\\Vdero_test_together\\3.0\\11\\')
shutil.rmtree('D:\\python file\\Vdero_test_together\\3.0\\11_1\\')
os.mkdir('D:\\python file\\Vdero_test_together\\3.0\\11_1\\')

if __name__ == '__main__':
    main_pic()
    main_cut()
    main_ocr2()

