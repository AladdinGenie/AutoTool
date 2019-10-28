# coding: utf-8
import public.httpmethod
from common import *
from scs import API_SCS_TICKET_AUTH
import unittest



# 1
def API_SCQ_TELLER_LOGINSTATUS():
    url = scqurl + '/api/v1/teller/loginstatus'
    data = {"username": teller['code'], "pwd": teller['password'], "windowid": window['_id'],
            "status": "login"}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_TELLER_LOGINSTATUS', '柜员登录', url, response, result)

# 2
def API_SCQ_BUSINESS_GET():
    url = scqurl + '/api/v1/business/scc'
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_BUSINESS_GET', '获取营业厅内所有业务列表', url, response, result)
    result = json.loads(response)
    return result

# 3
def API_SCQ_MANAGER_POST():
    url = scqurl + '/api/v1/manager'
    data = {"windowid": window['_id'], "tellercode": teller['code']}
    try:
        code, response = public.httpmethod.Post(url, json.dumps(data), headers)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_MANAGER_POST', '呼叫柜面经理', url, response, result)

# 4
def API_SCQ_WINDOW_SAVE():
    url = scqurl + '/api/v1/window'
    data = {"windowid": window['_id'], "name": window['name'], 'windowboxmac': '007001000d00',
            "callerip": sccurl[7:-5], "callerport": sccurl[-4:],
            "boxip": scburl[7:-5], "boxport": scburl[-4:],
            "windowboxip": sceurl[7:-5], "windowboxport": sceurl[-4:],
            "ledip": "192.168.65.183", "ledscreennum": 102}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_WINDOW_SAVE', '保存窗口信息', url, response, result, data)

# 5
def API_SCQ_OFFICEWAITCOUNT_GET():
    url = scqurl + '/api/v1/office/waitcount'
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_OFFICEWAITCOUNT_GET', '13.获得营业厅等待人数', url, response, result)

# 6
def API_SCQ_OFFICEWAITDETAIL_GET():
    url = scqurl + '/api/v1/office/waitdetail'
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_OFFICEWAITDETAIL_GET', '获得营业厅等待详情', url, response, result)

