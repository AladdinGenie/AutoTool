#!/usr/bin/python
#coding=utf-8
import os,platform
import shutil
systemStr = platform.architecture()
for i in range(len(systemStr)):
    systemStr_0=systemStr[0]
    systemStr_1=systemStr[1]
    if (systemStr_1 == "WindowsPE"):
        os.system("rd /s/q dist")
        os.system("rd /s/q build")
        #print "Sucessful"
    else:
        os.system("rm dist -rf")
        os.system("rm build -rf") 
os.system("python setup.py py2exe")
ls = os.listdir("dist")
for i in ls:
    if i[-3:] == 'exe' and i!= 'w9xpopen.exe':
        shutil.move("Microsoft.VC90.CRT.manifest", 'dist')
        shutil.move("msvcr90.dll", 'dist')
        shutil.move("parameter_set.txt", 'dist')
        print "打包成功"
