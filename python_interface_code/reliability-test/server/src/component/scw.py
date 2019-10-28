# coding: utf-8
import public.httpmethod
from common import *
import unittest

scw_ali = 'scwtest.51dmb.com'
p3 = 'oxs2ExDo3p4jTnSH5GzNzQVlAlsM'
p6 = 'fjfz'


def API_SCW_OFFICE_POST():
    url = scwurl + '/api/v1/office'
    data = {"id": officeid, "n": office['name'], "c": city['name'], "p": "自动化测试省",
            "d": "", "tm": 120, "ah": 0, "aht": "hour", "ad": 10, "pn": [], "t": ""}
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
        log_result('API_SCW_OFFICE_POST', '营业厅配置信息新增/更新消息', url, response, result, data)


# 2
def API_SCW_OFFICE_DEL():
    url = scwurl + '/api/v1/office'
    data = {"id": str(officeid)}
    code, response = public.httpmethod.Delete(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCW_OFFICE_DEL', '营业厅删除消息', url, response, result, data)


# 3
def API_SCW_BUSINESS_POST():
    '''暂未实现'''
    url = scwurl + '/api/v1/business'
    data = {
        "oid": officeid,
        "bs": [{
            "id": business['_id'], "name": business['name'], "isvip": False, "order": 0,
            "schedule": {
                "0": [{"start": "00:00", "end": "23:00"}], "1": [{"start": "00:00", "end": "23:00"}],
                "2": [{"start": "00:00", "end": "23:00"}], "3": [{"start": "00:00", "end": "23:00"}],
                "4": [{"start": "00:00", "end": "23:00"}], "5": [{"start": "00:00", "end": "23:00"}],
                "6": [{"start": "00:00", "end": "23:00"}], "-1": [{"start": "00:00", "end": "23:00"}],
            }
        }, {
            "id": vipbusiness['_id'], "name": vipbusiness['name'], "isvip": True, "order": 0,
            "schedule": {
                "0": [{"start": "00:00", "end": "23:00"}], "1": [{"start": "00:00", "end": "23:00"}],
                "2": [{"start": "00:00", "end": "23:00"}], "3": [{"start": "00:00", "end": "23:00"}],
                "4": [{"start": "00:00", "end": "23:00"}], "5": [{"start": "00:00", "end": "23:00"}],
                "6": [{"start": "00:00", "end": "23:00"}], "-1": [{"start": "00:00", "end": "23:00"}],
            }
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
        log_result('API_SCW_BUSINESS_POST', '业务配置信息新增/更新消息', url, response, result, data, comment='接口未实现，待确认')


# 4
def API_SCW_BUSINESS_DEL():
    '''暂未实现'''
    url = scwurl + '/api/v1/business'
    data = {"oid": officeid, "id": business['_id']}
    code, response = public.httpmethod.Delete(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCW_BUSINESS_DEL', '业务删除消息', url, response, result, data, comment='接口未实现，待确认')


# 5
def API_SCW_SUBBUSINESS_PUT():
    url = scwurl + '/api/v1/business/sb'
    data = {"bs": [{"id": business['_id'], "sb": [{"n": "", "t": ""}]}]}
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
        log_result('API_SCW_SUBBUSINESS_PUT', '更新营业厅业务明细类型', url, response, result, data)


# 6
def API_SCW_BUSINESSITEM_PUT():
    '''与API_SCW_SUBBUSINESS_PUT为同一接口，删除'''
    url = scwurl + '/api/v1/business/sb'
    data = {"bs": [{"id": business['_id'], "sb": [{"n": "细分类型名称", "t": "办理提示"}]}]}
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
        log_result('API_SCW_BUSINESSITEM_PUT', '业务细分类型配置信息更新消息', url, response, result, data)


# 7
def test_api_scw_numberrule_post():
    url = scwurl + '/api/v1/numberrule'
    bs = []
    for b in businesses:
        info = {
            'id': b['_id'], "n": b['name'], 'v': b['isvip'], 'o': b['order'], 'sb': b['subbusinesses'],
            'rs': [{
                "d": "%sT16:00:00.000Z" % YESTERDAY, "ts": [
                    {"s": "%sT16:05:00.000Z" % YESTERDAY, "e": "%sT14:55:00.000Z" % TODAY, "i": 30, "wn": 30,
                     "rn": 10}]
            }, {
                "d": "%sT16:00:00.000Z" % TODAY, "ts": [
                    {"s": "%sT16:05:00.000Z" % TODAY, "e": "%sT14:55:00.000Z" % TOMORROW, "i": 30, "wn": 30,
                     "rn": 10}]
            }]
        }
        bs.append(info)
    data = {"oid": officeid, "bs": bs, "sd": False}
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
        log_result('api_scw_numberrule_post', '推送号源配置信息', url, response, result, data)


# 8
def API_SCW_NUMBERRUEL_DEL():
    '''暂未实现'''
    url = scwurl + '/api/v1/numberrule'
    data = {"oid": int(officeid), "bid": business['_id'], "rt": TODAY}
    code, response = public.httpmethod.Delete(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCW_NUMBERRUEL_DEL', '号源配置信息删除消息', url, response, result, data, comment='接口未实现，待确认')


# 9
def API_SCW_NUMBERRULE_DELETE():
    '''暂未实现'''
    url = scwurl + '/api/v1/sync'
    data = {"oid": int(officeid), "bid": business['_id'], "rt": TODAY}
    code, response = public.httpmethod.Delete(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCW_NUMBERRULE_DELETE', '号源删除', url, response, result, data, comment='接口未实现，待确认')


# 10
def API_SCW_DTDCONF_POST():
    '''暂未实现'''
    url = scwurl + '/api/v1/dtdinfo'
    data = {
        "id": province_idpath.split('.')[-1], "n": "自动化测试省",
        "ad": 10, "at": [{"s": "09:00", "e": "11:00"}], "cs": [],
        "sub": [{"si": city['_id'], "sn": city['name'], "st": "三环内支持上门服务"}],
        "nt": "未达标客户提示", "ra": ['zhangsan'],
        "buss": [{"bi": business['_id'], "bn": business['name'], "bs": [{"n": "满期给付", "t": "请准备身份证"}]}]
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
        log_result('API_SCW_DTDCONF_POST', '更新上门服务配置、业务信息', url, response, result, data, comment='接口未实现')


def scw_appoint2017(pbusiness=business, idcard=newidcard(), phone='15205042128'):
    rest_time = scw_get_appoint_time(pbusiness)
    assert rest_time is not None
    back = False
    url = scwurl + '/api/v1/appoint2'
    data = {"businesses": [{"bi": pbusiness['_id'], "bn": pbusiness['name']}], "office_id": int(officeid),
            "start": rest_time['start'], "end": rest_time['end'], "bqa": False, "self": True, "bdltnames": [],
            "customerphone": phone, "customeridcard": idcard, "customername": '赵立晓', "bdlt": True,
            "customertype": "I", "seller": None, "bv": pbusiness['isvip'], "customerlevel": "", "customersex": ""}
    code, response = public.httpmethod.Post(url, json.dumps(data), headers)
    try:
        assert code == 200
        response = json.loads(response)
        assert response['message'] == "预约成功"
        result = PASS
        back = True
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('scw_appoint2017', '微信端预约业务', url, response, result, data)
        return response


def scw_get_appoint_time(pbusiness=business):
    rest_time = None
    url = scwurl + '/api/v1/number2?business_ids=%s&office_id=%s' % (pbusiness['_id'], officeid)
    result = FAIL
    response = None
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        response = json.loads(response)
        for at in response:
            if at['rest'] > 0:
                rest_time = at
                result = PASS
                break
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('scw_get_appoint_time', '获取业务的可预约时段', url, response, result)
        return rest_time


def API_SCW_EVALUATION_REQUEST(ticketid, number):
    url = scwurl + '/api/v1/ticket/evaluation'
    data = {"ticketid": ticketid, "officeid": officeid, "appointmentnumber": number}
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
        log_result('API_SCW_EVALUATION_REQUEST', '请求评价', url, response, result, data)


def API_SCW_TICKET_STATUS_PUT(ticketid, status='DOING'):
    url = scwurl + '/api/v1/ticket'
    data = {"ticketid": ticketid, "officeid": officeid, "windowname": window['name'],
            "ticketstatus": status}
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
        log_result('API_SCW_TICKET_STATUS_PUT', '虚拟处理完成', url, response, result, data)


def API_SCW_APPOINTMENT_PUT(number, status='CHECKIN'):
    '''暂未实现'''
    url = scwurl + '/api/v1/appoint'
    data = {"number": number, "status": status}  # CANCEL, CHECKIN,
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
        log_result('API_SCW_APPOINTMENT_PUT', '更新预约状态', url, response, result, data, comment='接口未实现，待确认')


def API_SCW_EVALUATION_CLOSE(ticket):
    url = scwurl + '/api/v1/ticket/evaluation'
    data = {
        "ticketid": ticket['ticketid'],
        "officeid": officeid
    }
    code, response = public.httpmethod.Delete(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCW_EVALUATION_CLOSE', '关闭评价', url, response, result, data)


def scw_shake_ticket():
    url = 'http://%s/api/v1/customer/me?p3=%s&p6=%s' % (scw_ali, p3, p6)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        url = 'http://%s/api/v1/ticket2' % scw_ali
        data = {"business_id": business['_id'], "office_id": officeid, "isvip": False}
        code, response = public.httpmethod.Post(url, json.dumps(data), headers)
        assert code == 200
        response = json.loads(response)
        assert 'data' in response.keys()
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('scw_shake_ticket', '摇一摇取票', url, response, result, data)
        return response


def scw_ticket2_get(ticketnumber):
    url = 'http://%s/api/v1/ticket2?mark=%s' % (scw_ali, officeid)
    code, response = public.httpmethod.Get(url)
    ticket2_scw_id = None
    try:
        assert code == 200
        response = json.loads(response)
        for ticket2 in response:
            if ticket2['sn'] == ticketnumber:
                ticket2_scw_id = ticket2['_id']
                result = PASS
                break
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('scw_ticket2_get', '我的取号', url, response, result)
        return ticket2_scw_id


def scw_ticket_evaluation_put(ticketid):
    url = 'http://%s/api/v1/ticket2/%s/evaluate' % (scw_ali, ticketid)
    data = {"_id": ticketid, "nsa": 5, "nsen": 5, "nsef": 5, "sse": "dw"}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        response = json.loads(response)
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('scw_ticket2_evaluation_put', '手机端评价', url, response, result, data)


def test_scw_api():
    API_SCW_OFFICE_DEL()
    API_SCW_OFFICE_POST()
    API_SCW_SUBBUSINESS_PUT()
    API_SCW_BUSINESSITEM_PUT()
    API_SCW_BUSINESS_DEL()
    API_SCW_BUSINESS_POST()
    API_SCW_NUMBERRUEL_DEL()
    API_SCW_NUMBERRULE_DELETE()
    test_api_scw_numberrule_post()
    API_SCW_DTDCONF_POST()
    scw_get_appoint_time()


if __name__ == '__main__':
    test_scw_api()
