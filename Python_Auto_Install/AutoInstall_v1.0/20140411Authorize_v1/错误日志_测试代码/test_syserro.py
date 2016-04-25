#!/bin/python
#coding = utf-8

import re

def ReadStream(resfile,desfile):
    res_file = open(resfile,'r')
    des_file = open(desfile,'a+')
    while True:
        strline = res_file.readline()
        des_file.write(strline)
        if len(strline) == 0:
            break
        else:
            continue
    print "********************************************************************"
    str1 = "\n********************************************************************\n"
    des_file.write(str1)
            
def matchConfig(astr,filename):
    f = open(filename,'r+')
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

if __name__ == '__main__':
    number = matchConfig('num','config.txt')
    num = int(number)
    tmpdesfile = matchConfig('desfile','config.txt')
    print tmpdesfile
    print num
    for i in range(0,num):
        ReadStream('test.txt',str(tmpdesfile))
    print "End!"