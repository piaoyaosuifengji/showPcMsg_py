# -- coding: utf-8

import sys
import winreg
# import Access-Control
import win32api  
import win32con  
import tkinter
import os
import psutil
# import hcdn_mainwin *-*
from hcdn_mainwin import *
# win32api.MessageBox(win32con.NULL, 'Python 你好！', '你好', win32con.MB_OK) 
import time







 



#获取系统时间，如果超过固定时间就退出

# timeStr=time.strftime('%Y-%m',time.localtime(time.time()))
# print(timeStr)
ys=time.strftime('%Y',time.localtime(time.time()))
ms=time.strftime('%m',time.localtime(time.time()))


# print(timeStr)
# ys,ms=time.localtime(time.time())

ysD=int(ys)
msD=int(ms)
# print(ysD)
# print(msD)
if ysD >2018 or msD > 6:
    sys.exit(0)
else:
    pass

main_win()