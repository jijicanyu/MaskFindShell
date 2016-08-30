#!/usr/bin/python2.7
#!coding=utf-8

import os
import sys
import time

plusarr=[] #插件列表
backdoor_count=0

def loadplus():
    for root,dirs,files in os.walk("plus"):
        for filespath in files:
            if filespath[-3:] == '.py':
                plusname = filespath[:-3]
                if plusname=='__init__':
                    continue
                __import__('plus.'+plusname)
                plusarr.append(plusname)

def Scan(path):
    loadplus() #动态添加插件
    global backdoor_count
    for root,dirs,files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root,filename)
            if os.path.getsize(filepath)<500000:
                    for plus in plusarr:
                        file= open(filepath,"rb")
                        filestr = file.read()
                        file.close()
                        result = sys.modules['plus.'+plus].Check(filestr,filepath)

                        if result!=None:
                            
                            print u'文件: ',
                            print filepath
                            print u'后门描述: ',
                            print result[1]
                            print u'后门代码: ',
                            for code in result[0]:
                                print code[0][0:100]
                            print u'最后修改时间: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))+'\n\n'
                            backdoor_count= backdoor_count+1
                          
                            break

def ScanFiletime(path,times):
    global backdoor_count
    times = time.mktime(time.strptime(times, '%Y-%m-%d %H:%M:%S'))
    print u'########################################'
    print u'文件路径           最后修改时间   \n'

    for root,dirs,files in os.walk(path):
        for curfile in files:
            if '.' in curfile:
                f=curfile.split(".")
                c=""
                for i in range(len(f)):
                    if i==0:
                       pass
                    else:
                        c=c+"."+f[i]
                suffix = c.lower()
                filepath = os.path.join(root,curfile)
                if 'php' in suffix or 'jsp' in suffix:
                    FileTime =os.path.getmtime(filepath)
                    if FileTime>times:
                        backdoor_count +=1
                        print filepath+'        '+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(FileTime))

if __name__ == "__main__":
    print u'----------------------------------------'
    print u"""
          ╭╮　　　　　　　╭╮　　
       　││　　　　　　　││　　
       ╭┴┴———————┴┴╮
       │　　　　　　　　　　　│　　　
       │　　　　　　　　　　　│　　　
       │　●　　　　　　　●　│
       │○　　╰┬┬┬╯　　○│
       │　　　　╰—╯　　　　│　
       ╰——┬Ｏ———Ｏ┬——╯
       　 　╭╮　　　　╭╮　　　　
       　 　╰┴————┴╯
----┏━☆━━━━━━━━━━━━┓----
----┃ MaskFindShell 1.0          ┃----
----┃ Author:nmask               ┃----
----┃ SITE:www.maskghost.com     ┃----
----┗━━━━━━━━━━━━━━┛----
    """

    if len(sys.argv)!=3 and len(sys.argv)!=2:
        print u'【参数错误】'
        print u'按恶意代码查杀: '+sys.argv[0]+u' 目录名'
        print u'按修改时间查杀: '+sys.argv[0]+u' 目录名 最后修改时间(格式:"2013-09-09 12:00:00")'
        sys.exit()
       
    if os.path.lexists(sys.argv[1])==False:
        print u'【错误提示】：指定的扫描目录不存在---'
        sys.exit()

    if len(sys.argv)==2:
        print u'\n\n【开始查杀】'
        print sys.argv[1]+'\n'
        Scan(sys.argv[1])
        print u'【查杀完成】'
        print u'\t后门总数: '+str(backdoor_count)
    else:
        print u'\n\n【开始查找】'
        print sys.argv[1]+'\n'
        ScanFiletime(sys.argv[1],sys.argv[2])
        print u'\n【查找完成】'
        print u'\t文件总数: '+str(backdoor_count)