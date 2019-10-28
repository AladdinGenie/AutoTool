# -*- encoding: utf-8 -*-
import ConfigParser
import os
import sys
from xml.etree import ElementTree
import paramiko
from public.LogMethod import mlogger as mlogger
from pymongo import MongoClient
import json
CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
ROOT_PATH = os.path.dirname(CURRENT_PATH)
reload(sys)
sys.setdefaultencoding('utf-8')
ssh_port = 22
ssh_name = 'root'
ssh_pwd = 'root1234'


def printjson(obj):
    mlogger.info(json.dumps(obj, ensure_ascii=False))


class _Methods(object):
    def __init__(self):
        '''配置文件读取，配置文件为config.ini，放在上一级目录下'''
        config = ConfigParser.ConfigParser()
        config.readfp(open(os.path.join(ROOT_PATH, 'config.ini')))
        self.scqurl = 'http://' + config.get("urlconfig", "scqurl")
        self.scsurl = 'http://' + config.get("urlconfig", "scsurl")
        self.scwurl = 'http://' + config.get("urlconfig", "scwurl")
        self.mongoip = config.get("urlconfig", "mongoip")
        self.scw_version = config.get("urlconfig", "scw_version")
        self.provinceid = config.get("urlconfig", "province_idpath")

    ''' 
    def get_apiurl_officeid(self):
        client = MongoClient(self.mongoip,27017)
        titles = client['smartcountserver']['apiurls']
        rows = titles.find({'name':'福建接口'})
        ori_officeid = rows[0]['office_id']
        client.close()
        return  ori_officeid         
    
    def set_apiurl_officeid(self,provinceid):
        mlogger.info('\n\n--------------------------设置接口：北京--------------------------\n')
        mlogger.info('设置省份ID：'+str(provinceid))
        client = MongoClient(self.mongoip,27017)
        titles = client['smartcountserver']['apiurls'] 
        titles.update({'name':'福建接口'},{'$set':{'office_id':provinceid}}, False,False)
#         titles.update({'name':'福建接口'},{'$set':{'url':'http://192.168.96.69:1418'}}, False,False)    
        client.close()
        pass
    '''

    def clear_db_offices(self):
        client = MongoClient(self.mongoip, 27017)
        offices = client['smartcountserver']['offices']
        office_ids = self.get_overtime_officeids()
        for o_id in office_ids:
            offices.remove({'_id':o_id})

    def get_overtime_officeids(self):
        client = MongoClient(self.mongoip, 27017)
        offices = client['smartcountserver']['offices']
        office_ids = []
        for u in offices.find({'idpath': {"$regex": u"^%s*" % self.provinceid}}):
            if u['idpath'] != self.provinceid:
                office_ids.append(u['_id'])
        return office_ids

    def clear_db_tables_by_officeid(self):
        table_key = {
            'windows': 'office_id',
            'plays': '_id',
            'numberrules': 'office_id',
            'businesses': 'office_id',
            'baseconfs': 'office_id',
            'officeconfs': 'office_id',
            'appointments': 'o_id',
            'appointmentdaylogs': 'o_id',
            'officedaylogs': 'o_id',
            'officemonthlogs': 'o_id',
            'officeyearlogs': 'o_id',
            'telleryearlogs': 'o_id',
            'telleronlinelogs': 'o_id',
            'tellermonthlogs': 'o_id',
            'tellerdaylogs': 'o_id',
            'versionrecords': 'o_id',
            'officeevaluates': 'o_id',
            'businessdetaillogs': 'o_id'
        }
        client = MongoClient(self.mongoip, 27017)
        office_ids = self.get_overtime_officeids()
        for t, key in table_key.items():
            table = client['smartcountserver'][t]
            for officeid in office_ids:
                mlogger.info('--------------------------清除表: %s ------------------------' % t)
                table.remove({key: officeid})
        client.close()

    def clear_db_tellers(self):
        client = MongoClient(self.mongoip, 27017)
        offices = client['smartcountserver']['offices']
        idpaths = []
        for u in offices.find({'idpath': {"$regex": u"^%s*" % self.provinceid}}):
            if u['idpath'] != self.provinceid:
                idpaths.append(u['idpath'])
        table = client['smartcountserver']['tellers']
        for tt in idpaths:
            table.remove({'code': '10001'})

    def clear_wechat(self):
        client = MongoClient(self.mongoip, 27018)
        office_ids = self.get_overtime_officeids()
        table_key = {
            'appointments': 'noi',
            'numbersources': 'noi',
            'offices': '_id'
        }
        for t, key in table_key.items():
            table = client['smartcounterwechat'][t]
            for officeid in office_ids:
                mlogger.info('--------------------------清除表: %s ------------------------' % t)
                table.remove({key: officeid})
        client.close()

    def start_scq(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.scqurl[7:-5], ssh_port, ssh_name, ssh_pwd)
        self.exec_ssh(ssh, "cmd /c start C:\Starnet\SCQ\SCQ.exe")  # 启动排队服务软件

    def restart_scq(self, city, office):
        mlogger.info('\n\n--------------------------重启  SCQ 开始--------------------------\n')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.scqurl[7:-5], ssh_port, ssh_name, ssh_pwd)
        sftp = ssh.open_sftp()
        self.exec_ssh(ssh, "cmd /c taskkill /F  /IM SCQ.exe /T")  # 关闭排队服务软件进程
        dmbconfig = 'SCQ' + os.sep + 'DmbConfig.xml'
        tmp = 'DmbConfig.xml'
        sftp.get(dmbconfig, tmp)  # 获取排队服务软件配置文件
        xmldoc = ElementTree.parse(tmp)
        xmldoc.find('SCSAddress').text = self.scsurl  # 设置柜面平台地址
        xmldoc.find('Office').set('officeid', str(office['_id']))  # 设置营业厅ID
        xmldoc.find('Office').set('cityname', str(city['name']))  # 设置城市名称
        xmldoc.find('Office').text = office['name']  # 设置营业厅名称
        xmldoc.write(tmp, encoding="utf-8", xml_declaration=True)
        sftp.put(tmp, dmbconfig)
        self.exec_ssh(ssh, "cmd /c start C:\Starnet\SCQ\SCQ.exe")  # 启动排队服务软件
        mlogger.info('\n\n--------------------------重启  SCQ 结束--------------------------\n')

    def restart_scc(self, city, office, window, mode='caller'):
        mlogger.info('\n\n--------------------------重启  SCC 开始--------------------------\n')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.scqurl[7:-5], ssh_port, ssh_name, ssh_pwd)
        sftp = ssh.open_sftp()
        self.exec_ssh(ssh, "cmd /c taskkill /F  /IM SCC.exe /T")  # 关闭叫号软件进程
        dmbconfig = 'SCC\\config.xml'
        tmp = 'config.xml'
        sftp.get(dmbconfig, tmp)  # 获取叫号软件配置文件
        xmldoc = ElementTree.parse(tmp)
        xmldoc.find('SCSServerDomain').text = self.scsurl[7:-5]
        xmldoc.find('SCSServerIp').text = self.scsurl[7:-5]  # 设置柜面平台地址
        xmldoc.find('SCSServerPort').text = self.scsurl[-4:]  # 设置柜面平台端口
        xmldoc.find('SCQServerIp').text = self.scqurl[7:-5]  # 设置排队服务软件地址
        xmldoc.find('SCQServerPort').text = self.scqurl[-4:]  # 设置排队服务软件端口
        xmldoc.find('VerType').text = 'chinalife'  # 设置为人寿版本
        xmldoc.find('Window').set('officeId', str(office['_id']))  # 设置营业厅ID
        xmldoc.find('Window').set('officeName', office['name'])  # 设置营业厅名称
        xmldoc.find('Window').set('name', window['name'])  # 设置窗口名称
        xmldoc.find('Window').set('city', city['name'])  # 设置城市名称
        xmldoc.find('Window').set('id', window['_id'])  # 设置窗口ID
        xmldoc.find('VerMode').text = mode  # 运行模式:caller:叫号软件模式,evaluation:评价器模式
        xmldoc.write(tmp, encoding="utf-8", xml_declaration=True)
        sftp.put(tmp, dmbconfig)
        self.exec_ssh(ssh, "cmd /c start C:\Starnet\SCC\SCC.exe -u 10001 -p 1111111a -w " + window[
            '_id'] + " -noupdate")  # 启动叫号软件
        ssh.close()
        mlogger.info('\n\n--------------------------重启  SCC 结束--------------------------\n')
        pass

    def exec_ssh(self, ssh, cmd):
        if cmd.startswith('cmd'):
            coding = 'gbk'
        else:
            coding = 'utf8'
        mlogger.debug(cmd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        mlogger.debug(stdout.read(), coding)
        mlogger.debug(stderr.read(), coding)
        pass

    def restart_smartcounterwechat(self):
        mlogger.info('\n\n--------------------------重启微信后台：开始--------------------------\n')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.scwurl[7:-5], 22, "root", "123456")
        commands = "source /etc/profile;cd /scs/smartcounterserver-smartcounterwechat-" + self.scw_version + \
                   ";./stop-docker.sh;./docker-run.sh"
        self.exec_ssh(ssh, commands)
        ssh.close()
        mlogger.info('\n\n--------------------------重启微信后台：结束--------------------------\n')
        pass
