# -*- coding: utf-8 -*-  
import sys
import io
import os
import psutil
import uuid
import winreg
# import win32api  
# import win32con  
# reload(sys)
# sys.setdefaultencoding('utf8')
def get_CURRENT_USER(keyname,value_name):
    # key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, keyname, 0, win32con.KEY_ALL_ACCESS)  
    key =winreg.OpenKey(winreg.HKEY_CURRENT_USER,keyname, 0 ,winreg.KEY_ALL_ACCESS)
    print("key is",key)
    key_value,key_kind=winreg.QueryValueEx(key,value_name)
    # win32api.RegQueryValue()
    print(key_value,key_kind)


keyname=r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
value_name="Desktop"
value_name="Desktop"
print(keyname," * ",value_name)
get_CURRENT_USER(keyname,value_name)                   