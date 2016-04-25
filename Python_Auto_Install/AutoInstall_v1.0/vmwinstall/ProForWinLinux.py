#!/usr/bin/python
#coding=utf-8
'''
    ftp自动下载、自动上传脚本，可以递归目录操作
    8/10修改
'''

from ftplib import FTP
import platform
import socket
import sys
import os
import os.path
import stat
import re
import string
import datetime
import time

#reload(sys)
#sys.setdefaultencoding('utf-8')

class MYFTP:
    def __init__(self, hostaddr, username, password, remotedir, port=21):
        self.hostaddr = hostaddr
        self.username = username
        self.password = password
        self.remotedir  = remotedir
        self.port     = port
        self.ftp      = FTP()
        self.file_list = []
        # self.ftp.set_debuglevel(2)
    def __del__(self):
        self.ftp.close()
        # self.ftp.set_debuglevel(0)
    def login(self):
        ftp = self.ftp
        try: 
            timeout = 60
            socket.setdefaulttimeout(timeout)
            ftp.set_pasv(True)
            print '开始连接到 %s' %(self.hostaddr)
            ftp.connect(self.hostaddr, self.port)
            print '成功连接到 %s' %(self.hostaddr)
            print '开始登录到 %s' %(self.hostaddr)
            ftp.login(self.username, self.password)
            print '成功登录到 %s' %(self.hostaddr)
            debug_print(ftp.getwelcome())
        except Exception:
            deal_error("连接或登录失败")
        try:
            ftp.cwd(self.remotedir)
        except(Exception):
            deal_error('切换目录失败')

    def is_same_size(self, localfile, remotefile):
        try:
            remotefile_size = self.ftp.size(remotefile)
        except:
            remotefile_size = -1
        try:
            localfile_size = os.path.getsize(localfile)
        except:
            localfile_size = -1
        debug_print('lo:%d  re:%d' %(localfile_size, remotefile_size),)
        if remotefile_size == localfile_size:
            return 1
        else:
            return 0
    def download_file(self, localfile, remotefile):
        if self.is_same_size(localfile, remotefile):
            debug_print('%s 文件大小相同，无需下载' %localfile)
            return
        else:
            debug_print('>>>>>>>>>>>>下载文件 %s ... ...' %localfile)
        #return
        file_handler = open(localfile, 'wb')
        self.ftp.retrbinary('RETR %s'%(remotefile), file_handler.write)
        file_handler.close()

    def download_files(self, localdir='./', remotedir='./'):
        try:
            self.ftp.cwd(remotedir)  #设置remotedir为当前工作目录
        except:
            debug_print('目录%s不存在，继续...' %remotedir)
            return
        if not os.path.isdir(localdir):
            os.makedirs(localdir)
        debug_print('切换至目录 %s' %self.ftp.pwd())
        self.file_list = []
        self.ftp.dir(self.get_file_list)
        remotenames = self.file_list
        #print(remotenames)
        #return
        for item in remotenames:
            filetype = item[0]
            filename = item[1]
            local = os.path.join(localdir, filename)
            if filetype == 'd':
                self.download_files(local, filename)
            elif filetype == '-':
                self.download_file(local, filename)
        self.ftp.cwd('..')
        debug_print('返回上层目录 %s' %self.ftp.pwd())
    def upload_file(self, localfile, remotefile):
        if not os.path.isfile(localfile):
            return
        if self.is_same_size(localfile, remotefile):
            debug_print('跳过[相等]: %s' %localfile)
            return
        file_handler = open(localfile, 'rb')
        self.ftp.storbinary('STOR %s' %remotefile, file_handler)
        file_handler.close()
        debug_print('已传送: %s' %localfile)
        print "upload success!"
    def upload_files(self, localdir='./', remotedir = './'):
        if not os.path.isdir(localdir):
            return
        localnames = os.listdir(localdir)
        self.ftp.cwd(remotedir)
        for item in localnames:
            src = os.path.join(localdir, item)
            if os.path.isdir(src):
                try:
                    self.ftp.mkd(item)
                except:
                    debug_print('目录已存在 %s' %item)
                self.upload_files(src, item)
            else:
                self.upload_file(src, item)
        self.ftp.cwd('..')

    def get_file_list(self, line):
        ret_arr = []
        file_arr = self.get_filename(line)
        if file_arr[1] not in ['.', '..']:
            self.file_list.append(file_arr)
            
    def get_filename(self, line):
        pos = line.rfind(':')
        while(line[pos] != ' '):
            pos += 1
        while(line[pos] == ' '):
            pos += 1
        file_arr = [line[0], line[pos:]]
        return file_arr
