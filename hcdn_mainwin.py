# -- coding: utf-8

import sys
import menubar
import tabCtl
import tkinter as tk


# print('start win: ')


def usr_login():
    pass


def usr_sign_up():
    pass


def main_win():
    mainWindow = tk.Tk()
    mainWindow.title('XXXX技术部 系统安装配置软件(win7测试版)')
    mainWindow.geometry('850x500')

    # user information
    # tk.Label(window, text='User name: ').place(x=50, y= 150)
    # tk.Label(window, text='Password: ').place(x=50, y= 190)

    # var_usr_name = tk.StringVar()
    # var_usr_name.set('example@python.com')
    # entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
    # entry_usr_name.place(x=160, y=150)
    # var_usr_pwd = tk.StringVar()
    # entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
    # entry_usr_pwd.place(x=160, y=190)

    # login and sign up button
    # btn_login = tk.Button(window, text='Login', command=usr_login)
    # btn_login.place(x=170, y=230)
    # btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
    # btn_sign_up.place(x=270, y=230)

    # 在`window`上创建一个`frame`
    frm = tk.Frame(mainWindow)
    frm.pack()

    tabCtl.createt_tab(mainWindow)

    menubar_ = menubar.create_menu(frm)

    mainWindow.config(menu=menubar_)

    mainWindow.mainloop()
