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
# import win32

import wx
import myDirDialog
import opRegedit
import wmi

# if __name__ == '__main__':
#     print get_netcard()



class netconfg:


    def __init__(self,tabCtlFrame):
        i = 0
        j = 0
        pad = 0 
        enteryLen=0
        TextLen_tmp=30
        self.fireWallFlag=0
        self.cur_netCard=""
        self.cur_netCardname=""
        self.ipSetWay = 3 # ip设置方式 
        self.ipMsg={
            'ip': '192.168.1.2',
            'ipmask': '255.255.255.0',
            'gateway': '192.168.1.1',
            'dnsserver': '60.191.244.5'
            }
        self.ipMsgList=[]

        showItem = {
            0: 'ip设置方式', #手动设置0，自动获取1
            1: 'ip地址',
            2: '子网掩码',
            3: '默认网关',
            4: 'DNS服务器',
        }      
        self.get_netcard()

        itemToShow = len(showItem)
        for i in range(0, itemToShow):
            columnspan_tmp=1
            widthe=38
            if i == 0:
                var1 = tk.StringVar()
                l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
                var1.set(showItem[i])
                l1.grid(row=i,column =0, padx=pad, pady=pad, sticky=tk.W)

                # var2 = tk.StringVar()
                # l2 = tk.Label(tabCtlFrame, textvariable=var2, font=('Arial', 12))
                # var2.set("手动设置")
                # l2.grid(row=1,column =1, padx=pad, pady=pad, sticky=tk.W)

                # var3 = tk.StringVar()
                # l3 = tk.Label(tabCtlFrame, textvariable=var3, font=('Arial', 12))
                # var3.set("自动获取")
                # l3.grid(row=2,column =1, padx=pad, pady=pad, sticky=tk.W)

                r1 = tk.Radiobutton(tabCtlFrame, text='手动设置',
                            variable=self.ipSetWay, value=0,
                            command=self.self_ipSetWay_selection0)              
                r1.grid(row=1,column =0, padx=pad, pady=pad, sticky=tk.W)

                r2 = tk.Radiobutton(tabCtlFrame, text='自动获取',
                            variable=self.ipSetWay, value=1,
                            command=self.self_ipSetWay_selection1)              
                r2.grid(row=2,column =0, padx=pad, pady=pad, sticky=tk.W)

                var4 = tk.StringVar()
                l4 = tk.Label(tabCtlFrame, textvariable=var4, font=('Arial', 12))
                var4.set("网卡选择(双击选择)")
                l4.grid(row=0,column =1, padx=35, pady=pad, sticky=tk.W)


                varForNetcard = tk.StringVar()
                # for i in self.netcard_info

                varForNetcard.set(self.netcard_cardName) #为变量设置值

                #创建Listbox
                self.netCardLB = tk.Listbox(tabCtlFrame, listvariable=varForNetcard,height=7  )  #将var2的值赋给Listbox
                # self.netCardLB = tk.Listbox(tabCtlFrame, listvariable=varForNetcard,height=18,width=15 )  #将var2的值赋给Listbox
                # self.netCardLB = tk.Listbox(tabCtlFrame, listvariable=varForNetcard,height=5)  #将var2的值赋给Listbox
                #创建一个list并将值循环添加到Listbox控件中
                # list_items = [1,2,3,4]
                # for item in list_items:  #在varForNetcard之外再次添加
                #     lb.insert('end', item)   
                padxy=0
                self.netCardLB.bind('<Double-Button-1>',self.select_netCard)
                self.netCardLB.grid(row=1,column =1,rowspan=2,columnspan=2, padx=50, pady=padxy,ipadx=30)#, sticky=tk.W)  #,columnspan=4

                
                # var5 = tk.StringVar()
                # l5 = tk.Label(tabCtlFrame, textvariable=var5, font=('Arial', 10),foreground= '#4169E1')
                # var5.set("双击选择")
                # l5.grid(row=1,column =5, padx=pad, pady=pad, sticky=tk.W)

            elif i == 1:
                var1 = tk.StringVar()
                l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
                var1.set(showItem[i])
                l1.grid(row=i+2,column =0, padx=pad, pady=pad, sticky=tk.W)
  
                # e = tk.Entry(tabCtlFrame,state=tk.DISABLED )
                e = tk.Entry(tabCtlFrame  )
                e.grid(row=i+2,column =1 ,columnspan=columnspan_tmp, padx=0, pady=pad,ipadx = enteryLen, sticky=tk.W)
                e.insert("end", self.ipMsg['ip'] )
                e['width']=widthe
                self.ipMsgList.append(e)
                # e.state=tk.DISABLED'
                e['state'] = 'readonly'
            elif i == 2:
                var1 = tk.StringVar()
                l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
                var1.set(showItem[i])
                l1.grid(row=i+2,column =0, padx=pad, pady=pad, sticky=tk.W)
  
                e = tk.Entry(tabCtlFrame)#,state=tk.DISABLED )
                e.grid(row=i+2,column =1 ,columnspan=columnspan_tmp, padx=0, pady=pad,ipadx = enteryLen, sticky=tk.W)
                e.insert("end", self.ipMsg['ipmask'] )
                self.ipMsgList.append(e)
                e['state'] = 'readonly'
                e['width']=widthe

            elif i == 3:
                var1 = tk.StringVar()
                l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
                var1.set(showItem[i])
                l1.grid(row=i+2,column =0, padx=pad, pady=pad, sticky=tk.W)
  
                e = tk.Entry(tabCtlFrame)#,state=tk.DISABLED )
                e.grid(row=i+2,column =1 ,columnspan=columnspan_tmp, padx=0, pady=pad,ipadx = enteryLen, sticky=tk.W)
                e.insert("end", self.ipMsg['gateway'] )
                self.ipMsgList.append(e)
                e['width']=widthe
                e['state'] = 'readonly'

            elif i == 4:
                var1 = tk.StringVar()
                l1 = tk.Label(tabCtlFrame, textvariable=var1, font=('Arial', 12))
                var1.set(showItem[i])
                l1.grid(row=i+2,column =0, padx=pad, pady=pad, sticky=tk.W)
  
                e = tk.Entry(tabCtlFrame)#,state=tk.DISABLED )
                e.grid(row=i+2,column =1 ,columnspan=columnspan_tmp, padx=0, pady=pad,ipadx = enteryLen, sticky=tk.W)
                e.insert("end", self.ipMsg['dnsserver'] )
                self.ipMsgList.append(e)
                # e['state'] = 'readonly'
                e['width']=widthe

    
        pass
        lineUsed=itemToShow+2
        b = tk.Button(tabCtlFrame, 
            text='一键设置',      # 显示在按钮上的文字
            width=15, height=2, 
            command=self.changIPconfg)     # 点击按钮式执行的命令
        # b.grid(row=curRow,column =3 , padx=pad, pady=pad  )
        # b.height
        b.grid(row=lineUsed,column =7 , ipadx=0, ipady=0 , sticky=tk.W )    

        self.msgText = tk.Text(tabCtlFrame)

        #,ipadx = enteryLen
        self.msgText.grid(row=lineUsed,column =0 ,columnspan=2, padx=0, pady=0,ipadx=1, sticky=tk.W)
        self.msgText['width']=45
        self.msgText.insert("end", "init...")
        self.msgText['state']=tk.DISABLED
        # self.msgText.after
        # print("tk.END:",tk.END)
        
        # print("\n",self.netcard_info)


        #防火墙设置：
        l_fire_var1 = tk.StringVar()
        l_fire = tk.Label(tabCtlFrame, textvariable=l_fire_var1, font=('Arial', 12))
        l_fire_var1.set("防火墙设置（重启生效）：")
        l_fire.grid(row=i+2,column =0, padx=pad, pady=pad, sticky=tk.W)
        l_fire.grid(row=0,column =6 , ipadx=0, ipady=0 , sticky=tk.W )    


        r1 = tk.Radiobutton(tabCtlFrame, text='关闭',
                    variable=self.fireWallFlag, value=0,
                    command=self.self_fireWallFlag_selection0)              
        r1.grid(row=1,column =6, padx=pad, pady=pad, sticky=tk.W)

        r2 = tk.Radiobutton(tabCtlFrame, text='开启',
                    variable=self.fireWallFlag, value=1,
                    command=self.self_fireWallFlag_selection1)              
        r2.grid(row=2,column =6, padx=pad, pady=pad, sticky=tk.W)



        



    def self_fireWallFlag_selection1(self):
        self.fireWallFlag  =1
        # print(len(self.ipMsgList))
        # print(self.ipSetWay)
        # msgtextStr=self.msgText.get("0","end")
        # msgtextStr=msgtextStr+r"\n"+"ip设置方式为手动输入。"
        # self.msgText.insert()
        self.msgText['state']='normal'
        self.msgText.insert('end', '\n')
        self.msgText.insert('end', '选择防火墙开启')
        self.msgText['state']=tk.DISABLED
        # 这里直接就设置了吧
        opRegedit.OpRegedit.change_fireWall_set(1)



    def self_fireWallFlag_selection0(self):
        self.fireWallFlag  =0
        # print(len(self.ipMsgList))
        # print(self.ipSetWay)
        # msgtextStr=self.msgText.get("0","end")
        # msgtextStr=msgtextStr+r"\n"+"ip设置方式为手动输入。"
        # self.msgText.insert()
        self.msgText['state']='normal'
        self.msgText.insert('end', '\n')
        self.msgText.insert('end', '选择防火墙关闭')
        self.msgText['state']=tk.DISABLED

        opRegedit.OpRegedit.change_fireWall_set(0)

        
    #所有操作都在这里完成
    def changIPconfg(self):

        # print(self.cur_netCard[0])
        cur_netCard=self.cur_netCard[0]
        # cur_netCardname=self.cur_netCardname[cur_netCard]
        netcard_cardMacadd=str(self.netcard_cardMacadd[cur_netCard])

        netcard_cardMacadd_list=list(netcard_cardMacadd)
        netcard_cardMacadd_list[2]=':'
        netcard_cardMacadd_list[5]=':'
        netcard_cardMacadd_list[8]=':'
        netcard_cardMacadd_list[11]=':'
        netcard_cardMacadd_list[14]=':'
        netcard_cardMacadd="".join(netcard_cardMacadd_list)
        # print("netcard_cardMacadd:",netcard_cardMacadd)
        findadaptor=0

        # Obtain network adaptors configurations
        nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

        # First network adaptor
        # nic = nic_configs[0]
        for adaptor in nic_configs:
            # for var in range(0,len(adaptor)):
            # print (nic_configs[0].MACAddress)
            # print (adaptor.MACAddress)
            adaptorMacAdd=str(adaptor.MACAddress)
            if adaptorMacAdd == netcard_cardMacadd:
                nic = adaptor
                findadaptor=1      
        if self.ipSetWay == 0: #手动设置0，自动获取1



            # IP address, subnetmask and gateway values should be unicode objects
            # ip = u'192.168.0.11'
            # subnetmask = u'255.255.255.0'
            # gateway = u'192.168.0.1'
            if findadaptor == 1:
                ip=self.ipMsgList[0].get()
                subnetmask=self.ipMsgList[1].get()
                gateway=self.ipMsgList[2].get()
                # Set IP address, subnetmask and default gateway
                # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
                nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
                nic.SetGateways(DefaultIPGateway=[gateway])
                # print("ch adaptor done:ip",ip," sbmask:",subnetmask," gateway:",gateway)
            else :
                # print("can not find findadaptor")
                pass
        
        elif  self.ipSetWay == 1:
            if findadaptor == 1:
                # Obtain network adaptors configurations
                # nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

                # First network adaptor
                # nic = nic_configs[0]

                # Enable DHCP
                nic.EnableDHCP()

            else :
                # print("can not find findadaptor")
                pass






        # pass
    def select_netCard(self,event):
        # self.cur_netCard= self.netCardLB.get(self.netCardLB.curselection())
        # eve
        #在选择框中被选择的对象，一般内容为0,1..的列表，实际上只有一个值
        cur_netCard=self.netCardLB.curselection()
        le =len(cur_netCard)
        # print(le)
        if le >0 and le ==1:
            self.cur_netCard= self.netCardLB.curselection()
            self.cur_netCardname= self.netCardLB.get(self.cur_netCard)
            # print("card id",self.cur_netCard)
            # print("card name",self.cur_netCardname)
            self.msgText['state']='normal'
            self.msgText.insert('end', '\n')
            self.msgText.insert('end', '选择网卡：'+self.cur_netCardname)
            self.msgText['state']=tk.DISABLED        
        else:
            self.cur_netCard=""
            self.cur_netCardname=""
            self.ipSetWay=3
        # if condition:
        #     pass
        # else:
        #     pass


    def self_ipSetWay_selection0(self):
        self.ipSetWay=0
        # print(len(self.ipMsgList))
        # print(self.ipSetWay)
        # msgtextStr=self.msgText.get("0","end")
        # msgtextStr=msgtextStr+r"\n"+"ip设置方式为手动输入。"
        # self.msgText.insert()
        self.msgText['state']='normal'
        self.msgText.insert('end', '\n')
        self.msgText.insert('end', 'ip设置方式为手动输入。')
        self.msgText['state']=tk.DISABLED
        for e in self.ipMsgList:  
            # print(fruit)  
            # e.state=tk.NORMAL
            if e !=  self.ipMsgList[3]:
                e['state'] = 'normal'
                # print (e.get())

    def self_ipSetWay_selection1(self):
        self.ipSetWay=1

        self.msgText['state']='normal'
        self.msgText.insert('end', '\n')
        self.msgText.insert('end', 'ip设置方式为自动获取。')
        self.msgText['state']=tk.DISABLED       
        # # print(self.ipSetWay)
        # # print(len(self.ipMsgList))
        for e in self.ipMsgList:  
            # print(fruit)  
            # e.state=tk.DISABLED
            if e !=  self.ipMsgList[3]:
                e['state'] = 'readonly'
                # print (e.get())
            else:
                pass

        

    def get_netcard(self):
        """获取网卡名称和ip地址

        """
        self.netcard_cardName = []
        self.netcard_cardIP = []
        self.netcard_cardMacadd = []

        info = psutil.net_if_addrs()
        lastadd=""
        # psutil.net_if_stats
                # psutil.net_if_stats
        # i=0
        # j=0
        # isave=[]
        # jsave=[]
        for k, v in info.items():
            # print(k)
            # print(v)
            # print("\n")
            # j=0
            for item in v:
                # print(k)
                # print(v)
                # print(item[0])
                # print("\n")
                # print(item)
                # print("\n")
                # lastadd=item[1]
               
                if item[0] == 2 and not item[1] == '127.0.0.1':
                    # print(item[0])
                    # isave.append(i)
                    # jsave.append(j)
                    # self.netcard_info.append((k, item[1]))x
                    self.netcard_cardName.append(k)
                    self.netcard_cardIP.append(item[1])
                    self.netcard_cardMacadd.append(lastadd)
                lastadd=item[1]
            # i=i+1
        # info


        # print(self.netcard_cardName )
        # print(self.netcard_cardIP)
        # print(self.netcard_cardMacadd)
        # return netcard_info