def debug_print(s):
    print (s)
def deal_error(e):
    timenow  = time.localtime()
    datenow  = time.strftime('%Y-%m-%d', timenow)
    logstr = '%s 发生错误: %s' %(datenow, e)
    debug_print(logstr)
    file.write(logstr)
    sys.exit()
    
def judgeOs():
    os_str=platform.architecture()
    print os_str
    v = os_str[1]
    return v
    
def isFileEmpty(filepath):
    filesize=os.stat(filepath).st_size
    if filesize==0:
        return True
    else:
        return False

def timeSleep(seconds,winindir,linuxindir):
    print datetime.datetime.now()
    time.sleep(seconds)
    print datetime.datetime.now()
    testfilename = hostName()
    testfile = strLink(testfilename,"-")
    testfilestr = testfile+".log"
    v = judgeOs()
    if v == "WindowsPE":
        os.chdir(winindir)
        initdb_exit=os.path.isfile('initdb.log')
        print initdb_exit
    elif v == "ELF":
        os.chdir(linuxindir)
        initdb_exit=os.path.isfile('initdb.log')
        print initdb_exit
    else:
        print "wrong"
    if initdb_exit:
        #os.chdir(linuxindir)
        infile=open('initdb.log','rb')
        outfile=open(testfilestr,'wb')
        outfile.write(infile.read())
        infile.close()
        outfile.close()
    else:
        print "the file not exit!"
    #file('resultdb.log', 'wb').write(file('initdb.log', 'rb').read())
    isempty=isFileEmpty("initdb.log")
    testfilename = hostName()
    testfile = strLink(testfilename,"-")
    testfilestr = testfile+".log"
    if isempty:
        resultstring="database initionized successfully!"
        fil=open(testfilestr,'wb+')
        fil.write(resultstring)
        fil.close()
        print "success"
    else:
        resultstring="database initionized failed!"
        fil=open(testfilestr,'wb+')
        fil.write(resultstring)
        fil.close()
        print "failed!"

def hostName():   
    sys = os.name   
    if sys == 'nt':   
        hostname = os.getenv('computername')
        print hostname 
        list_hostname=string.split(hostname, "-") 
        list_hostname[0] = list_hostname[0].lower()
        list_hostname[1] = list_hostname[1].lower()
        list_hostname[2] = list_hostname[2].lower()
        list_hostname[3] = list_hostname[3].lower()
        print list_hostname 
        return list_hostname   
  
    elif sys == 'posix':   
        host = os.popen('echo $HOSTNAME')   
        try:   
            hostname = host.read()
            file_hostname = open('htname.txt','w')
            file_hostname.write(hostname)
            file_hostname.close()
            open_file = open("htname.txt",'r')
            fileline = open_file.readline()
            fileline = fileline.strip('\n\r')
            list_hostname=string.split(fileline, "-")
            file_hostname.close()
            os.remove("htname.txt")
            return list_hostname
                
        finally: 
            host.close()   
    else:   
        print "wrong"

#从文件中读取参数实现安装目录、传参安装自动化
def matchfileline():
    f = open("parameter_set.txt",'r')#8/10
    f.readline()
    hostname=hostName()
    print hostname
    while True:
        fileline = f.readline()
        fileline = fileline.strip('\n\r')
        paralist = fileline.split(',')
        if not fileline:
            break
        if paralist[0]==hostname[0] and paralist[1]==hostname[1] and paralist[2]==hostname[2] and paralist[3]==hostname[3]:
            return paralist
    print paralist

#删除文件中的确认安装行
def del_line_of_sh(chmodfile):
    alist = []  
    name="#确认是否要安装"                            
    matchPattern = re.compile(name) 
    del_lineof_file = open(chmodfile,'r')          
    while 1:
        line = del_lineof_file.readline()             
        if not line:                        
            break
        elif matchPattern.search(line):    
            line = del_lineof_file.readline()
            pass
        else:                              
            alist.append(line)               
    del_lineof_file.close()

    del_lineof_file = open(chmodfile, 'w')        
    for i in alist:                       
        del_lineof_file.write(i)                      
    del_lineof_file.close()
    
