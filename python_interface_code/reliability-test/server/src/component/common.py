# coding: utf-8
import os
import time
import json
import string
import random
import datetime
import ConfigParser
import traceback
import public.httpmethod
from public.LogMethod import mlogger
from public.data2html import *
report = HtmlReport("中国人寿", '二期', debug=True)
PASS = 'pass'
FAIL = 'fail'
result_list = []
headers = {'content-type': 'application/json'}
YESTERDAY = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
TODAY = time.strftime("%Y-%m-%d", time.localtime())
TOMORROW = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")


subfix = string.join(random.sample('abcdefghijklmnopqrstuvwxyz12345678901234567890', 5)).replace(' ', '')
CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
ROOT_PATH = os.path.dirname(os.path.dirname(CURRENT_PATH))
STUFF_DIR = os.path.join(ROOT_PATH, 'stuff')
config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join(ROOT_PATH, 'config.ini')))
bs3url = 'http://' + config.get('urlconfig', 'bs3url')
sceurl = 'http://' + config.get("urlconfig", "sceurl")
sccurl = 'http://' + config.get("urlconfig", "sccurl")
scburl = 'http://' + config.get("urlconfig", "scburl")
scqurl = 'http://' + config.get("urlconfig", "scqurl")
scsurl = 'http://' + config.get("urlconfig", "scsurl")
scaurl = 'http://' + config.get("urlconfig", "scaurl")
scaurl_https = 'https://' + config.get("urlconfig", "scaurl_https")
scwurl = 'http://' + config.get("urlconfig", "scwurl")
mongoip = config.get("urlconfig", "mongoip")
scw_version = config.get("urlconfig", "scw_version")
scs_version = config.get("urlconfig", "scs_version") # 2017-08-11

normal_idcard = config.get("urlconfig", "normal_idcard")
normal_phone = config.get("urlconfig", "normal_phone")
normal_name = config.get("urlconfig", "normal_name")
vip_idcard = config.get("urlconfig", "vip_idcard")
vip_phone = config.get("urlconfig", "vip_phone")
vip_name = config.get("urlconfig", "vip_name")
upgrade_md5 = config.get('urlconfig', 'upgrade_md5')
newphone = '15100030003'
office_idpath = config.get("urlconfig", "office_idpath")
officeid = office_idpath.split('.')[-2]
city_idpath = office_idpath[: office_idpath.index(officeid)]
cityid = city_idpath.split('.')[-2]
province_idpath = office_idpath[: office_idpath.index(cityid)]


def newidcard():
    return string.join(random.sample('1234567890123456789012345678901234567890', 18)).replace(' ', '')

def login():
    url = scsurl + "/api/v1/user/me"
    data = {"name": "root", "password": "U2FsdGVkX1+hS6Nm+32qTL7HJrijCF7NcuSj2nWVAgA="}
    try:
        code, response = public.httpmethod.Post(url, json.dumps(data), headers)
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result('login', '登录柜面平台', url, response, result, data)

def get_province():
    url = scsurl + '/api/v1/settings/offices/{}'
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result("get_province", '获取组织结构', url, response, result)
    response = json.loads(response)
    return get_node_by_id(response[0], 'province', province_idpath)


def get_node_by_id(parent, node_type=None, node_idpath=None):
    for node in parent['children']:
        if node['type'] == node_type and node['idpath'] == node_idpath:
            return node
    mlogger.error('组织结构type=%s _id=%s not found!' % (node_type, node_idpath))


def get_office_business(filter_isvip=None):
    url = scsurl + '/api/v1/settings/business/{"office_path":"%s"}' % office_idpath
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result("get_office_business", '获取营业厅业务列表', url, response, result)
    result = json.loads(response)
    bss = result[0]['businesses']
    if filter_isvip is None:
        return bss
    else:
        for bs in bss:
            if bs['isvip'] == filter_isvip:
                log = '选择业务:    ' + bs['name']
                mlogger.info(log)
                return bs
        mlogger.warn('没有匹配的业务')


def get_office_window():
    url = scsurl + '/api/v1/settings/window/{"office_id":%s}' % officeid
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result("get_office_window", '获取营业厅窗口列表', url, response, result)
    result = json.loads(response)
    return result[0]


def get_office_teller():
    url = scsurl + '/api/v1/settings/teller/{"filterKey":"code","idpath":"%s"}' % office_idpath
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result("get_office_teller", '获取营业厅柜员列表', url, response, result)
    result = json.loads(response)
    return result[0]


def get_officeconf():
    url = scsurl + "/api/v1/settings/officeconf/" + str(officeid)
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result('get_officeconf', '获取营业厅配置 ', url, response, result)
    result = json.loads(response)
    return result


def API_SCS_OFFICE_GET():
    randomstr = ('abcdefghijklmnopqrstuvwxyz0123456789' + 'abcdefghijklmnopqrstuvwxyz0123456789')
    md5 = string.join(random.sample(randomstr, 32)).replace(' ', '')
    url = scsurl + '/api/v1/office?officeid=%s&confmd5=%s&warnrulesmd5=%s&' \
                   'businessesmd5=%s&windowsmd5=%s&tellersmd5=%s&sccconfmd5=%s&sctconfmd5=%s' % (
                    officeid, md5, md5, md5, md5, md5, md5, md5)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result('API_SCS_OFFICE_GET', '获取指定营业厅的配置', url, response, result)
    result = json.loads(response)
    return result


