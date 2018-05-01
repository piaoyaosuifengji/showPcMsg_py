# -- coding: utf-8

import tkinter as tk
from tkinter import ttk
import socket
import os
import psutil
import platform
# import commands
import uuid
import winreg
# from Tkinter import *
# import win32ui
import wx
import myDirDialog
import opRegedit
import netconfg

#在目录tab中修改一些默认的目录地址，需要保存分区信息
#Python的元组与列表类似，不同之处在于元组的元素不能修改。

saveDirList=[]
dirEnList=[]

class DiskMsg:
    diskMsgTotalCapacity = {}
    diskMsgRemainingCapacity = {}
    def __init__(self):
        pass
    def addNewDisk(self,diskName,totalCapacity,remainingCapacity):
        DiskMsg.diskMsgTotalCapacity[diskName] = totalCapacity
        DiskMsg.diskMsgRemainingCapacity[diskName] = remainingCapacity
    @classmethod   
    def getDiskMsgById(cls,id):
        if id == 0:
            pass
        elif id == 1:
            pass
        elif id == 2:
            pass   
        else:
            pass  

    @classmethod    
    def getDiskNum(cls):
        len1 =len( cls.diskMsgTotalCapacity)
        len2 =len( cls.diskMsgRemainingCapacity)
        if len1 == len2:
            return len1
        else:
            return 0
    @classmethod     
    def printDiskMsg(cls):
        pass
        # for key,value in DiskMsg.diskMsgTotalCapacity.items():
            # print("lable:",key," Total："，value," remaining：",DiskMsg.diskMsgRemainingCapacity[key])
            # print("lable:",key," Total：",value," remaining：",cls.diskMsgRemainingCapacity[key])

# enteryLen = 250
def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n
def createt_tab(win):

    # l = tk.Label(win,text='OMG! this is TK!',bg='green',font=('Arial', 12), width=15, height=2)
    # l.pack()
    tabControl = ttk.Notebook(win)  # Create Tab Control

    tab1 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text='系统信息')  # Add the tab
    tab_msg_create(tab1)

    tabControl.pack(expand=1, fill="both")  # Pack to make visible

    tab2 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab2, text='目录')  # Make second tab visible
    tab_DirectoryManagement_create(tab2)
    # tabControl.get
    # tab3 = ttk.Frame(tabControl)  # Add a second tab
    # tabControl.add(tab3, text='ping')  # Make second tab visible
    # tab_ping_create(tab3)
    tab3 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab3, text='网络')  # Make second tab visible
    # tab_DirectoryManagement_create(tab3)
    netcong_var=netconfg.netconfg(tab3)

