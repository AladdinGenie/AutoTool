# coding: utf-8
import public.httpmethod
from common import *
import unittest


# 1
def API_SCE_HEARTBEAT_POST():
    url = sceurl + '/api/v1/heartbeat'
    data = {"status": "start", "tellercode": teller['code']}
    code, response = public.httpmethod.Post(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCE_HEARTBEAT_POST', '叫号软件定时向评价软件发送心跳消息', url, response, result, data)


# 2
def API_SCE_HEARTBEAT_GET():
    url = sceurl + '/api/v1/heartbeat'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCE_HEARTBEAT_GET', '排队服务软件向评价软件发送心跳消息，判断评价软件是否可连接', url, response, result)


# 3
def API_SCE_STATUS_SHOW():
    url = sceurl + '/api/v1/status'
    data = {"status": 'stop', "tellercode": teller['code']}
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
        log_result('API_SCE_STATUS_SHOW', '暂停服务', url, response, result, data)
    data = {"status": 'start', "tellercode": teller['code']}
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
        log_result('API_SCE_STATUS_SHOW', '开始服务', url, response, result, data)


# 4
def API_SCE_STUFF_PLAY():
    url = sceurl + '/api/v1/stuff/playlist'
    data = {
        "md5": string.join(random.sample('12345678901234567890', 16)).replace(' ', ''),
        "data": [{
            "filename": "playShow",
            "play": {
                "cmd": "ALL", "key": [],
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
        log_result('API_SCE_STUFF_PLAY', '排队服务软件发送播放内容信息到评价软件显示', url, response, result, data)


# 5
def API_SCE_TICKET_SHOW(ticketid='123'):
    url = sceurl + "/api/v1/ticket"
    data = {"ticketnumber": str(ticketid), "windowname": window['name']}
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
        log_result('API_SCE_TICKET_SHOW', '叫号显示', url, response, result, data)


# 6
def API_SCE_WELCOME_SHOW(ticketid='123'):
    url = sceurl + "/api/v1/welcome"
    data = {"unitname": "", "welcomeinfo": "欢迎您" + str(ticketid) + "，" + teller['code'] + "正在为您服务！"}
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
        log_result('API_SCE_WELCOME_SHOW', '欢迎显示', url, response, result, data)


# 7
def API_SCE_EVELUATE_SHOW(ticketid='123'):
    url = sceurl + '/api/v1/evaluation'
    data = {"ticketid": ticketid}
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
        log_result('API_SCE_EVELUATE_SHOW', '评价显示', url, response, result, data)


# 8
def API_SCE_EVELUATE_CLOSE(ticketid='123'):
    url = sceurl + '/api/v1/evaluation'
    data = {"ticketid": str(ticketid)}
    code, response = public.httpmethod.Delete(url, json.dumps(data))
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCE_EVELUATE_CLOSE', '评价关闭', url, response, result, data)


# 9
def API_SCE_TELLER_SHOW(pteller=tellerinfo):
    url = sceurl + "/api/v1/teller"
    data = {"code": pteller['code'], "name": pteller['name'], "photoimgpath": pteller['photoimgpath'],
            "levelimgpath": pteller['levelimgpath'], "level": pteller['level']}
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
        log_result('API_SCE_TELLER_SHOW', '柜员信息显示', url, response, result, data)


def test_sce_api():
    API_SCE_TELLER_SHOW()
    API_SCE_HEARTBEAT_POST()
    API_SCE_HEARTBEAT_GET()
    API_SCE_STATUS_SHOW()
    API_SCE_STUFF_PLAY()
    ticketid = string.join(random.sample('1234567890123456789012345678901234567890', 3)).replace(' ', '')
    API_SCE_TICKET_SHOW(ticketid)
    API_SCE_WELCOME_SHOW(ticketid)
    API_SCE_EVELUATE_SHOW(ticketid)
    API_SCE_EVELUATE_CLOSE(ticketid)


if __name__ == '__main__':
    test_sce_api()