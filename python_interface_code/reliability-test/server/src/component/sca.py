# coding: utf-8
import public.httpmethod
import unittest
from common import *

# 相关配置文件
# /mean/smartcounterapiserver/lib/config/env/all.js   port_https
# /mean/smartcounterapiserver/lib/config/env/production.js


def API_SCA_TELLER_TOKEN_GET_V2():
    url = scaurl_https + '/api/v2/teller/token?username=%s&password=%s' % (
        teller['code'], teller['password'])
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
        log_result('API_SCA_TELLER_TOKEN_GET_V2', '柜员身份认证', url, response, result)
    result = response
    if result.startswith('{'):
        result = json.loads(result)
        return result['access_token']


def API_SCA_TELLER_STATUS_PUT_V2(token):
    url = scaurl + '/api/v2/teller/status'
    data = {
        "access_token": token,
        "username": teller['code'],
        "officeid": int(officeid),
        "windowid": window['_id'],
        "status": "login"
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
        log_result('API_SCA_TELLER_STATUS_PUT_V2', '柜员状态更新', url, response, result, data)


def API_SCA_MANAGER_HELP_PUT_V2(token):
    url = scaurl + '/api/v2/manager/help'
    data = {
        "access_token": token,
        "username": teller['code'],
        "officeid": int(officeid),
        "windowid": window['_id']
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
        log_result('API_SCA_MANAGER_HELP_PUT_V2', '柜员求助', url, response, result, data)


def API_SCA_TICKET_STATUS_PUT_V2(ticket, token=API_SCA_TELLER_TOKEN_GET_V2()):
    url = scaurl + '/api/v2/ticket/status'
    data = {
        "access_token": token,
        "username": teller['code'],
        "officeid": int(officeid),
        "windowid": window['_id'],
        "action": "CALL",
        "ticketno": ticket['ticketnumber'],
        "businesses": []
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
        log_result('API_SCA_TICKET_STATUS_PUT_V2', '票号状态更新', url, response, result, data)


def test_sca_api():
    token = API_SCA_TELLER_TOKEN_GET_V2()
    API_SCA_TELLER_STATUS_PUT_V2(token)
    API_SCA_MANAGER_HELP_PUT_V2(token)

if __name__ == '__main__':
    test_sca_api()
