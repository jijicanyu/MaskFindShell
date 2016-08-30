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
                            
                            print u'FilePath: ',
                            print filepath
                            print u'describe: ',
                            print result[1]
                            print u'code: ',
                            for code in result[0]:
                                print code[0][0:100]
                            print u'time: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))+'\n\n'
                            backdoor_count= backdoor_count+1
                          
                            break

def ScanFiletime(path,times):
    global backdoor_count
    times = time.mktime(time.strptime(times, '%Y-%m-%d %H:%M:%S'))
    print u'########################################'
    print u'FilePath           time   \n'

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
        print u'【Error】'
        print u'style1: '+sys.argv[0]+u' filepath'
        print u'style2: '+sys.argv[0]+u' filepath time(Forexample:"2013-09-09 12:00:00")'
        sys.exit()
       
    if os.path.lexists(sys.argv[1])==False:
        print u'【Error Tag】：not found file---'
        sys.exit()

    if len(sys.argv)==2:
        print u'\n\n【Start】'
        print sys.argv[1]+'\n'
        Scan(sys.argv[1])
        print u'【End】'
        print u'\tsum number: '+str(backdoor_count)
    else:
        print u'\n\n【Start】'
        print sys.argv[1]+'\n'
        ScanFiletime(sys.argv[1],sys.argv[2])
        print u'\n【End】'
        print u'\tsum number: '+str(backdoor_count)