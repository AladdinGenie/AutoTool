# coding: utf-8
import public.httpmethod
from common import *
import unittest



def API_SCB_QUEUEE_BROADCAST():
    url = scburl + '/comm'
    data = {
        "filename": "queueCall",
        "call": {"cmd": "ADD", "key": ["windowname"], "records": [{"ticketnumber": "002", "windowname": "1"}]}
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
        log_result('API_SCB_QUEUEE_BROADCAST', '向叫号显示与播报软件发送叫号数据', url, response, result, data)


def API_SCB_HEARTBEAT_GET():
    url = scburl + '/api/v1/heartbeat'
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
        log_result('API_SCB_HEARTBEAT_GET', '心跳消息', url, response, result)


def test_scb_api():
    API_SCB_HEARTBEAT_GET()
    API_SCB_QUEUEE_BROADCAST()

if __name__ == '__main__':
    test_scb_api()