# 7
def API_SCQ_HEARTBEAT_PUT():
    url = scqurl + '/api/v1/heartbeat/' + str(window['_id'])
    code, response = public.httpmethod.Put(url, None, headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_HEARTBEAT_PUT', '心跳消息', url, response, result)

# 8
def API_SCQ_TICKET_RECALL_POST():
    url = scqurl + '/api/v1/ticket/recall'
    data = {"ticketnumber": "1001", "windowid": window['_id']}
    code, response = public.httpmethod.Post(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_TICKET_RECALL_POST', '重呼', url, response, result, data)

# 9
def API_SCQ_STUFF_POST():
    url = scqurl + '/api/v1/stuff/playlist'
    data = {"md5": string.join(random.sample('12345678901234567890', 16)).replace(' ', ''),
            "data": [{
                "filename": "playShow",
                "play": {"cmd": "ALL", "key": [],
                         "records": [{"stuff": "/stufflib/IMAGE/3e20b41f97836e43b9f5d13fab964397.png"}]}
            }]
            }
    code, response = public.httpmethod.Post(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_STUFF_POST', '通知排队服务软件发送播放内容信息到评价软件', url, response, result, data)

# 10
def API_SCQ_LOG_GET():
    url = scqurl + '/log/SCQ.log'
    code, response = public.httpmethod.getcode(url)
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_LOG_GET', '下载排队服务软件日志文件', url, response, result, code)

# 11
def API_SCQ_SCTLOG_GET():
    url = scqurl + '/sct/log/SCT.log'
    code, response = public.httpmethod.getcode(url)
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_SCTLOG_GET', '下载取号软件日志文件', url, response, result, code)

# 12
def API_SCQ_BOXIP_SAVE():
    url = scqurl + '/api/v1/box'
    data = {"boxmac": "000002000002", "boxno": "BOX00001", "boxip": "192.168.66.45", "boxport": "60003"}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_BOXIP_SAVE', '保存嵌入式终端IP', url, response, result, data)

# 13
def API_SCQ_OFFICEWINDOWLIST_GET():
    url = scqurl + '/api/v1/windowlist'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_OFFICEWINDOWLIST_GET', '获得营业厅窗口列表', url, response, result)

# 14
def API_SCQ_MONITOR_GET():
    url = scqurl + '/api/v1/monitor'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_MONITOR_GET', '监控营业厅状态', url, response, result)

# 15
def API_SCQ_WINDOW_STATUS():
    url = scqurl + '/api/v1/window/status'
    data = {"status": "stop", "windowid": window['_id']}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_WINDOW_STATUS', '上报窗口状态（暂停、启用）', url, response, result, data)

# 16
def API_SCQ_NOTIFIED_UPGRADE_PUT():
    url = scqurl + '/api/v1/upgrade/version'
    data = {"scqhref": "/scq/xxxx/xx.xml",
            "scthref": "/sct/xxxx/xx.xml",
            "scchref": "/scc/xxxx/xx.xml"}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_NOTIFIED_UPGRADE_PUT', 'SCS通知SCQ升级软件', url, response, result, data)

# 17
def API_SCQ_NEEDED_UPGRADE_GET():
    url = scqurl + '/api/v1/upgrade/version/scc/121312435425'
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_NEEDED_UPGRADE_GET', 'SCT、SCC向SCQ验证软件版本是否需要升级', url, response, result)

# 18
def API_SCQ_DOWNLOAD_UPGRADEFILE_GET():
    url = scqurl + '/api/v1/upgrade/download/scc/upgrade.xml'
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_DOWNLOAD_UPGRADEFILE_GET', '下载软件升级文件', url, response, result)

# 19
def API_SCQ_REPORT_UPGRADE_RESULT_PUT():
    url = scqurl + '/api/v1/upgrade/result'
    data = {
        'type': "SCC",
        'md5': "xxxxxxxxxxxxx",
        'version': "xx.xx.xx.xx",
        'time': TODAY + " 17:49:50"
    }
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_REPORT_UPGRADE_RESULT_PUT', '上报升级结果', url, response, result, data)

# 20
def API_SCQ_OFFICE_GET():
    url = scqurl + '/api/v1/office'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_OFFICE_GET', '获取营业厅基本信息', url, response, result)

# 21
def API_SCQ_RUNNING_STATUS_GET():
    url = scqurl + '/api/v1/runningstatus'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_RUNNING_STATUS_GET', '获取营业厅各个模块运行状态', url, response, result)

# 22
def API_SCQ_TRANSPOND_TO_COUNTER():
    url = scqurl + '/tspdctr/api/v1/offices'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_TRANSPOND_TO_COUNTER', '消息转发到柜面的通用接口', url, response, result)

# 23
def API_SCQ_SYSLOGS_GET():
    url = scqurl + '/api/v1/syslogs/scq'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        assert isinstance(response, list)
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_SYSLOGS_GET', '获取SCQ日志', url, response, result, code)

    url = scqurl + '/api/v1/syslogs/sct'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_SYSLOGS_GET', '获取SCT日志', url, response, result, code)

    url = scqurl + '/api/v1/syslogs/scc/%s' % window['name']
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        assert isinstance(response, list)
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_SYSLOGS_GET', '获取SCC日志', url, response, result, code)

# 24
def API_SCQ_TELLER_GET():
    url = scqurl + '/api/v1/teller/%s' % window['_id']
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_TELLER_GET', '获取员工牌信息', url, response, result)

# 25
def API_SCQ_TELLER_PUT():
    url = scqurl + '/api/v1/office'
    data = {
        "tellerid": teller['_id'],
        "code": teller['code'],
        "name": teller['name'],
        "photoname": teller['phototmp'],
        "sex": teller['sex'],
        "level": teller['level'],
        "password": teller['password'],
    }
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_TELLER_PUT', '更新柜员', url, response, result)

# 26
def API_SCQ_CUSTOMERRECORD_LIST_GET():
    url = scqurl + '/api/v1/customerrecords/' + teller['code']
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_CUSTOMERRECORD_LIST_GET', '获取客户登记信息列表', url, response, result)

# 27
def API_SCQ_ORDER_LIST_GET():
    url = scqurl + '/api/v1/policy?policyno=10001&officeid=' + str(officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_ORDER_LIST_GET', '查询保单列表', url, response, result)

# 28
def API_SCQ_QUEUE_GET():
    url = scqurl + '/api/v1/queue'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_QUEUE_GET', '获取客户排队详情', url, response, result)

# 29
def API_SCQ_MYCUSTOMER_LIST_GET():
    url = scqurl + '/api/v1/sellercus?sellerno=10001&officeid=' + str(officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_MYCUSTOMER_LIST_GET', '获取客户列表', url, response, result)

# 30
def API_SCQ_MYORDER_LIST_GET():
    url = scqurl + '/api/v1/sellerpolicy?&sellerno=10001&sdate=20150101&edate=20150302&officeid=' + str(
        officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_MYORDER_LIST_GET', '我的保单—已生效的保单', url, response, result)

# 31
def API_SCQ_MYAPPLYORDER_LIST_GET():
    url = scqurl + '/api/v1/sellerapplypolicy?&sellerno=10001&sdate=20150101&edate=20150301&officeid=' + str(
        officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_MYAPPLYORDER_LIST_GET', '我的保单—已申请的保单', url, response, result)

# 32
def API_SCQ_CALLER_IP_PORT_GET():
    url = scqurl + '/api/v1/caller/' + window['_id']
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_CALLER_IP_PORT_GET', '获取叫号器IP配置信息 ', url, response, result)

# 33
def API_SCQ_OFFICE_PUT(data=officeinfo):
    url = scqurl + '/api/v1/office'
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_OFFICE_PUT', '更新营业厅配置', url, response, result, data)

# 34
def API_SCQ_CUSTOMER_GET(idcard=normal_idcard):
    url = scqurl + '/api/v1/customer?idcard=' + idcard + '&officeid=' + str(officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_CUSTOMER_GET', '查询客户信息', url, response, result)

# 35
def API_SCQ_CUSTOMERRECORD_SUBMIT(idcard=normal_idcard):
    url = scqurl + '/api/v1/customerrecord'
    data = {"businessname": business['name'], "name": normal_name, "idcard": idcard,
            "telephone": "19850429084", "address": "", "salary": "", "isnew": False,
            "buyproducts": [{"productname": "A", "buypercent": "28%"},
                            {"productname": "B", "buypercent": "50%"}],
            "operatorid": teller['code'], "updatetime": TODAY, "remark": ""}
    code, response = public.httpmethod.Post(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_CUSTOMERRECORD_SUBMIT', '登记客户信息', url, response, result, data)

# 36
def API_SCQ_CUSTOMERRECORD_GET(idcard=normal_idcard):
    url = scqurl + '/api/v1/customerrecord/' + idcard
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_CUSTOMERRECORD_GET', '获取客户登记信息', url, response, result)

# 37
def API_SCQ_CUSTOMER_OF_NAME_GET(name='%E5%BC%A0%E4%B8%89'):  # name='%E5%BC%A0%E4%B8%89'
    url = scqurl + '/api/v1/customers?name=' + name + '&officeid=' + str(officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_CUSTOMER_OF_NAME_GET', '根据客户姓名获取客户列表', url, response, result)


def API_SCQ_TICKET_ADD(pbusiness=business, idcard=newidcard(), number=None):  # idcard是必须的参数
    url = scqurl + '/api/v1/ticket'
    data = {'idcard': idcard, "type": "local"}
    if pbusiness:
        data['businessid'] = pbusiness['_id']
    if number:
        data['appointmentnumber'] = number
        data['idcard'] = idcard
    try:
        code, response = public.httpmethod.Post(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_TICKET_ADD', '取票 ', url, response, result, data)
        return response


def API_SCQ_TICKET_STATUS_PUT(ticketid, stat):
    url = scqurl + '/api/v1/ticket'
    data = {"ticketid": ticketid, "windowid": window['_id'], "tellercode": teller['code'],
            "ticketstatus": stat}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_TICKET_STATUS_PUT', '票状态更新: ' + stat, url, response, result, data)


def API_SCQ_EVALUATION_PUT(ticketid, value=''):
    url = scqurl + '/api/v1/ticket/evaluation'
    data = {"type": "scc", "value": str(value), "ticketid": ticketid}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    tag = '请求评价' if value == '' else '评价结果上报'
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_EVALUATION_PUT', tag, url, response, result, data)


def API_SCQ_REQUEST_WELCOME(ticketid):
    url = scqurl + '/api/v1/ticket/welcome'
    data = {"ticketid": ticketid, 'windowid': window['_id']}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_REQUEST_WELCOME', '请求欢迎', url, response, result, data)


def API_SCQ_TICKET_TRANSFER(ticketid, frombusiness, tobusiness):
    url = scqurl + '/api/v1/ticket/business'
    data = {"ticketid": ticketid, "frombusinessid": frombusiness['_id'], "tobusinessid": tobusiness['_id']}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_TICKET_TRANSFER', '票业务转移', url, response, result, data)


def API_SCQ_IDCARD_BIND(ticketid):
    url = scqurl + '/api/v1/ticket/idcard'
    data = {"ticketid": ticketid, "idcards": vip_idcard}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers={'Content-Type': 'text/plain'})
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCQ_IDCARD_BIND', '更新票的身份证号码', url, response, result, data)


def test_scq_api():
    API_SCQ_TELLER_LOGINSTATUS()
    API_SCQ_BUSINESS_GET()
    API_SCQ_MANAGER_POST()
    API_SCQ_WINDOW_SAVE()
    API_SCQ_OFFICEWAITCOUNT_GET()
    API_SCQ_OFFICEWAITDETAIL_GET()
    API_SCQ_HEARTBEAT_PUT()
    API_SCQ_TICKET_RECALL_POST()
    API_SCQ_STUFF_POST()
    API_SCQ_LOG_GET()
    API_SCQ_SCTLOG_GET()
    API_SCQ_BOXIP_SAVE()
    API_SCQ_OFFICEWINDOWLIST_GET()
    API_SCQ_MONITOR_GET()
    API_SCQ_WINDOW_STATUS()
    API_SCQ_NOTIFIED_UPGRADE_PUT()
    API_SCQ_NEEDED_UPGRADE_GET()
    API_SCQ_DOWNLOAD_UPGRADEFILE_GET()
    API_SCQ_REPORT_UPGRADE_RESULT_PUT()
    API_SCQ_OFFICE_GET()
    API_SCQ_RUNNING_STATUS_GET()
    API_SCQ_TRANSPOND_TO_COUNTER()
    API_SCQ_SYSLOGS_GET()
    API_SCQ_TELLER_GET()
    API_SCQ_TELLER_PUT()
    API_SCQ_CUSTOMERRECORD_LIST_GET()
    API_SCQ_ORDER_LIST_GET()
    API_SCQ_QUEUE_GET()
    API_SCQ_MYCUSTOMER_LIST_GET()
    API_SCQ_MYORDER_LIST_GET()
    API_SCQ_MYAPPLYORDER_LIST_GET()
    API_SCQ_CALLER_IP_PORT_GET()
    API_SCQ_CUSTOMER_GET()
    API_SCQ_CUSTOMERRECORD_SUBMIT()
    API_SCQ_CUSTOMERRECORD_GET()
    API_SCQ_CUSTOMER_OF_NAME_GET()
    API_SCQ_OFFICE_PUT()
    ticket = API_SCQ_TICKET_ADD()
    assert ticket is not None
    ticketid = ticket['ticketid']
    API_SCQ_TICKET_STATUS_PUT(ticketid, 'DOING')
    API_SCQ_TICKET_TRANSFER(ticketid, business, vipbusiness)
    API_SCQ_REQUEST_WELCOME(ticketid)
    API_SCQ_IDCARD_BIND(ticketid)
    API_SCQ_EVALUATION_PUT(ticketid)

if __name__ == '__main__':
    test_scq_api()