def API_SCQ_TELLER_LOGINSTATUS():
    url = scqurl + '/api/v1/teller/loginstatus'
    data = {"username": teller['code'], "pwd": teller['password'], "windowid": window['_id'],
            "status": "login"}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result('API_SCQ_TELLER_LOGINSTATUS', '柜员登录', url, response, result)
    result = json.loads(response)
    return result


def add_numberrule():
    login()
    data = {'officeId': int(officeid), 'noDelay': True}
    bmap = dict()
    response = None
    result = None
    for cb in businesses:
        businesses_id = cb['_id']
        data_temp1 = []
        for j in range(0, 7):
            data_temp1.append({
                "office_id": int(officeid),
                "week": str(j),
                "business_id": businesses_id,
                "name": cb['name'],
                "worktimes": [{"start": "", "end": "", "interval": 30, "wechatnumber": 30, "rainbownumber": 10}]
            })
        bmap[businesses_id] = data_temp1
    data['data'] = bmap
    try:
        url = scsurl + "/api/v1/settings/check/numberrule"
        code, response = public.httpmethod.Post(url, json.dumps(data), headers)
        assert code == 200
        # headers['Accept'] = "application/json, text/plain, */*"
        # headers['Content-Type'] = "application/json;charset=utf-8"
        url = scsurl + "/api/v1/settings/numberrule"
        code, response = public.httpmethod.Post(url, json.dumps(data), headers)
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('add_numberrule', '新增号源 ', url, response, result, data)
    # url = scsurl + '/api/v1/settings/numberrule/%7B%22office_id%22:' + str(officeid) + '%7D'
    # code, response = public.httpmethod.Get(url)
    # try:
    #     assert code == 200
    #     response = json.loads(response)
    #     assert result['errcode'] == 0
    #     result = PASS
    # except:
    #     result = FAIL
    #     mlogger.error(traceback.format_exc())
    # finally:
    #     log_result('add_numberrule', '查询号源 ', url, response, result)


def redis():
    url = scsurl + '/api/v1/redis'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result('redis', 'redis同步', url, response, result)


def get_comment(response):
    if isinstance(response, list):
        return ''
    if isinstance(response, dict):
        return response['errmsg'] if 'errcode' in response.keys() and response['errcode'] != 0 else ''
    if isinstance(response, str):
        if response == 'OK':
            return ''
        elif response.startswith('{'):
            response = json.loads(response)
            try:
                return response['errmsg'] if 'errcode' in response.keys() and response['errcode'] != 0 else ''
            except:
                return response
        elif response.startswith('['):
            return ''
    else:
        return '返回异常'


def log_result(api, desc, url, response, result=FAIL, data=None, **kwargs):
    try:
        myresult = dict()
        myresult['id'] = api
        myresult['description'] = desc
        myresult['url'] = url
        myresult['data'] = data
        myresult['result'] = result
        myresult['comment'] = kwargs['comment'] if kwargs and 'comment' in kwargs.keys() else get_comment(response)
        if data is not None and str(data).startswith('{'):
            data = json.dumps(data, ensure_ascii=False)
        if str(response).startswith('<'):
            myresult['response'] = str(response).replace('<', '').replace('>', '')
        else:
            myresult['response'] = response
        report.add_record(myresult)
    except:
        mlogger.error(traceback.format_exc())


def start_scq():
    import paramiko
    ssh_port = 22
    ssh_name = 'root'
    ssh_pwd = 'root1234'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(scqurl[7:-5], ssh_port, ssh_name, ssh_pwd)
    exec_ssh(ssh, "cmd /c start C:\Starnet\SCQ\SCQ.exe")  # 启动排队服务软件


def printjson(obj):
    mlogger.info(json.dumps(obj, ensure_ascii=False))


'''使用已存在的office'''
login()
province = get_province()
city = get_node_by_id(province, 'city', city_idpath)
office = get_node_by_id(city, 'office', office_idpath)
officeinfo = API_SCS_OFFICE_GET()
teller = get_office_teller()
teller_user = teller['code']
teller_pwd = teller['password']
window = get_office_window()
businesses = get_office_business()
vipbusiness = get_office_business(True)
business = get_office_business(False)
officeconfid = get_officeconf()['_id']
tellerinfo = API_SCQ_TELLER_LOGINSTATUS()['teller']
redis()

operations = [
    {'idcard': newidcard(), 'phone': newphone, 'business': business},
    {'idcard': vip_idcard, 'phone': vip_phone, 'business': vipbusiness},
    {'idcard': vip_idcard, 'phone': vip_phone, 'business': business},
    {'idcard': normal_idcard, 'phone': normal_phone, 'business': business}
]


def exec_ssh(ssh, cmd):
    if cmd.startswith('cmd'):
        coding = 'gbk'
    else:
        coding = 'utf8'
    mlogger.debug(cmd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    mlogger.debug(stdout.read(), coding)
    mlogger.debug(stderr.read(), coding)