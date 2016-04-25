#************************************************************************
#************************************************************************
#本地测试环境：
#    vmx_dir = "C:\Program Files\VMware\VMware Workstation"
#    machinesdir = "D:\virturemuchine"
#其中：
#    vmx_dir：".vmx"文件所在的根目录
#    machinesdir：虚拟机存放根目录
#************************************************************************
#************************************************************************

#!/bin/python
#coding = utf-8

from Tkinter import *
import tkMessageBox
import string
import os
from os.path import *
import tkFileDialog
import shelve
import struct
import time

choices = []
true_choices = []
AllMachine = ['1-win8-32-zh','2-win7-32-en','7-win8-64-en','8-win7-64-zh','10-win2k8-64-df',
'11-RedHat5.4-x64-df','13-RedHat6.4-x32-df','14-win8-32-TW','15-win7-32-en',
'16-win2k3-32-zh','18-RedHat5.4-x32-zh','19-RedHat6.4-x32-TW','20-SUSE11-x32-df',
'21-win8-32-hk','22-win7-32-TW','23-win2k3-32-en','25-win2k8-64-en',
'26-RedHat5.4-x64-zh','29-win8-64-df','30-win2k3-64-TW','33-RedHat5.4-x32-en',
'34-RedHat6.4-x32-zh','35-SUSE11-x32-zh','36-win8-32-en','37-win7-32-df',
'38-win7-64-TW','39-win2k3-64-df','41-SUSE11-x64-zh','42-win8-64-hk']
#AllMachine = ['1-win8-32-zh']
DbMachine = ['10-win2k8-64-df','14-win8-32-TW','16-win2k3-32-zh','21-win8-32-hk',
             '26-RedHat5.4-x64-zh','29-win8-64-df','34-RedHat6.4-x32-zh',
             '37-win7-32-df','39-win2k3-64-df','42-win8-64-hk']
Database = ['110RedHat5.4_x32_en_ORACLE','114RedHat5.4_x32_en_ORACLE','116RedHat5.4_x32_cn_dmbsybase',
            '121RedHat5.4_x32_cn_dmbsybase','126RedHat5.4_x32_cn_dmbsybase','129RedHat5.4_x32_cn_dmbsybase',
            '134RedHat5.4_x32_en_ORACLE','137RedHat5.4_x32_cn_dmbsybase','139RedHat5.4_x32_en_ORACLE',
            '142RedHat5.4_x32_cn_dmbsybase']

#Checkbar和Quitter类是用来布局界面的
class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)
            choices.append(pick)
    def state(self):
        return map((lambda var: var.get()), self.vars)

class Quitter(Frame):                      
    def __init__(self, parent=None):      
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)
    def quit(self):
        ans = tkMessageBox.askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)

#用来绘制选择文件路径的
def makeFormRow(parent, label, width=15, browse=True, extend=False):
    var = StringVar()
    row = Frame(parent)
    lab = Label(row, text=label, relief=RIDGE, width=width)
    ent = Entry(row, relief=SUNKEN, textvariable=var)
    row.pack(fill=X)                                  # uses packed row frames
    lab.pack(side=LEFT)                               # and fixed-width labels
    ent.pack(side=LEFT, expand=YES, fill=X)           # or use grid(row, col)
    if browse:
        btn = Button(row, text='浏览。。。')
        btn.pack(side=RIGHT)
        if not extend:
            btn.config(command=
                 lambda: var.set(tkFileDialog.askdirectory() or var.get()) )
        else:
            btn.config(command=
                 lambda: var.set(var.get() + ' ' + tkFileDialog.askdirectory()) )
    return var    

def entryGui(parent,label):
    var = IntVar()
    row = Frame(parent)
    lab = Label(row,text = label)
    ent = Entry(row,textvariable = var)
    
    row.pack(fill = X)
    lab.pack(side = LEFT)
    ent.pack(side = LEFT)
    
    var.set(var.get())
    return var