def tab_DirectoryManagement_create(tabCtlFrame):
    i = 0
    j = 0
    pad = 3   
    # DiskMsg.printDiskMsg()
    diskCount = DiskMsg.getDiskNum()
    showItem = {
        0: '盘符',
        1: '总容量',
        2: '剩余容量',
    }
    showItem2 = {
        0: '目录对象',
        1: '当前目录',
        2: '新目录',
    }   
    changDir = {
        0: '文档',
        1: '桌面',
        2: '收藏夹',
        3: '下载',
    }    
    itemToShow = len(showItem)
    for i in range(0, itemToShow):
        var1 = tk.StringVar()
        l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
        var1.set(showItem[i])
        l1.grid(row=0,column =i, padx=pad, pady=pad, sticky=tk.W)
    # for i in range(0, diskCount):
    #     for j in range(0, 3):
    #         var11 = tk.StringVar()
    #         l11 = tk.Label(tabCtlFrame, textvariable=var11, font=('Arial', 12))
    #         var11.set(showItem[i])
    #         l11.grid(row=(i+1),column =j, padx=pad, pady=pad, sticky=tk.W)
    i =0
    curRow=0
    for key,value in DiskMsg.diskMsgTotalCapacity.items():
        # print("lable:",key," Total：",value," remaining：",DiskMsg.diskMsgRemainingCapacity[key])
        j=0
        var11 = tk.StringVar()
        l11 = tk.Label(tabCtlFrame, textvariable=var11, font=('Arial', 12))
        var11.set(key)
        l11.grid(row=(i+1),column =j, padx=pad, pady=pad, sticky=tk.W)
        j=j+1

        var12 = tk.StringVar()
        l12 = tk.Label(tabCtlFrame, textvariable=var12, font=('Arial', 12))
        var12.set(value)
        l12.grid(row=(i+1),column =j, padx=pad, pady=pad, sticky=tk.W)
        j=j+1

        var13 = tk.StringVar()
        l13 = tk.Label(tabCtlFrame, textvariable=var13, font=('Arial', 12))
        var13.set(DiskMsg.diskMsgRemainingCapacity[key])
        l13.grid(row=(i+1),column =j, padx=pad, pady=pad, sticky=tk.W)
        j=j+1

        i=i+1
        curRow=i
    #开始显示当前默认目录位置
    j=0
    # for key,value in DiskMsg.diskMsgTotalCapacity.items():
    itemToShow = len(showItem2)
    # itemToShow = len(changDir)
    curRow = i+1
    # print(curRow)
    for i in range(0, itemToShow):
        var1 = tk.StringVar()
        l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
        var1.set(showItem2[i])
        l1.grid(row=curRow,column =i, padx=pad, pady=pad, sticky=tk.W)

    itemToShow = len(changDir)
    curRow = curRow+1
    enteryLen = 80
    padxForDirE=10
    for i in range(0, itemToShow):
        j=0
        var1 = tk.StringVar()
        l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
        var1.set(changDir[i])
        l1.grid(row=curRow,column =j, padx=pad, pady=pad, sticky=tk.W)
        j=j+1
        oldDir=""
        newDir=""
        if  i ==0 :
            oldDir=opRegedit.OpRegedit.get_CURRENT_USER_Personal_dir()
            newDir="f:\\我的文档"
            dirsave=myDirDialog.RegeditSaveDir(changDir[i],newDir,"Personal")
            saveDirList.append(dirsave)
        elif i ==1: 
            oldDir=opRegedit.OpRegedit.get_CURRENT_USER_desktop_dir()
            newDir="f:\\我的桌面"
            dirsave=myDirDialog.RegeditSaveDir(changDir[i],newDir,"Desktop")
            saveDirList.append(dirsave)
        elif i ==2:
            oldDir=opRegedit.OpRegedit.get_CURRENT_USER_Favorites_dir()
            newDir="f:\\收藏夹"
            dirsave=myDirDialog.RegeditSaveDir(changDir[i],newDir,"Favorites")
            saveDirList.append(dirsave)
        elif i ==3:
            oldDir=opRegedit.OpRegedit.get_CURRENT_USER_download_dir()
            newDir="f:\\我的下载"
            dirsave=myDirDialog.RegeditSaveDir(changDir[i],newDir,"{374DE290-123F-4565-9164-39C4925E467B}")
            saveDirList.append(dirsave)

        e = tk.Entry(tabCtlFrame )
        e.grid(row=curRow,column =j , padx=padxForDirE, pady=pad,ipadx = enteryLen, sticky=tk.W)
        e.insert("end",oldDir)#从注册表中读取数据
        j=j+1
        
        e = tk.Entry(tabCtlFrame )
        e.grid(row=curRow,column =j , padx=padxForDirE, pady=pad,ipadx = enteryLen, sticky=tk.W)
        e.insert("end",newDir)
        # e.bind()
        dirEnList.append(e)        
        j=j+1

        # if



        curRow = curRow+1

    
    b = tk.Button(tabCtlFrame, 
        text='一键全部修改',      # 显示在按钮上的文字
        width=15, height=2, 
        command=changDirs)     # 点击按钮式执行的命令
    # b.grid(row=curRow,column =3 , padx=pad, pady=pad  )
    # b.height
    b.grid(row=curRow,column =3 , ipadx=0, ipady=0 , sticky=tk.NSEW )
    