def judgeOsAndInstall(defaultdir,chmodfile,wininstallfile,para):
    v = judgeOs() 
    if v=="WindowsPE":
        os.chdir(defaultdir)
        if "derby" in para[4] or "pgsql" in para[4]:
            if para[3]=="df":
                command="start "+wininstallfile+" /silent /licensedriver no /dbtype "+para[4]+" /ftp "+para[5]+" /service "+para[6]+" /launch yes"
            elif para[3]=="hk":
                command="start "+wininstallfile+" /silent /licensedriver no /lang "+"TW"+" /dbtype "+para[4]+" /ftp "+para[5]+" /service "+para[6]+" /launch yes"
            else:
                command="start "+wininstallfile+" /silent /licensedriver no /lang "+para[3]+" /dbtype "+para[4]+" /ftp "+para[5]+" /service "+para[6]+" /launch yes"
                print command
        if "oracle" in para[4]:
            if para[3]=="df":
                command="start "+wininstallfile+" /silent /licensedriver no /dbtype "+para[4]+" /dbip "+para[8]+" /initdb yes"+" /ftp "+para[5]+" /service "+para[6]+" /dbauser sys /dbapwd sys /tablespacesize 2 /launch yes"
                print command
            elif para[3]=="hk":
                command="start "+wininstallfile+" /silent /licensedriver no /lang "+"TW"+" /dbtype "+para[4]+" /dbip "+para[8]+" /initdb yes"+" /ftp "+para[5]+" /service "+para[6]+" /dbauser sys /dbapwd sys /tablespacesize 2 /launch yes"
            else:
                command="start "+wininstallfile+" /silent /licensedriver no /lang "+para[3]+" /dbtype "+para[4]+" /dbip "+para[8]+" /initdb yes"+" /ftp "+para[5]+" /service "+para[6]+" /dbauser sys /dbapwd sys /tablespacesize 2 /launch yes"
                print command
        if "sybase" in para[4]:
            if para[3]=="df":
                command="start "+wininstallfile+" /dbip "+para[8]+" /silent /licensedriver no /dbtype "+para[4]+" /ftp "+para[5]+" /service "+para[6]+" /dbauser sa /dbapwd 123456 /tablespacesize 2 /launch yes"
            elif para[3]=="hk":
                command="start "+wininstallfile+" /dbip "+para[8]+" /silent /licensedriver no /lang "+"TW"+" /dbtype "+para[4]+" /ftp "+para[5]+" /service "+para[6]+" /dbauser sa /dbapwd 123456 /tablespacesize 2 /launch yes"
            else:
                command="start "+wininstallfile+" /dbip "+para[8]+" /silent /licensedriver no /lang "+para[3]+" /dbtype "+para[4]+" /ftp "+para[5]+" /service "+para[6]+" /dbauser sa /dbapwd 123456 /tablespacesize 2 /launch yes"
        #command = "start DMB-BS3.1.28.24425-finance-win-x86.exe /silent /lang en /dbtype pgsql /ftp yes /service yes /lauch yes"
        os.system(command)
    if v=="ELF":
        #hostname=hostName() 
        #print hostname
        os.chdir(defaultdir)
        del_line_of_sh(chmodfile)
        os.chmod(chmodfile,stat.S_IRWXU+stat.S_IRWXG+stat.S_IRWXO)
        
        if "derby" in para[4]:
            if para[3]=="df":
                command = "nohup ./" +chmodfile+" -d "+para[4]+ " -f "+para[5]+ " -s "+para[6]+" \&"
            elif para[3]=="hk":
                command = "nohup ./" +chmodfile+" -l "+"TW"+" -d " +para[4]+ " -f "+para[5]+ " -s "+para[6]+" \&"
            else:
                command = "nohup ./" +chmodfile+" -l "+para[3]+" -d " +para[4]+ " -f "+para[5]+ " -s "+para[6]+" \&"
        if "pgsql" in para[4]:
            if para[3]=="df":
                command = "nohup ./" +chmodfile+" -d "+para[4]+" -f "+para[5]+" -s "+para[6]+" \&"
            elif para[3]=="hk":
                command = "nohup ./" +chmodfile+" -l "+"TW"+" -d "+para[4]+" -f "+para[5]+ " -s "+para[6]+" \&"
            else:
                command = "nohup ./" +chmodfile+" -l "+para[3]+" -d "+para[4]+" -f "+para[5]+ " -s "+para[6]+" \&"
        if "oracle" in para[4]:
            if para[3]=="df":
                command = "nohup ./" +chmodfile+" -i "+para[8]+" -d " +para[4]+ " -f " +para[5]+ " -s "+para[6]+" -b sys -w sys -e 2 \&"
            elif para[3]=="hk":
                command = "nohup ./" +chmodfile+" -i "+para[8]+" -l "+"TW"+" -d " +para[4]+ " -f " +para[5]+ " -s "+para[6]+" -b sys -w sys -e 2 \&"
            else:
                command = "nohup ./" +chmodfile+" -i "+para[8]+" -l "+para[3]+" -d " +para[4]+ " -f " +para[5]+ " -s "+para[6]+" -b sys -w sys -e 2 \&"
        if "sybase" in para[4]:
            if para[3]=="df":
                command = "nohup ./" +chmodfile+" -i "+para[8]+" -d " +para[4]+ " -f " +para[5]+ " -s "+para[6]+" -b sa -w 123456 -e 2 \&"
            elif para[3]=="hk":
                command = "nohup ./" +chmodfile+" -i "+para[8]+" -l "+"TW"+" -d " +para[4]+ " -f " +para[5]+ " -s "+para[6]+" -b sa -w 123456 -e 2 \&"
            else:
                command = "nohup ./" +chmodfile+" -i "+para[8]+" -l "+para[3]+" -d " +para[4]+ " -f " +para[5]+ " -s "+para[6]+" -b sa -w 123456 -e 2 \&"
        os.system(command)  