#绘制选择路径界面
def packDialog():                               # a new top-level window
    win = Toplevel()                            # with 2 row frames + ok button
    win.title('选择目录')
    var1 = makeFormRow(win, label='vmware目录')
    var2 = makeFormRow(win, label='虚拟机存放目录', extend=True)
    var3 = entryGui(win,label = '一次打开虚拟机台数')
    Button(win, text='确定', command=win.destroy).pack()
    #root = Tk()
    #root.update()
    #root.deiconify()
    win.grab_set()
    win.focus_set()                  # go modal: mouse grab, keyboard focus, wait
    win.wait_window()                # wait till destroy; else returns now
    return var1.get(), var2.get(), var3.get()  # fetch linked var values


#功能：在界面中勾选需要打开的虚拟机之后，将需要打开的虚拟机名称放入列表中存储起来
#参数：
#    states:勾选界面的选项后，生成的0、1列表，1代表勾选，需要打开的虚拟机
#    ture_choices：列表；保存的是勾选的选项的字符串
def get_truestate(states):
    print 'states_list'
    print states 
    len_of_state_list = len(states)
    for i in range(len_of_state_list):
        for j in range(len(states[i])):
            if states[i][j] == 1:
                true_choices.append(choices[i * 2 + j])                        

#功能：找到以".vmx"结尾的文件的路径
#参数：
#    virturepath：虚拟机所在的根目录
#    vmpath:虚拟机名称也是存放".vmx"文件的上层目录
#返回值：
#    set_of_vmxfile：返回".vmx"文件所在路径
def find_virturepath(virturepath,vmpath):
    os.chdir(virturepath)
    os.chdir(vmpath)
    virture_path = os.getcwd()
    print "the virturepath**"
    print virture_path
    set_of_vmxfile = []
    file_list = []
    file_list = os.listdir(virture_path)
    file_list_count = len(file_list)
    j = 0
    while(j < file_list_count):
        onestring = file_list[j]
        find_vmxfile = onestring.split(".")
        if find_vmxfile[-1] == "vmx":
            vmxfile_abspath = os.getcwd() + "\\" + file_list[j]
            print 'vmxfile_abspath'
            print vmxfile_abspath
            set_of_vmxfile.append(vmxfile_abspath)
            return set_of_vmxfile
            break
        j= j + 1
        
#功能：将在文件中选择的路径的书写方式与当前操作系统文件路径规范
#参数：
#    tmpstring：虚拟机存放的根目录
#返回值：
#    astr：界面中返回的目录分隔符"/"替换为"\"
def strdeal(tmpstring):
    print "the tmpstring**"
    print tmpstring
    acontainer = tmpstring.split('/')  
    acont_len = len(acontainer)
    astr = acontainer[0] + "\\"    #风险点：考虑脚本在windows下运行，所以这样的文件分隔符
    for i in range(acont_len - 1):
        astr = os.path.join(astr,acontainer[i + 1])
    print "the astr**"
    print astr
    return astr

#功能：自动关闭vmware
def killVm():
    time.sleep(1300)
    command = 'taskkill /F /T /IM vmware.exe'
    os.system(command)
    time.sleep(60)

def matchStr(substr,orastr):
    print "match the string"
    matchPattern = re.compile(substr)
    if matchPattern.search(orastr):
        return True

def seperateStr(astring):
    print "将字符串分割，返回分割后的第一个子字符串："
    tmpstr = astring.split('-')
    print "打印分割后的第一个子字符串："
    print tmpstr[0]
    return tmpstr[0]

def matchDb(virsubstr,dbstr):
    print "test.."
    strlist = dbstr.split('_')
    print strlist
    subdbstr = strlist[0][0:3]
    subdbstr_int = int(subdbstr)
    db_int = subdbstr_int - 100
    if db_int == int(virsubstr):
        print db_int
        return True