def changDirs():
    '''
    每做一步都要检查一遍

    '''
    listLen=len(saveDirList )
    if listLen != len(dirEnList):
        return

    #因为没有Entry widget的单独文本改变的事件处理函数，所以这里进行统一处理
    for i in range(0, listLen):
        if saveDirList[i].get_newDir()  ==  dirEnList[i].get() :
            pass
        else:
            # dirEnList[i].delete(0,len(dirEnList[i].get()))
            # dirEnList[i].insert("end",newDir)
            dirEnList[i].select_range(0, len(dirEnList[i].get()) )
            saveDirList[i].setNewDir(dirEnList[i].get())
    # print("listLen=",listLen)
    for i in range(0, listLen):
        #1 打开reg
        #2 测试目录是否已经存在
        #3 如果不存在就创建目录

        isExists=os.path.exists(saveDirList[i].get_newDir())
        newidr=saveDirList[i].get_newDir()
        print("newidr:",newidr)
        # saveDirList[i].printDir()
        chRegFlag=0
        if not isExists:
            isok=myDirDialog.mkdir(newidr)
            isok = True
            if isok == True:
                chRegFlag=1
        else:
            # print("未完全全部内容")
            chRegFlag=1
            # continue
        if chRegFlag == 1:
            # get_regeditKey
            print("time to ch reg:")
            if  saveDirList[i].get_regeditKey() ==  "Personal" :
                opRegedit.OpRegedit.set_CURRENT_USER_Personal_dir(newidr)
            elif saveDirList[i].get_regeditKey() ==  "Desktop" :
                opRegedit.OpRegedit.set_CURRENT_USER_desktop_dir(newidr)
            elif saveDirList[i].get_regeditKey() ==  "Favorites" :
                    opRegedit.OpRegedit.set_CURRENT_USER_Favorites_dir(newidr)
            elif saveDirList[i].get_regeditKey() ==  "{374DE290-123F-4565-9164-39C4925E467B}" :
                opRegedit.OpRegedit.set_CURRENT_USER_download_dir(newidr)
            pass
        else:
            pass

def tab_ping_create(tabCtlFrame):
    #ping tab
    i = 0
    j = 0
    pad = 3
    def tab_pingAddress(add):
        iplist = list()  
        # ip = '192.168.1.11'  
        # ip = '172.24.186.191'  
        ip = 'www.baidu.com'  
        backinfo =  os.system('ping -c 1 -w 1 %s'%ip) # 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒  
        # print 'backinfo'  
        print (backinfo)  
        # print type(backinfo)  
        if backinfo:  
            return "ok"
            # print ('no' ) 
        else:  
            iplist.append(ip)  
            return "fail"

    # 字典是无序的
    showItem = {
        0: 'ping :',
        1: 'result :',
        # 2: 'RAM :',
        # 3: 'ip address :',
        # 4: 'arp address',
        # 5: "系统盘位置 ：",
        # 6: '分区信息 ：',
        # 7: '桌面目录位置 ：',
        # 8: '默认安装目录 ：',
        # 9: '注意事项：使用此软件需要关闭360等安全防护软件',
    }
        # 
    setPingIetms={ 
        0:tab_pingAddress,
        # 1:tab_msg_get_os_msg,
        # 2:getRAMinfo2,
        # 3:tab_msg_getIP,
        # 4:get_mac_address,
        # 5:get_os_drive,
        # 6:get_drive_msg,
        # 7:get_desktop,
        # 8:get_installDir,
    }
    var1 = tk.StringVar()
    l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
    var1.set(showItem[0])
    l1.grid(row=0,column =0, padx=pad, pady=pad, sticky=tk.W)

    e = tk.Entry(tabCtlFrame )
    # e.grid(row=i,column =1,columnspan=4, padx=0, pady=pad,ipadx =280, sticky=tk.W)
    e.grid(row=0,column =1 , padx=0, pady=pad,ipadx =enteryLen, sticky=tk.W)
    # e.insert("end","unknow yet")
    e.insert("end","input ip add here")
    ip = 'www.baidu.com'  
    resStr=tab_pingAddress(ip)

    var2 = tk.StringVar()
    l2 = tk.Label(tabCtlFrame, textvariable=var2, font=('Arial', 12))
    var2.set(showItem[1])
    l2.grid(row=1,column =0, padx=pad, pady=pad, sticky=tk.W)

    var3 = tk.StringVar()
    l3 = tk.Label(tabCtlFrame, textvariable=var3, font=('Arial', 12))
    var3.set(resStr)
    l3.grid(row=1,column =1, padx=pad, pady=pad, sticky=tk.W)


    # if i < len(setPingIetms):
    #     getstr=(setPingIetms[i])()
    #     tmpstr = e.get()
    #     e.delete(0,len(tmpstr))
    #     e.insert("end",getstr)
    # else:
    #     pass




