#!/usr/bin/python
#coding = utf-8

import os
import re

path = '/sunshine/backups'
localfile = '/zx/result.txt'

def writefile(astr,local_path):
    output = open(local_path,'a+')
    output.write(astr)
    output.close()

def getSize(strPath):  
    if not os.path.exists(strPath):  
        return 0;  
  
    if os.path.isfile(strPath):  
        return os.path.getsize(strPath);  
  
    nTotalSize = 0;  
    for strRoot, lsDir, lsFiles in os.walk(strPath):  
        #get child directory size  
        for strDir in lsDir:  
            nTotalSize = nTotalSize + getSize(os.path.join(strRoot, strDir));  
  
        #for child file size  
        for strFile in lsFiles:  
            nTotalSize = nTotalSize + os.path.getsize(os.path.join(strRoot, strFile));  
  
    return nTotalSize; 

def matchConfig(astr,filename):
    f = open(filename,'r')
    matchPattern = re.compile(astr)
    strline = f.readline()
    while True:
        strline = f.readline()
        if not strline:
            break
        else:
            if matchPattern.search(strline):
                ttmp_str = str(strline).strip('\n\t')
                tmp_str = ttmp_str.split('=') 
                print tmp_str
                return tmp_str[-1]
                break

set_backupday = matchConfig('set_backupday','config.txt')
backday = int(set_backupday)            

list_backupdir = []
list_backupdir = os.listdir(path)
print "backup目录下的文件列表如下："
str2 = "backup目录下的文件列表如下：\n"
writefile(str2,localfile)
print list_backupdir
#writefile(list_backupdir,localfile)
writefile('[',localfile)
for i in list_backupdir:
    writefile(i,localfile)
    writefile(",",localfile)
writefile(']',localfile)

command = 'date +%Y%m%d'
tmp_today = os.popen(command)
get_today = tmp_today.read()
#writefile(get_today,localfile)
to_day = int(get_today)

Int_list = []
for i in list_backupdir:
    Int_list.append(int(i))

len_listdir = len(list_backupdir)
if len_listdir <= backday:
    re_path = path + '//' + str(to_day)
    print re_path
    Totalsize = getSize(re_path)
    if Totalsize != 0:
        if to_day in Int_list:
            flag = 1
            print "yes!在backup目录下能找到当天备份的文件！"
            str3 = "yes!在backup目录下能找到当天备份的文件！\n"
            writefile(str3,localfile)
        else:   
            print "备份出错！没有当天的备份文件！"
            str4 = "备份出错！没有当天的备份文件！\n"
            writefile(str4,localfile)
    else:
        print "%d文件为空！"%to_day
        str5 = "%d文件为空！"%to_day
        writefile(str5,localfile)
else:
    sorted_dirlist = sorted(Int_list)
    print "排序之后的backup目录下的文件列表："
    str6 = "排序之后的backup目录下的文件列表：\n"
    writefile(str6,localfile)
    print sorted_dirlist 
    for i in range(len_listdir - backday):     
        print "该删除的文件是：%d"%(i)
        str7 = "该删除的文件是：%d"%(i)
        writefile(str7,localfile)
    