#功能：打开安装了sybase、oracle数据库的虚拟机
#参数：
#    amachine：被验证数据库是否为sybase、oracle的平台虚拟机
#    machinespath：虚拟机存放的根目录
#    vmxpath:".vmx"文件所在的目录
def startDbmachine(amachine,machinespath,vmxpath):
    print "find the matched machine"
    print "***********#########*********"
    print "the index of DbMachine"
    #找到与sybase、oracle匹配的虚拟机打开
    print "the amachine**"
    print amachine
    set_amachine = amachine.split('-')
    print "the set_amachine**"
    print set_amachine
    print "the first number of set_amachine is :"
    print set_amachine[0]
    for j in range(len(Database)):
        #if matchStr(set_amachine[0],Database[j]):
        if matchDb(set_amachine[0],Database[j]):
            getdbdir = Database[j]
            print "the Database[j]:"
            print Database[j]
        else:
                continue
    print "the getdbdir**"
    print getdbdir
    getdbvmxpath = find_virturepath(machinespath,getdbdir)
    print "the getdbvmxpath value:"
    print getdbvmxpath
    os.chdir(vmxpath)
    command = "start vmware.exe -X " + '"' + getdbvmxpath[0] + '"'
    #command = "vmrun -T ws start " + '"' + getdbvmxpath[0] + '" nogui'
    os.system(command)
    time.sleep(400)
       
        #else:
            #print "go ahead!"
                  
#打开vmware虚拟机    
def start_vm(vmxfile,filepath,macnum):
    print "start_vm: "
    print true_choices
    tmppath = strdeal(filepath)
    virturepath = tmppath.strip()
    true_choices_count = len(true_choices)
    vmx_start = []   
    for i in range(true_choices_count):
        if true_choices[i] == '':
            print 'nothing'
        else:
            tmp_vmx_start = find_virturepath(virturepath,true_choices[i])
            vmx_start.append(tmp_vmx_start)
        print 'now path:'
        print os.getcwd()       
    print 'vmx_start: '
    print vmx_start
    true_choices_len = len(true_choices)
    j = 0
    while j < true_choices_len:
        print "第%d轮j的值",(j)
        print j
        print "start"
        k = j + macnum
        t = j
        if k <= true_choices_len:
            print "增量与初始值和小于外层循环之和时，查询虚拟机是否有sybase、oracle数据库："
            while t < k:
                if true_choices[t] in DbMachine:
                    print "打开sybase或oracle虚拟机："
                    substr = seperateStr(true_choices[t])
                    for m in range(len(DbMachine)):
                        print "匹配出sybase或oracle数据库："
                        if matchStr(substr,DbMachine[m]):
                            startDbmachine(DbMachine[m],virturepath,vmxpath)
                            break
                        else:
                            print "打印DbMachine此次循环的下标："
                            print m 
                else:
                    print "直接打开非sybase、oracle虚拟机"
                os.chdir(vmxpath)
                command = "start vmware.exe -X " + '"' + vmx_start[t][0] + '"'
                #command = "vmrun -T ws start " + '"' + vmx_start[t][0] + '" nogui'
                os.system(command)
                t = t + 1
        else:
            print "增量与初始值j的和大于外层循环len_vmx_start的值时，代开方式如下："
            while t < true_choices_len:
                if true_choices[t] in DbMachine:
                    print "打开sybase或oracle虚拟机："
                    substr = seperateStr(true_choices[t])
                    for m in range(len(DbMachine)):
                        print "匹配出sybase或oracle数据库："
                        if matchStr(substr,DbMachine[m]):
                            startDbmachine(DbMachine[m],virturepath,vmxpath)
                            break
                        else:
                            print "打印DbMachine此次循环的下标："
                            print m
                else:
                    print "直接打开虚拟机"
                os.chdir(vmxpath)
                command = "start vmware.exe -X " + '"' + vmx_start[t][0] + '"'
                #command = "vmrun -T ws start " + '"' + vmx_start[t][0] + '" nogui'
                os.system(command)
                t = t + 1
        killVm()
        j = k
        

