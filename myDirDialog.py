# -- coding: utf-8
import sys
import io
import os
import wx  
'''
class DirDialog(wx.Frame):  
  
  
    #----------------------------------------------------------------------  
    def __init__(self):  
        # """Constructor"""  
        wx.Frame.__init__(self,None,-1,u"文件夹选择对话框")  
        b = wx.Button(self,-1,u"文件夹选择对话框")  
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)  
          
    #----------------------------------------------------------------------  
    def OnButton(self, event):  
 
        dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)  
        if dlg.ShowModal() == wx.ID_OK:  
            print (dlg.GetPath()) #文件夹路径  
              
        dlg.Destroy()  
'''

'''
    changDir = {
        0: '文档',
        1: '桌面',
        2: '下载',
        3: '收藏夹',
    }  
''' 
class RegeditSaveDir:
    #记录单个需要修改目录的对应的  名字    新的目录          注册表的key
    #           如：            文档    f:\\我的文档      Personal
    # zhName=""
    # newDir=""
    # regeditKey=""
    population=0
    # zhName
    # newDi
    # regeditKey


    def __init__(self,zhName,newDir,regeditKey):
        self.__zhName=zhName
        self.__newDir=newDir
        self.__regeditKey=regeditKey
        RegeditSaveDir.population=RegeditSaveDir.population+1
        # self.printDir()
        pass
    def get_regeditKey(self):
        return self.__regeditKey

    def get_newDir(self):
        return self.__newDir
    def get_zhName(self):
        return self.__zhName

    # # @classmethod
    # def getRegeditKey(self):
    #     return self.__regeditKey
    # # @classmethod
    # def getNewDir(self):
    #     return self.__newDir
    # @classmethod
    def setNewDir(self,newDir):
        self.__newDir=newDir
    @classmethod
    def printDir(clf):
        print("printDir count:",RegeditSaveDir.population)
        # print(clf.zhName," ",clf.newDir," ",clf.regeditKey)

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
 
        os.makedirs(path) 
        print("新目录",path,"创建成功")
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print("新目录没有创建")
        return False