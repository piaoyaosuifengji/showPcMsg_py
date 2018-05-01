# -- coding: utf-8

import sys
import winreg
# import win32api  
# import win32con  
import tkinter
import os
import psutil


# http://docs.python.org/library/_winreg.html
# http://www.python.org/doc/2.6.2/library/_winreg.html


# keyname=r'Software\Microsoft\Internet Explorer\Main'
# page = 'www.sina.com.cn'  
# title = 'I love sina web site!'  
# search_page = 'http://www.baidu.com'  

# LONG RegOpenKeyEx(
#     HKEY hKey, // 需要打开的主键的名称
#     LPCTSTR lpSubKey, //需要打开的子键的名称
#     DWORD ulOptions, // 保留，设为0
#     REGSAM samDesired, // 安全访问标记，也就是权限
#     PHKEY phkResult // 得到的将要打开键的句柄
# ) 

# key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, keyname, 0, win32con.KEY_ALL_ACCESS)  
# win32api.RegSetValueEx(key, 'Start Page', 0, win32con.REG_SZ, page)  
# win32api.RegSetValueEx(key, 'Window Title', 0, win32con.REG_SZ, title)  
# win32api.RegSetValueEx(key, 'Search Page', 0, win32con.REG_SZ, search_page) 


class OpRegedit:

    def __init__(self):
        pass


    @classmethod
    def change_fireWall_set(clf,flag):
        #flag =1  开启防火墙
        # flag=0  关闭
        # print("key is",key)
        keyname=r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile"
        # HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders
        value_name="EnableFirewall"

        keyname2=r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile"
# HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\SharedAccess\Parameters\FirewallPolicy\PublicProfile
        if flag == 1:

            clf.set_LOCAL_MACHINE_REG_DWORD(keyname,value_name,1 )
            clf.set_LOCAL_MACHINE_REG_DWORD(keyname2,value_name,1 )
            # return key_value
        elif  flag == 0:
            clf.set_LOCAL_MACHINE_REG_DWORD(keyname,value_name,0 )
            clf.set_LOCAL_MACHINE_REG_DWORD(keyname2,value_name,0 )
            pass

    @classmethod
    def set_LOCAL_MACHINE_REG_DWORD(clf,keyname,value_name,value):
        key =winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,keyname, 0 ,winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, value_name,0, winreg.REG_DWORD, value)
        winreg.CloseKey(key)

    @classmethod
    def get_CURRENT_USER(clf,keyname,value_name):
        # key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, keyname, 0, win32con.KEY_ALL_ACCESS)  
        key =winreg.OpenKey(winreg.HKEY_CURRENT_USER,keyname, 0 ,winreg.KEY_ALL_ACCESS)
        # print("key is",key)
        key_value,key_kind=winreg.QueryValueEx(key,value_name)
        # win32api.RegQueryValue()
        # print(key_value,key_kind)
        winreg.CloseKey(key)
        return key_value
    @classmethod
    def set_CURRENT_USER(clf,keyname,value_name,value):
        # key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, keyname, 0, win32con.KEY_ALL_ACCESS)  

       
        key =winreg.OpenKey(winreg.HKEY_CURRENT_USER,keyname, 0 ,winreg.KEY_ALL_ACCESS)
        # print("key is",key)


        #Associates a value with a specified key.
        # winreg.SetValue(key,value_name,winreg.REG_SZ,value)

        #Stores data in the value field of an open registry key.
        winreg.SetValueEx(key, value_name,0, winreg.REG_SZ, value)
        # return key_value
        winreg.CloseKey(key)

    @classmethod
    def set_CURRENT_USER_desktop_dir(clf,value):
        keyname=r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        # HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders
        value_name="Desktop"
        return clf.set_CURRENT_USER(keyname,value_name,value )
    @classmethod
    def set_CURRENT_USER_Favorites_dir(clf,value):
        keyname=r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        value_name="Favorites"
        return clf.set_CURRENT_USER(keyname,value_name,value )
    @classmethod
    def set_CURRENT_USER_download_dir(clf,value):
        keyname=r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        value_name="{374DE290-123F-4565-9164-39C4925E467B}"
                    #  {374DE290-123F-4565-9164-39C4925E467B}
        return clf.set_CURRENT_USER(keyname,value_name,value )
    @classmethod
    def set_CURRENT_USER_Personal_dir(clf,value):
        keyname=r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        value_name="Personal"
        return clf.set_CURRENT_USER(keyname,value_name,value )


    @classmethod
    def get_CURRENT_USER_desktop_dir(clf):
        keyname=r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        value_name="Desktop"
        return clf.get_CURRENT_USER(keyname,value_name)
    @classmethod
    def get_CURRENT_USER_Favorites_dir(clf):
        keyname=r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        value_name="Favorites"
        return clf.get_CURRENT_USER(keyname,value_name)
    @classmethod
    def get_CURRENT_USER_download_dir(clf):
        keyname=r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        value_name="{374DE290-123F-4565-9164-39C4925E467B}"
        return clf.get_CURRENT_USER(keyname,value_name)
    @classmethod
    def get_CURRENT_USER_Personal_dir(clf):
        keyname=r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        value_name="Personal"
        return clf.get_CURRENT_USER(keyname,value_name)