#功能：读取readmachines。txt中的参数
def readParame():
    name = "#Input the name of machine"
    matchPattern = re.compile(name)
    readfile = open('readmachines.txt','r')
    while True: 
        fileline = readfile.readline()
        if not fileline:
            break
        else:
            if matchPattern.search(fileline):
                print "get the machinename:"
                ora_machinechoices = readfile.readline()
                print ora_machinechoices
    
    len_ora_machinechoices = len(ora_machinechoices)
    len_MachineChoices = len("MachineChoices = [")
    print "len-----"
    print len_ora_machinechoices
    print len_MachineChoices
    machinechoices = ora_machinechoices[len_MachineChoices:len_ora_machinechoices-2]
    print "machinechoices lalall"
    print machinechoices
    return machinechoices

#在参数文件readmachines.txt中读取字符串：AllMachine、vmx_dir、machinesdir
#参数：
#    name：需要匹配的字符串
#    filename：需要读取的文本文件名称
#    string：读取一行中的子字符串
#返回值：
#    apath：得到需要的字符串
def readPath(name,filename,string):
    matchPattern = re.compile(name)
    readfile = open(filename,'r')
    while True: 
        fileline = readfile.readline()
        if not fileline:
            break
        else:
            if matchPattern.search(fileline):
                print "get the path:"
                ora_machinespath = fileline
                print ora_machinespath
    len_ora_machinespath = len(ora_machinespath)
    len_machinedir = len(string)
    apath = ora_machinespath[len_machinedir:len_ora_machinespath - 2]
    print "now the path is:"
    print apath
    return apath

#功能：读取参数文件打开虚拟机
#参数：
#    getstring：存放虚拟机名称的列表
def startWithPara(getstring):
    astr = readPath('step_num','readmachines.txt','step_num = ')
    print "the astr value:"
    print astr
    anum = int(astr)
    print "the anum value:"
    print anum
    machinenames = getstring.split(',')
    print "from the txt:"
    print machinenames
    vmx_start = []
    len_machinenames = len(machinenames)
    print "len machinenames:"
    print len_machinenames
    for i in range(len_machinenames):
        if machinenames[i] == '':
            print 'nothing'
        else:
            tmp_vmx_start = find_virturepath(machinespath,machinenames[i])
            vmx_start.append(tmp_vmx_start)
            print "hahahahahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
            print machinespath
    print vmx_start
    len_vmx_start = len(vmx_start)
    print "the number of vmx:"
    print len_vmx_start
    j = 0
    while j < len_vmx_start:
        print "第%d轮j的值",(j)
        print j
        print "start"
        k = j + anum
        t = j
        if k <= len_vmx_start:
            print "增量与初始值和小于外层循环之和时，查询虚拟机是否有sybase、oracle数据库："
            while t < k:
                if machinenames[t] in DbMachine:
                    print "打开sybase或oracle虚拟机："
                    substr = seperateStr(machinenames[t])
                    for m in range(len(DbMachine)):
                        print "匹配出sybase或oracle数据库："
                        if matchStr(substr,DbMachine[m]):
                            startDbmachine(DbMachine[m],machinespath,vmxpath)
                            break
                        else:
                            print "打印DbMachine此次循环的下标："
                            print m 
                else:
                    print "直接打开虚拟机"
                os.chdir(vmxpath)
                command = "start vmware.exe -X " + '"' + vmx_start[t][0] + '"'
                #command = "vmrun -T ws start " + '"' + vmx_start[t][0] + '" nogui'
                os.system(command)
                t = t + 1
        else:
            print "增量与初始值j的和大于外层循环len_vmx_start的值时，代开方式如下："
            while t < len_vmx_start:
                if machinenames[t] in DbMachine:
                    print "打开sybase或oracle虚拟机："
                    substr = seperateStr(machinenames[t])
                    for m in range(len(DbMachine)):
                        print "匹配出sybase或oracle数据库："
                        if matchStr(substr,DbMachine[m]):
                            startDbmachine(DbMachine[m],machinespath,vmxpath)
                            break
                        else:
                            print "打印DbMachine此次循环的下标："
                            print m
                else:
                    print "直接打开虚拟机"
                os.chdir(vmxpath)
                command = "start vmware.exe -X " + '"' + vmx_start[t][0] + '"'
                #command = "vmrun -T ws start " + '"' + vmx_start[t][0] + '" nogui'
                os.system(command)
                t = t + 1
        killVm()
        print "此时k的值是多少："
        print k
        j = k
        print "j = k后j的值是多少："
        print j