def strLink(alist,a):
    #a = '_'
    strlink = a.join(alist)
    return strlink

if __name__ == '__main__':
    afile = open("log.txt", "a")
    timenow  = time.localtime()
    datenow  = time.strftime('%Y-%m-%d', timenow)
    logstr = datenow
    # 配置如下变量
    hostaddr = '192.168.65.192' # ftp地址
    username = 'unlimit' # 用户名
    password = 'unlimit' # 密码
    port  =  21   # 端口号 
    rootdir_local = '/starnet/'
    
    #judge and install
    defaultdir = "/starnet"

    filename = hostName()
    hostlocalfile = strLink(filename,"-")
    localfile = hostlocalfile+".log"
    print localfile
    #localfile = "resultdb.log"
    para = matchfileline()
    print para
    if "nologo" not in para[9]:
        sublist = [para[9],para[10]]
        substrlink = strLink(sublist,'_')
    #print substrlink
        #rootdir_remote01 = para[8]+"_"+para[9]
    else:
        sublist = [para[10],para[11]]
        substrlink = strLink(sublist,'_')
    #print substrlink
    rootdir_remote1 = os.path.join("/DMB发布_BS3.1＋精简版/BS3.1/",para[7])#8/10
    rootdir_remote = rootdir_remote1 + "/" +substrlink
    print rootdir_remote 
    remotefile = os.path.basename(localfile)
    rootdir_remote=rootdir_remote.decode("utf-8").encode("gb2312")

    f = MYFTP(hostaddr, username, password, rootdir_remote, port)
    f.login()
    f.download_files(rootdir_local, rootdir_remote)
    
    timenow  = time.localtime()
    datenow  = time.strftime('%Y-%m-%d', timenow)
    logstr += " - %s 成功执行了备份\n" %datenow
    debug_print(logstr)
    
    afile.write(logstr)
    afile.close()
    
    #验证数据库是否初始化成功
    seconds = 600
    #commanfile = "dmb-"+para[7]
    chmodfile = "dmb-"+para[-1]+"-setup.sh"#8/10
    #print chmodfile
    if "nologo" not in para[9]:
        wininstallfile1 = "DMB-"+para[-1]+"-"+para[10]+"-"+para[9]+"-x86"#8/10
        #print wininstallfile1
        wininstallfile = wininstallfile1+".exe"#8/10
        #print wininstallfile
        winindir = "C:\\"+wininstallfile1+"\dmb"#8/10
        #print winindir
    else:
        wininstallfile1 = "DMB-"+para[-1]+"-"+para[11]+"-"+para[9]+"-"+para[10]+"-x86"#8/10
        #print wininstallfile1
        wininstallfile = wininstallfile1+".exe"#8/10
        #print wininstallfile
        winindir = "C:\\"+wininstallfile1+"\dmb"#8/10
        #print winindir
        
    list0 = [para[-1],para[10],para[9]]
    list_link = strLink(list0,'-')
    linuxindir = "dmb-"+list_link+"/dmb"#8/10
    #print linuxindir
    
    #judge and install
    judgeOsAndInstall(defaultdir,chmodfile,wininstallfile,para)
    
    #check
    timeSleep(seconds,winindir,linuxindir)
    #upload
    f1 = MYFTP(hostaddr,username,password,rootdir_remote,port)
    f1.login()
    f1.upload_file(localfile,remotefile)
    
    
    


    