def tab_msg_create(tabCtlFrame):
    xx = 10
    yy = 10
    w = 15
    h = 12
    i = 0
    j = 0
    pad = 3
    enteryLen=250
    '''
    显示信息：
    '''
    # itemToShow = 10

    def tab_msg_getPcName():
        hostn = socket.gethostname()
        # print ( "Host name: %s" %hostname)
        # sysinfo = socket.gethostbyname_ex(hostname)
        # ip_addr = sysinfo[2]
        # ip_addr1 = ip_addr[0]
        # ip_addr2 = ip_addr[1]
        # ip_addr3 = ip_addr[2]
        # ip_addr4 = ip_addr[3]
        # print("IP Address: %s" %ip_addr1,ip_addr2,ip_addr3,ip_addr4)
        return hostn

    def tab_msg_get_os_msg():
        # platform.platform()
        # platform.version() 
        return platform.platform()
        # return platform.version()
    def tab_msg_getIP():
        hostn = socket.gethostname()
        # print ( "Host name: %s" %hostname)
        ip_addr = socket.gethostbyname(hostn)
        return ip_addr


    # Return CPU temperature as a character string                                      
    # def getCPUtemperature():
    #     res = os.popen('vcgencmd measure_temp').readline()
    #     return(res.replace("temp=","").replace("'C\n",""))

    # # Return GPU temperature as a character string
    # def get_gpu_temp():
    #     gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    #     return  float(gpu_temp)
        # Uncomment the next line if you want the temp in Fahrenheit
        # return float(1.8* gpu_temp)+32


    # Return RAM information (unit=kb) in a list                                       
    # Index 0: total RAM                                                               
    # Index 1: used RAM                                                                 
    # Index 2: free RAM                                                                 
    def getRAMinfo2():
        pc_mem =psutil.virtual_memory()

        div_gb_factor =(1024.0 ** 3)
        # print("totalmemor: %fGB" % float(pc_mem.total/div_gb_factor))
        # print("availablememory: %fGB" % float(pc_mem.available/div_gb_factor))
        # print("usedmemory: %GB" % float(pc_mem.used/div_gb_factor))
        # print("percentof used memory: %f" % float(pc_mem.percent))
        # print("freememory:%fGB" % float(pc_mem.free/div_gb_factor))
        res = (pc_mem.total/div_gb_factor)
 
        res=round(res)
        tmpstr = str(res)
        tmpstr = tmpstr +  " GB"
       
        return tmpstr

    def getRAMinfo():
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                return(line.split()[1:4])
    # Return % of CPU used by user as a character string                                
    # def getCPUuse():
    #     return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\)))
    # Return information about disk space as a list (unit included)                     
    # Index 0: total disk space                                                         
    # Index 1: used disk space                                                         
    # Index 2: remaining disk space                                                     
    # Index 3: percentage of disk used                                                  
    def getDiskSpace():
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i +1
            line = p.readline()
            if i==2:
                return(line.split()[1:5])

    def get_drive_msg(): 
        # print( os.name)
        dMsg=DiskMsg()

        tmpstr=""
        templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
        for part in psutil.disk_partitions(all=False):
            # print( os.name)
            # tmpstr=tmpstr+" "
            if os.name == 'nt':  #如果是windows系统
                if 'cdrom' in part.opts or part.fstype == '':
                    # skip cd-rom drives with no disk in it; they may raise
                    # ENOENT, pop-up a Windows GUI error for a non-ready
                    # partition or just hang.
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            # tmpstr=tmpstr+part.device+": 总容量"+str(usage.total)+" 剩余容量"+str(usage.free)
            tmpstr=tmpstr+part.device+": 容量-"+ bytes2human(usage.total)+" 剩余-"+bytes2human(usage.free)+" "
            dMsg.addNewDisk(part.device,bytes2human(usage.total),bytes2human(usage.free))

        return tmpstr
    def get_os_drive(): 
        tmpstr = os.getenv("SystemDrive")
        return tmpstr
    def get_mac_address(): 
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
        return ":".join([mac[e:e+2] for e in range(0,11,2)])
    def get_desktop():
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,\
                            r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders',)
        return winreg.QueryValueEx(key, "Desktop")[0]
    def get_installDir():
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,\
                            r'Software\Microsoft\Windows\CurrentVersion',)
        return winreg.QueryValueEx(key, "ProgramFilesDir")[0]

    # 字典是无序的
    showItem = {
        0: 'pc name :',
        1: 'os version :',
        2: 'RAM :',
        3: 'ip address :',
        4: 'arp address',
        5: "系统盘位置 ：",
        6: '分区信息 ：',
        7: '桌面目录位置 ：',
        8: '默认安装目录 ：',
        9: '注意事项：使用此软件修改系统配置需要管理权限，以及关闭360等安全防护软件',
    }
        # 

    getSysMsgIetms={ 
        0:tab_msg_getPcName,
        1:tab_msg_get_os_msg,
        2:getRAMinfo2,
        3:tab_msg_getIP,
        4:get_mac_address,
        5:get_os_drive,
        6:get_drive_msg,
        7:get_desktop,
        8:get_installDir,
    }


    itemToShow = len(showItem)
    # for i in range(0, lenOfItem):
    #     print(i, " is ", showItem[i])
    for i in range(0, itemToShow):
        if i == (6):
            var1 = tk.StringVar()
            l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
            var1.set(showItem[i])
            l1.grid(row=i,column =0, padx=pad, pady=pad, sticky=tk.W)

            e = tk.Entry(tabCtlFrame )
            # e.grid(row=i,column =1,columnspan=4, padx=0, pady=pad,ipadx =280, sticky=tk.W)
            e.grid(row=i,column =1 , padx=0, pady=pad,ipadx =enteryLen, sticky=tk.W)
            # e.insert("end","unknow yet")
            e.insert("end","unknow yet")

            if i < len(getSysMsgIetms):
                getstr=(getSysMsgIetms[i])()
                tmpstr = e.get()
                e.delete(0,len(tmpstr))
                e.insert("end",getstr)
            else:
                pass
            # var2 = tk.StringVar()
            # l2 = tk.Label(tabCtlFrame, textvariable=var2, font=('Arial', 12))
            # var2.set("")
            # l2.grid(row=i,column =5, padx=pad, pady=pad, sticky=tk.W)

        if i == (itemToShow -1):
            var1 = tk.StringVar()
            l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 9),fg='blue' )
            var1.set(showItem[i])
            # l1.grid(row=i,column =0,columnspan=1, padx=pad, pady=pad,sticky=tk.SE )
            l1.grid(row=i,column =1 , padx=pad, pady=pad,sticky=tk.SE )
            # l1.grid(row=i,column =1 , padx=pad, pady=pad,sticky=tk.W )
            # l1.grid(row=i,column =0,columnspan=2, padx=pad, pady=pad, sticky=tk.E+tk.W)
        else:           
            var1 = tk.StringVar()
            l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
            var1.set(showItem[i])
            l1.grid(row=i,column =0, padx=pad, pady=pad, sticky=tk.W)
            # var1.get()
 
            e = tk.Entry(tabCtlFrame )
            # e.grid(row=i,column =1,columnspan=2, padx=0, pady=pad,ipadx = 80, sticky=tk.W)
            e.grid(row=i,column =1 , padx=0, pady=pad,ipadx = enteryLen, sticky=tk.W)
            # e.insert("end","unknow yet")
            e.insert("end","unknow yet")
            # tmpstr = e.get()
            # print('size of str :',len(tmpstr))
            # e.clipboard_clear()

            # getstr=getSysMsgIetms[i]()
            # print (i,"* ", len(getSysMsgIetms))
            # print( len(getSysMsgIetms))
            if i < len(getSysMsgIetms):
                getstr=(getSysMsgIetms[i])()
                tmpstr = e.get()
                e.delete(0,len(tmpstr))
                e.insert("end",getstr)
            else:
                pass