#功能：打开所有的虚拟机
def startAllMachine():
    astr = readPath('step_num','readmachines.txt','step_num = ')
    print "the astr value:"
    print astr
    anum = int(astr)
    print "the anum value:"
    print anum
    machinespath = readPath('machinesdir','readmachines.txt','machinesdir = "')
    vmx_start = []
    print "take turns to start VM"
    len_AllMachine = len(AllMachine)
    print "len machinenames:"
    print len_AllMachine
    for i in range(len_AllMachine):
        if AllMachine[i] == '':
            print 'nothing'
        else:
            #startDbmachine(AllMachine[i],machinespath,vmxpath)
            tmp_vmx_start = find_virturepath(machinespath,AllMachine[i])
            vmx_start.append(tmp_vmx_start)
            print "hahahahahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
            print machinespath
    #len_machinespath = len(machinespath)
    print "LLen"
    #print len_machinespath
    print vmx_start
    len_vmx_start = len(vmx_start)
    print "the number of vmx:"
    print len_vmx_start
    j = 0
    while j < len_vmx_start:
        print "第%d轮j的值",(j)
        print j
        print "start"
        k = j + anum
        t = j
        if k <= len_vmx_start:
            print "增量与初始值和小于外层循环之和时，查询虚拟机是否有sybase、oracle数据库："
            while t < k:
                if AllMachine[t] in DbMachine:
                    print "打开sybase或oracle虚拟机："
                    substr = seperateStr(AllMachine[t])
                    for m in range(len(DbMachine)):
                        print "匹配出sybase或oracle数据库："
                        if matchStr(substr,DbMachine[m]):
                            startDbmachine(DbMachine[m],machinespath,vmxpath)
                            break
                        else:
                            print "打印DbMachine此次循环的下标："
                            print m
                else:
                    print "直接打开虚拟机。。" 
                os.chdir(vmxpath)
                command = "start vmware.exe -X " + '"' + vmx_start[t][0] + '"'
                #command = "vmrun -T ws start " + '"' + vmx_start[t][0] + '" nogui'
                os.system(command)
                t = t + 1
        else:
            print "增量与初始值j的和大于外层循环len_vmx_start的值时，代开方式如下："
            while t < len_vmx_start:
                if AllMachine[t] in DbMachine:
                    print "打开sybase或oracle虚拟机："
                    substr = seperateStr(AllMachine[t])
                    for m in range(len(DbMachine)):
                        print "匹配出sybase或oracle数据库："
                        if matchStr(substr,DbMachine[m]):
                            startDbmachine(DbMachine[m],machinespath,vmxpath)
                            break
                        else:
                            print "打印DbMachine此次循环的下标："
                            print m
                else:
                    print "直接打开虚拟机。。"
                os.chdir(vmxpath)
                command = "start vmware.exe -X " + '"' + vmx_start[t][0] + '"'
                #command = "vmrun -T ws start " + '"' + vmx_start[t][0] + '" nogui'
                os.system(command)
                t = t + 1
        killVm()
        print "此时k的值是多少："
        print k
        j = k
        print "j = k后j的值是多少："
        print j 
    
