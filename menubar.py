# -- coding: utf-8

# from hcdn_mainwin import mainWindow
import tkinter as tk  #import A as B,给予A库一个B的别称，帮助记忆
                    # 如 from A import b,相当于
                    # import A
                    # b=A.b
count  = 0
tmpWin =1

def do_job():
    pass
# def key(event):
#     print("pressed",repr(event.char))

def window_show_my_msg_callback1(me):
    global count
    count  = count-1
    print(count)

def window_show_my_msg_callback(me):
    global count
    # count = 0
    # tmpWin.n
    # print("me=", type(me))   #me= <class 'tkinter.Event'>

    # print("位于屏幕", me.x_root, me.y_root)
    # print("位于窗口", me.x, me.y)
    # print("位于窗口", me.num)
    print(count)
    # print(me)  #传入的是事件的信息



def show_my_msg():
    global count
    if count == 1:
        pass
    else:      
        window_show_my_msg=tk.Toplevel()
        window_show_my_msg.geometry('450x300')
        window_show_my_msg.title('关于')
        xx =10
        yy = 10
        w=15
        h=12
        i =0
        j =0
        pad = 5
        
        var1=tk.StringVar()
        # l1=tk.Label(window_show_my_msg,textvariable=var1,font=('Arial',12),width=w,height=h,bg='green') # 
        l1=tk.Label(window_show_my_msg,textvariable=var1,font=('Arial',12)  ) # 
        var1.set(" ")
        l1.grid(row=i ,padx=pad,pady=pad,sticky=tk.W)
        # l1.grid(row=i,sticky=tk.NW )
        i=i+1
        j=j+1

        var1=tk.StringVar()
        # l1=tk.Label(window_show_my_msg,textvariable=var1,font=('Arial',12),width=w,height=h,bg='green') # 
        l1=tk.Label(window_show_my_msg,textvariable=var1,font=('Arial',12)  ) # 
        var1.set(" ")
        l1.grid(row=i ,padx=pad,pady=pad,sticky=tk.W)
        # l1.grid(row=i,sticky=tk.NW )
        i=i+1
        j=j+1
        
        var1=tk.StringVar()
        # l1=tk.Label(window_show_my_msg,textvariable=var1,font=('Arial',12),width=w,height=h,bg='green') # 
        l1=tk.Label(window_show_my_msg,textvariable=var1,font=('Arial',12) ) # 
        var1.set("软件作者：XXXX")
        l1.grid(row=i ,padx=pad,pady=pad,sticky=tk.W)
        # l1.grid(row=i,sticky=tk.NW )
        i=i+1
        j=j+1

        var2=tk.StringVar()
        var2.set("单位：XXXX")
        l2=tk.Label(window_show_my_msg,textvariable=var2 ,font=('Arial',12) )
        l2.grid(row=i ,padx=pad,pady=pad,sticky=tk.W)
        i=i+1
        j=j+1

        var3=tk.StringVar()
        var3.set("QQ:994371870")
        l3=tk.Label(window_show_my_msg,textvariable=var3 ,font=('Arial',12) )
        l3.grid(row=i ,padx=pad,pady=pad,sticky=tk.W)
        i=i+1
        j=j+1

        var4=tk.StringVar()
        var4.set("电话:XXXX")
        l4=tk.Label(window_show_my_msg,textvariable=var4 ,font=('Arial',12) )
        l4.grid(row=i ,padx=pad,pady=pad,sticky=tk.W)
        i=i+1
        j=j+1

        var4=tk.StringVar()
        var4.set("软件开发时间：18/03")
        l4=tk.Label(window_show_my_msg,textvariable=var4 ,font=('Arial',12) )
        l4.grid(row=i ,padx=pad,pady=pad,sticky=tk.W)
        i=i+1
        j=j+1
        # window_show_my_msg.bind("<Button-1>", window_show_my_msg_callback)
        window_show_my_msg.bind("<Destroy>", window_show_my_msg_callback1)
        # window_show_my_msg.wait_window()
        count = count +1
        print(count)
        # tmpWin = window_show_my_msg
    # return 1
    

def create_menu(win):
    ##创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
    menubar = tk.Menu(win)
    # menubar.place(x=50, y= 150)

    ##定义一个空菜单单元
    filemenu = tk.Menu(menubar, tearoff=0)
    # filemenu.place(x=2,y=2)

    ##将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='File', menu=filemenu)


    ##在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
    ##如果点击这些单元, 就会触发`do_job`的功能
    filemenu.add_command(label='New', command=do_job)
    filemenu.add_command(label='Open', command=do_job)##同样的在`File`中加入`Open`小菜单
    filemenu.add_command(label='Save', command=do_job)##同样的在`File`中加入`Save`小菜单
    filemenu.add_command(label='关于', command=show_my_msg) 

    filemenu.add_separator()##这里就是一条分割线

    ##同样的在`File`中加入`Exit`小菜单,此处对应命令为`mainWindow.quit`
    filemenu.add_command(label='Exit', command=win.quit)
    return menubar