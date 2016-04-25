#!/usr/bin/python
#coding = utf-8

import os
import time
import re

localfile = '/zx/result.txt'

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
            
def writefile(astr,local_path):
    output = open(local_path,'a+')
    output.write(astr)
    output.close()
            
set_sleeptime = matchConfig('set_sleeptime','config.txt')
sleeptime = int(set_sleeptime)
set_sysday = matchConfig('set_sysday','config.txt')
numdays = int(set_sysday)

print "读取当天的时间："
str1 = "读取当天的时间：\n"
writefile(str1,localfile)
command = "date"
tmp = os.popen(command)
str2 = tmp.read()
writefile(str2,localfile)

for i in range(numdays):
    print "*******************************************"
    str5 = "*******************************************\n"
    writefile(str5,localfile)
    print "下一天日期（设置年月日）："
    str6 = "下一天日期（设置年月日）：\n"
    writefile(str6,localfile)
    command1 = "date -d next-day +%Y%m%d "
    tmp_time = os.popen(command1)
    set_time = tmp_time.read()
    writefile(set_time,localfile)
    command2 = "date -s " + '"' + str(set_time) + '"'
    str7_tmp = os.popen(command2)
    str7 = str7_tmp.read()
    writefile(str7,localfile)
    print "设置时分秒之后的时间："
    str8 = "设置时分秒之后的时间：\n"
    writefile(str8,localfile)
    command3 = "date -s 02:59:00"
    str9_tmp = os.popen(command3)
    str9 = str9_tmp.read()
    writefile(str9,localfile)
    print "运行验证到凌晨3点时是否生成文件：\n"
    time.sleep(sleeptime)
    os.system('python verify.py')
    time.sleep(20)
    #print list_backupdir