#功能：gui方式打开指定虚拟机        
def startWithGui():
    root = Tk()
    root.withdraw()
    root.title("autoinstall")
    vmx_file,machine,macnum = packDialog()
    print "打印小窗口返回的值"
    print vmx_file
    print machine
    print macnum

    top1frame = Frame(root)
    top1frame.pack(side = TOP)
    lab = Label(top1frame,text = '选择需要打开的虚拟机:')
    lab.pack(fill = X)
    
    topframe = Frame(root)
    topframe.pack(side =TOP)

    bottomframe = Frame(root)
    bottomframe.pack(side =BOTTOM)
    
    oneline = Checkbar(bottomframe, ['1-win8-32-zh','2-win7-32-en'])
    twoline = Checkbar(bottomframe, ['7-win8-64-en','8-win7-64-zh'])
    threeline = Checkbar(bottomframe, ['10-win2k8-64-df','11-RedHat5.4-x64-df'])
    fourline = Checkbar(bottomframe, ['13-RedHat6.4-x32-df','14-win8-32-TW'])
    fiveline = Checkbar(bottomframe, ['15-win7-32-en','16-win2k3-32-zh'])
    sixline = Checkbar(bottomframe, ['18-RedHat5.4-x32-zh','19-RedHat6.4-x32-TW'])
    sevenline = Checkbar(bottomframe, ['20-SUSE11-x32-df','21-win8-32-hk'])
    eightline = Checkbar(bottomframe, ['22-win7-32-TW','23-win2k3-32-en'])
    nineline = Checkbar(bottomframe, ['25-win2k8-64-en','26-RedHat5.4-x64-zh'])
    tenline = Checkbar(bottomframe, ['29-win8-64-df','30-win2k3-64-TW'])
    elevenline = Checkbar(bottomframe, ['33-RedHat5.4-x32-en','34-RedHat6.4-x32-zh'])
    twelveline = Checkbar(bottomframe, ['35-SUSE11-x32-zh','36-win8-32-en'])
    thirteenline = Checkbar(bottomframe, ['37-win7-32-df','38-win7-64-TW'])
    fourteenline = Checkbar(bottomframe, ['39-win2k3-64-df','41-SUSE11-x64-zh'])
    fifteenline = Checkbar(bottomframe, ['42-win8-64-hk'])
    
    oneline.pack(side = TOP,fill = X)
    twoline.pack(side = TOP,fill = X)
        
    threeline.pack(side = TOP,fill = X)
    fourline.pack(side = TOP,fill = X)
    
    fiveline.pack(side = TOP,fill = X)
    sixline.pack(side = TOP,fill = X)
    
    sevenline.pack(side = TOP,fill = X)
    eightline.pack(side = TOP,fill = X)
    
    nineline.pack(side = TOP,fill = X)
    tenline.pack(side = TOP,fill = X)
    
    elevenline.pack(side = TOP,fill = X)
    twelveline.pack(side = TOP,fill = X)
    
    thirteenline.pack(side = TOP,fill = X)
    fourteenline.pack(side = TOP,fill = X)
    
    fifteenline.pack(side = TOP,fill = X)
    
    choices.append(oneline)
    choices.append(twoline)
    root.update()
    root.deiconify()
    
    print '******************'
    print choices
    print '******************'

    def allstates(): 
        state_list = list(oneline.state()), list(twoline.state()), list(threeline.state()), list(fourline.state()), list(fiveline.state()), list(sixline.state()), list(sevenline.state()), list(eightline.state()), list(nineline.state()), list(tenline.state()), list(elevenline.state()), list(twelveline.state()), list(thirteenline.state()), list(fourteenline.state()), list(fifteenline.state())
        #len_of_state_list = len(state_list)
        
        get_truestate(state_list)

        start_vm(vmx_file,machine,macnum)
            
    Quitter(bottomframe).pack(side=RIGHT)
    Button(bottomframe, text='Sure', command=allstates).pack(side=RIGHT)
    
    root.mainloop()

if __name__ == '__main__':
    getstring = readParame()
    print "the getstring is lllllllllllllll"
    print getstring
    vmxpath = readPath('vmx_dir','readmachines.txt','vmx_dir = "')
    machinespath = readPath('machinesdir','readmachines.txt','machinesdir = "')
    stateAllMach = readPath('AllMachine','readmachines.txt','AllMachine = "')    
    if stateAllMach == "True":
        print "Starting all Machines................................."
        startAllMachine()
    else:
        if getstring:
            print "Starting with Parameter..............................."
            startWithPara(getstring)
            print "debugtime..."
        else:
            print "Starting with GUI....................................."
            startWithGui()
    
    
    
    
    
    
    
