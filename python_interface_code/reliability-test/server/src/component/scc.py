# coding: utf-8
import public.httpmethod
import unittest
from common import *
from src.env.setting import *


# 1
def API_SCC_EVALUATOR_EVALUATION(ticket):
    url = sccurl + '/api/v1/evaluation'
    data = {'ticketid': ticket['ticketid']}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_EVALUATOR_EVALUATION', '发起评价', url, response, result, data)
    try:
        code, response = public.httpmethod.Delete(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_EVALUATOR_EVALUATION', '删除评价', url, response, result, data)


# 2
def API_SCC_EVALUATION_SUBMIT(ticket):
    url = sccurl + '/api/v1/evaluation'
    data = {"ticketid": ticket['ticketid'], "type": "sce", "value": "1"}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_EVALUATION_SUBMIT', '评价结果上报', url, response, result, data)


# 3
def API_SCC_TICKET_DEL(ticketid):
    url = sccurl + '/api/v1/ticket'
    data = {"ticketid": ticketid}
    try:
        code, response = public.httpmethod.Delete(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_TICKET_DEL', '叫号软件删除排队记录', url, response, result, data)


# 4
def API_SCC_TICKET_ADD():
    ticket = {'policypoint': 48256, 'validpolicy': 5, 'customername': '', 'customerbirth': '1970-01-02',
              'businessid': business['_id'], 'ordernumber': '3', 'ticketnumber': 'UA0046',
              'tickettime': '%s 16:19:10.410' % TODAY, 'totalpolicy': 13,
              'unitname': '\xe7\xb2\xbe\xe5\x87\x86\xe8\x90\xa5\xe9\x94\x801', 'idcards': '350583199312309281',
              'customerlevel': '1', 'totalpremium': 5232321, 'businessname': business['name'],
              'isappointment': 0, 'ticketid': '64', 'customersex': 'M'}
    url = sccurl + '/api/v1/ticket'
    data = {
        "ticketid": ticket['ticketid'],
        "ticketnumber": ticket['ticketnumber'],
        "ordernumber": ticket['ordernumber'],
        "businessid": ticket['businessid'],
        "businessname": ticket['businessname'],
        "tickettime": ticket['tickettime'],
        "isappointment": 0,
        "customername": ticket['customername'],
        "customersex": ticket['customersex'],
        "idcards": "350583199312309281",
        "customerlevel": "1",
        "customerbirth": "1970-01-02",
        "totalpolicy": 13,
        "validpolicy": 5,
        "totalpremium": 5232321,
        "policypoint": 48256,
        "unitname": "精准营销1",
    }
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
        log_result('API_SCC_TICKET_ADD', '叫号软件新增排队记录', url, response, result, data)


# 5
def API_SCC_TICKET_PUT(ticketid):
    url = sccurl + '/api/v1/ticket'
    data = {"tickets": [{"ticketid": ticketid, "status:": 'HANGUP'}]}  # HANGUP（挂起）、WAIT（取消挂起）
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_TICKET_PUT', '修改票号状态：挂起', url, response, result, data)

    try:
        data = {"tickets": [{"ticketid": ticketid, "status:": 'WAIT'}]}
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result('API_SCC_TICKET_PUT', '修改票号状态：取消挂起', url, response, result, data)

        # 1


def API_SCC_WINDOWBOXIP_UPDATE():
    url = sccurl + '/api/v1/windowboxip'
    data = {"windowboxip": sccurl[7:-5], "windowboxport": sccurl[-4:]}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_WINDOWBOXIP_UPDATE', '叫号软件更新评价软件IP', url, response, result, data)


# 2
def API_SCC_TELLER_GET():
    url = sccurl + '/api/v1/teller/%s' % window['_id']
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        response = json.loads(response)
        assert response['code'] == teller_user
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_TELLER_GET', '员工牌显示请求', url, response, result)


# 3
def API_SCC_TELLER_LOGOUT():
    url = sccurl + '/api/v1/logout'
    data = {"windowid": window['_id']}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_TELLER_LOGOUT', '叫号软件登出', url, response, result, data)


# 4
def API_SCC_EVALUATOR_WELCOME():
    url = sccurl + '/api/v1/welcome'
    data = {'data': 'welcome'}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_EVALUATOR_WELCOME', '请求评价器欢迎', url, response, result)


# 5
def API_SCC_DISCARDOVERTIME_PUT():
    url = sccurl + '/api/v1/discardovertime'
    data = {'discardovertime': 2}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_DISCARDOVERTIME_PUT', '叫号软件更新弃号超时时间', url, response, result, data)


# 6
def API_SCC_PRODUCTS_PUT():
    url = sccurl + '/api/v1/products'
    data = {'products': ["重疾保障产品", "人寿保险"]}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_PRODUCTS_PUT', '叫号软件更新推荐产品列表', url, response, result, data)


# 7
def API_SCC_LOG_GET():
    url = sccurl + '/api/v1/log'
    code, result = public.httpmethod.Get(url)
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        assert isinstance(response, list)
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_LOG_GET', '叫号软件日志获取', url, response, result)


# 8
def API_SCC_EVALUATOR_LEVEL():
    url = sccurl + '/api/v1/tellerlevel'
    data = {'level': 2}
    try:
        code, response = public.httpmethod.Put(url, json.dumps(data), headers)
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCC_EVALUATOR_LEVEL', '请求评价器设置星级', url, response, result, data)


def test_scc_api():
    API_SCC_WINDOWBOXIP_UPDATE()
    API_SCC_TELLER_GET()
    API_SCC_EVALUATOR_WELCOME()
    API_SCC_DISCARDOVERTIME_PUT()
    API_SCC_PRODUCTS_PUT()
    API_SCC_LOG_GET()
    API_SCC_TICKET_ADD()
    API_SCC_EVALUATOR_LEVEL()
    API_SCC_TELLER_LOGOUT()


if __name__ == '__main__':
    test_scc_api()
