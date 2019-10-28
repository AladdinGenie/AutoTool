# coding: utf-8

import public.httpmethod
from common import *
from public.formdata import encode_multipart_formdata

daterange = 'dateRange={"span":"month","startDate":"%sT10:00:00.000Z","endDate":%sT17:59:59.999Z"}' % (TODAY, TODAY)
filterp = '&filterKey=p&filterValue=%s' % province['name']
BASE_CONF = {"proinherit": {}, "comtikleninherit": {}, "apptikleninherit": {}, "apptikpreinherit": {},
             "ticketsuffixlengthinherit": {"type": "cou", "val": 3},
             "vipticketpreinherit": {"type": "cou", "val": "V"},
             "appointticketpre2inherit": {"type": "cou", "val": "Y"},
             "commonticketpreinherit": {"type": "cou", "val": "A"}, "qrcodeinherit": {}, "appdaysinherit": {},
             "apptiktimeinherit": {}, "apptimeinherit": {}, "apptimetypeinherit": {}, "appstartrangeinherit": {},
             "appendrangeinherit": {}, "advertisinherit": {}, "warncountinherit": {}, "warninvinherit": {},
             "busimindurainherit": {}, "busimaxdurainherit": {}, "waitmaxdurainherit": {}, "busovertimeinherit": {},
             "waitovertimeinherit": {}, "discardovertimeinherit": {}, "ticketautocallintervalinherit": {},
             "ticketqrcodesinherit": {},
             "tipinherit": {}, "accompanyenabledinherit": {}, "products": ["财产保险2596q", "旅游保险2596q"],
             "waitovertime": 30, "advertisings": [], "qrcode2": {"image": "", "content": ""},
             "waitmaxduration": 240, "ticketautocallinterval": 0, "discardovertime": 1,
             "businessminduration": 5, "businessmaxduration": 240, "appointtimetype": "hour", "appointstartrange": 5,
             "appointendrange": 5, "__v": 0, "office_id": officeid, "warncount": 3, "appointticketlength": 4,
             "appointticketpre": "预", "businessovertime": 20, "getappointtickettime": 120, "appointtime": 0,
             "appointdays": 2, "warninterval": 5, "commonticketlength": 4,
             "qrcode1": {"image": "", "content": ""}, "ticketlimit": {"interval": 1, "count": 100},
             "ticketcountlimit": {"day": 100, "week": 100, "month": 100}
             }


def add_office(name, officetype, parentPath):
    if officetype == 'province':
        parentPath = '.0.'
    url = scsurl + "/api/v1/settings/offices"
    prefix = 'a' if officetype == 'city' else 'b'
    data = {"type": officetype, "name": name, "parentPath": parentPath, 'no': prefix + subfix}
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
        log_result('add_office', '新增组织结构', url, response, result, data)
    return json.loads(response)


def add_business():
    schedule = {}
    for i in range(0, 7):
        schedule[str(i)] = [{"start": "00:00", "end": "23:00"}]
    url = scsurl + "/api/v1/settings/business"
    data = {"businesses": [
        {"code": "V", "name": "VIP业务" + subfix, "order": 0, "office_id": officeid, "isvip": True,
         "schedule": schedule},
        {"code": "A", "name": "保全业务" + subfix, "order": 1, "office_id": officeid, "isvip": False,
         "schedule": schedule}],
        "office_path": office_idpath}
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
        log_result('add_business', '新增业务', url, response, result, data)
        result = json.loads(response)
        return json.loads(result)


def get_baseconf():
    url = scsurl + "/api/v1/settings/baseconf/%s" % officeid
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['office_id'] == int(officeid)
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('get_baseconf', '获取基本配置 ', url, response, result, code)
        result = json.loads(response)
        return result


def set_baseconf():
    url = scsurl + '/api/v1/settings/baseconf'
    data = BASE_CONF
    data['businessruleversioninherit'] = {"type": "cou", "val": "V1"}
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
        log_result('set_baseconf', '设置基本配置 ', url, response, result, data)
    result = json.loads(result)
    return result


def update_baseconf(rule2=False):
    v = 'V2' if rule2 else 'V1'
    baseconf_id = get_baseconf()['_id']
    url = scsurl + '/api/v1/settings/baseconf/%s' % baseconf_id
    data = BASE_CONF
    data['_id'] = baseconf_id
    data['businessruleversion'] = v
    data['businessruleversioninherit'] = {}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['office_id'] == int(officeid)
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('update_baseconf', '更新基本配置 ', url, response, result, data)


def set_officeconf():
    v = get_officeconf()['__v']
    url = scsurl + "/api/v1/settings/officeconf/%s" % officeconfid
    data = {"scqip": scqurl[7:-5], "scqport": scqurl[-4:], "address": "测试地址金山大道", "unit": "minute",
            "ticketinterval": 5,
            "ticketcount": 10, "specialids": [], "specialID": "", "rainbowaccounts": ["starnetzlx"],
            "idneeded": True, "pwdenabled": True, "vipcommonbussenabled": True, "specialpassportenabled": True,
            "summertime": {"enabled": False}, "ticketnotice": {"commoncustomer": False, "seller": False},
            "vipcustomer": {"includeseller": True}, "_id": officeconfid, "office_id": int(officeid), "__v": v,
            "worktimes": [{"name": "周一至周五", "tip": ""}, {"name": "周六", "tip": ""}, {"name": "周日", "tip": ""}],
            "pwdaccounts": [],
            "msgreceivers": [{"name": "评价通知", "code": "evaluate", "receivers": []},
                             {"name": "取VIP号通知", "code": "vip", "receivers": []},
                             {"name": "呼叫客户经理", "code": "assist", "receivers": []},
                             {"name": "等待人数告警", "code": "waitpersonnumber", "receivers": []},
                             {"name": "窗口闲置时长告警", "code": "windowfreetime", "receivers": []},
                             {"name": "平均等待时长告警", "code": "customerwaittime", "receivers": []},
                             {"name": "单笔业务办理时长告警", "code": "businessdoingtime", "receivers": []}],
            "scqmacs": ["F48E388E8449"], "$promise": {}, "$resolved": True}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['office_id'] == int(officeid)
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('set_officeconf', '更新营业厅配置 ', url, response, result, data)


def set_bs3config():
    url = scsurl + "/api/v1/sysconf"
    data = {"bs3rootpwd": "aabb2100033f0352fe7458e412495148", "bs3rootusr": "root",
            "tellerimgpath": "/stufflib/IMAGE",
            "bs3url": bs3url}
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
        log_result('set_bs3config', 'DCPP配置 ', url, response, result, data)


def get_file_type():
    _dict = {}
    evideo = [".avi", ".mpg", ".mp4", ".wmv", ".mov", ".ts", ".mkv"]
    for e in evideo:
        _dict[e] = '视频'
    picture = [".jpg", ".png", ".bmp", ".gif"]
    for p in picture:
        _dict[p] = '图片'
    _dict[".txt"] = '文本'
    _dict[".pdf"] = 'PDF'
    _dict[".ppt"] = 'PPT'
    return _dict


def validate_stuff(filename):
    filetype = get_file_type()
    for i in filetype.keys():
        if os.path.splitext(filename)[1] == i:
            return True
    return False


def check(key, value):
    url = scsurl + '/api/v1/user/attribute/{"checkKey": "%s", "checkValue": "%s"}' % (key, value)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['result'] == 'true'
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('check', '名称验证', url, response, result)


def API_SCS_TICKET_AUTH(idcard):
    url = scsurl + '/api/v1/ticket/auth?idcard=%s&officeid=%s' % (idcard, officeid)
    try:
        code, response = public.httpmethod.Get(url)
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_TICKET_AUTH', '取票认证', url, response, result)
        return response


def API_SCS_TICKETLOG_SUBMIT(ticket):
    url = scsurl + '/api/v1/ticketlog'
    endstatus = random.choice(['DONE', 'DISCARD'])
    if endstatus != 'DONE':
        evaluateresult = ''
        evaluaterequesttime = ''
        evaluateresulttime = ''
    else:
        evaluateresult = random.choice(['1', '3', '5'])
        evaluaterequesttime = TODAY + " 10:30:00"
        evaluateresulttime = TODAY + " 10:31:00"
    idcard = random.choice([vip_idcard, normal_idcard, newidcard()])
    data = {"logs": [{
        "ticketid": ticket['ticketid'], "tickettime": ticket['tickettime'],
        "customername": ticket['customername'], "customerlevel": '1', "customersex": ticket['customersex'],
        "customeridcard": idcard,
        "businessname": ticket['businessid'], "province": province['name'], "city": city['name'],
        "officeid": str(officeid),
        "officename": office['name'], "ticketnumber": ticket['ticketnumber'],
        "appointmentid": "54b3728f2d358de80ed445d2",
        "calltime": TODAY + " 10:10:00", "waittime": "500000", "tellername": teller['name'],
        "tellercode": teller['code'], "windowname": window['name'], "welcometime": TODAY + " 10:20:00",
        "evaluaterequesttime": evaluaterequesttime, "evaluateresulttime": evaluateresulttime,
        "evaluateresult": evaluateresult, "endtime": TODAY + " 10:31:02", "endstatus": endstatus,
        "dealtime": "1200000", "isovertime": random.choice(['false', 'true'])
    }]}
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
        log_result('API_SCS_TICKETLOG_SUBMIT', '上报票行为记录 ', url, response, result, data)


def API_SCS_TICKET_ADD(idcard=None, businessid=None, isvip=None, number=None):  # idcard为必填项
    url = scsurl + '/api/v1/ticket'
    data = {"idcard": idcard, "officeid": officeid, "type": "wechat"}  # type=local的情况全部由SCQ自动发起，本用例不再执行
    if number:
        data['appointmentnumber'] = number
    if businessid:
        data['businessid'] = businessid
        data['isvip'] = isvip
    code, response = public.httpmethod.Post(url, json.dumps(data), headers)
    try:
        assert code == 200
        response = json.loads(response)
        assert response['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_TICKET_ADD', '新增取票', url, response, result, data)
        return response


def API_SCS_TICKET_STATUS_PUT(ticket, stat='DOING'):
    url = scsurl + '/api/v1/ticket'
    data = {"ticketid": ticket['ticketid'], "officeid": officeid, "windowname": window['name'], "ticketstatus": stat}
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
        log_result('API_SCS_TICKET_STATUS_PUT', '虚拟' + stat, url, response, result, data)


def API_SCS_TICKET_EVALUATION_PUT(ticket, value='1'):
    url = scsurl + '/api/v1/ticket/evaluation'
    data = {"ticketid": ticket['ticketid'], "officeid": int(officeid),
            "value": value, "isappointticket": False, "isvirtualticket": False}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_TICKET_EVALUATION_PUT', '请求评价，上报评价结果', url, response, result, data)


def API_SCS_EVELUATE_CLOSE(ticket):
    url = scsurl + "/api/v1/ticket/evaluation"
    data = {"ticketid": ticket['ticketid'], "officeid": int(officeid)}
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
        log_result('API_SCS_EVELUATE_CLOSE', '关闭评价 ', url, response, result, data)


def API_SCS_DTD_APPOINTMENT_ADD(openid='oxs2ExDo3p4jTnSH5GzNzQVlAlsM'):  # 未实现
    url = scsurl + '/api/v1/dtdAppointment'
    data = {
        "id": "02145875454",
        "province": province['name'],
        "city": city['name'],
        "address": "金山大道",
        "customername": normal_name,
        "customertype": "I",
        "customeridcard": normal_idcard,
        "customerphone": "97690500",
        "businesses": [{
            'bid': business['_id'],
            'bn': business['name'],
            'bs': ["变更收益人", "满期给付"]
        }],
        "starttime": TODAY + " 9:00:00",
        "endtime": TODAY + " 12:00:00",
        "openid": openid,
        "type": "wechat"
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
        log_result('API_SCS_DTD_APPOINTMENT_ADD', '新增上门服务预约', url, response, result, data, comment='接口未实现')


def API_SCS_APPOINTMENT_STATUS(idcard, phone='15205042128'):
    url = scsurl + '/api/v1/appointments?type=wechat&customertype=I&customeridcard=%s&customerphone=%s' % (
        idcard, phone)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result is not list()
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_APPOINTMENT_STATUS', '获取预约状态信息', url, response, result)
        return json.loads(response)


def API_SCS_APPOINTMENT_PUT(number):
    url = scsurl + '/api/v1/appointment/%s' % number
    data = {
        "officeid": officeid,
        "starttime": TODAY + " 17:00:00",
        "endtime": TODAY + " 17:15:00",
        "newNumber": number
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
        log_result('API_SCS_APPOINTMENT_PUT', '修改预约', url, response, result, data=data)


def API_SCS_APPOINTMENT_DEL(number):
    url = scsurl + '/api/v1/appointment/%s' % number
    code, response = public.httpmethod.Delete(url, None, headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_APPOINTMENT_DEL', '取消预约', url, response, result)


def test_add_teller_photo():
    filename = '3.jpg'
    filepath = os.path.join(STUFF_DIR, filename)
    filesize = str(os.path.getsize(filepath))
    # 提交头像信息，获取头像名称
    url = scsurl + '/api/v1/upload/image?flowChunkNumber=1&flowChunkSize=1048576&flowCurrentChunkSize=%s&' \
                   'flowTotalSize=%s&flowIdentifier=%s-%s&flowFilename=%s&flowRelativePath=%s&flowTotalChunks=1' \
                   % (filesize, filesize, filesize, filename.replace('.', ''), filename, filename)
    code, response = public.httpmethod.Get(url)
    result = json.loads(response)
    # 上传头像
    url = scsurl + '/api/v1/upload/image'
    form_data = [
        ('flowChunkNumber', '1'), ('flowChunkSize', '1048576'), ('flowCurrentChunkSize', filesize),
        ('flowTotalSize', filesize), ('flowIdentifier', filesize + '-' + filename.replace('.', '')),
        ('flowFilename', filename), ('flowRelativePath', filename), ('flowTotalChunks', '1'),
        ('file', "f'%s'" % filepath)
    ]
    contenttype, formed_data = encode_multipart_formdata(form_data)
    headers1 = {'Content-Type': contenttype}
    code, response = public.httpmethod.Post(url, formed_data, headers1)
    try:
        assert code == 200
        result = PASS
    except:
        result = FAIL
    finally:
        log_result('add_teller_photo', '上传柜员头像', url, response, result, code)
    # 更新柜员头像
    url = scsurl + '/api/v1/settings/teller/%s' % teller['_id']
    data = {"_id": teller['_id'], "name": teller['name'], "code": teller_user, "phototmp": response,
            "photostuffid": teller['photostuffid'], "photoname": teller['photoname'], "sex": teller['sex'],
            "level": teller['level'], "idpaths": [office_idpath], "offices": office['name']}
    code, response = public.httpmethod.Put(url, json.dumps(data), headers)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['code'] == teller_user
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('add_teller_photo', '更新柜员信息', url, response, result, data)


def API_SCS_CUSTOMERRECORD_SUBMIT(idcard=vip_idcard):
    url = scsurl + '/api/v1/customerrecord'
    data = {"businessname": business['name'], "name": normal_idcard, "idcard": idcard,
            "telephone": normal_phone, "address": "", "salary": "", "isnew": False,
            "buyproducts": [{"productname": "理财保险", "buypercent": "25%"},
                            {"productname": "旅游保险", "buypercent": "50%"}],
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
        log_result('API_SCS_CUSTOMERRECORD_SUBMIT', '登记客户信息', url, response, result, data)


def API_SCS_CUSTOMERRECORD_GET(idcard=vip_idcard):
    url = scsurl + '/api/v1/customerrecord/%s' % idcard
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
        log_result('API_SCS_CUSTOMERRECORD_GET', '获取客户登记信息', url, response, result)


def API_CUS_CALLLOG_GET(idcard=normal_idcard):
    url = scsurl + '/api/v1/customercalllog?idcard=%s&officeid=%s' % (idcard, officeid)
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
        log_result('API_CUS_CALLLOG_GET', '获取客户来电信息', url, response, result)


def API_SCS_CUSTOMER_AUTH(idcard=normal_idcard):
    url = scsurl + '/api/v1/customer?idcard=' + idcard + '&officeid=' + str(officeid)
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
        log_result('API_SCS_CUSTOMER_AUTH', '客户认证', url, response, result)


def API_APPLYORDER_OF_TELLER_GET():
    url = scsurl + '/api/v1/sellerapplypolicy?sellerno=10001&sdate=20150101&edate=20150301&officeid=' + str(
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
        log_result('API_APPLYORDER_OF_TELLER_GET', '直销助手-我的签单-申请日期', url, response, result)


def API_SCS_CUSTOMER_OF_NAME_GET():
    url = scsurl + '/api/v1/customers?name=%E5%BE%90%E5%AE%81&officeid=' + str(officeid)
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
        log_result('API_SCS_CUSTOMER_OF_NAME_GET', '客户查询-姓名', url, response, result)


def API_SCS_CUSTOMERRECORD_LIST_GET():
    url = scsurl + '/api/v1/customerrecords/%s' % teller['code']
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
        log_result('API_SCS_CUSTOMERRECORD_LIST_GET', '获取客户登记信息列表', url, response, result)


def API_SCS_NUMBERRULE_GET():
    url = scsurl + '/api/v1/numberrule?officeId=%s' % officeid
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
        log_result('API_SCS_NUMBERRULE_GET', '同步预约号策略', url, response, result)


def API_SCS_STUFF_GET():
    url = scsurl + '/api/v1/stuff/playlist?officeid=%s&md5=' % officeid
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
        log_result('API_SCS_STUFF_GET', '获取指定营业厅的播放内容信息', url, response, result)


def API_SCS_QUEUE_GET():
    url = scsurl + '/api/v1/queue/%s' % officeid
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
        log_result('API_SCS_QUEUE_GET', '获取客户排队详情', url, response, result)


def API_SCS_OFFICEWAITCOUNT_GET():
    url = scsurl + '/api/v1/office/%s/waitcount' % officeid
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
        log_result('API_SCS_OFFICEWAITCOUNT_GET', '获取营业厅排队人数', url, response, result)


def API_SCS_OFFICEWAITDETAIL_GET():
    url = scsurl + '/api/v1/office/%s/waitdetail' % officeid
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
        log_result('API_SCS_OFFICEWAITDETAIL_GET', '获取营业厅等待详情', url, response, result)


def API_SCS_TELLERLOG_SUBMIT():
    url = scsurl + '/api/v1/tellerlog'
    data = {"logs": [
        {"tellername": teller['name'], "tellercode": teller['code'], "windowname": window['name'],
         "province": province['name'], "city": city['name'], "officeid": officeid,
         "officename": office['name'], "logintime": TODAY + " 08:30:00",
         "logouttime": TODAY + " 12:00:00", "onlinetime": 12000000}]}
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
        log_result('API_SCS_TELLERLOG_SUBMIT', '上报柜员在线日志 ', url, response, result, data)


def API_SCS_RAINBOW_NOTICE():
    url = scsurl + '/api/v1/rainbow'
    data = {"title": "呼叫大堂经理", "msg": "2号窗口呼叫大堂经理", "type": "assist", "officeid": str(officeid)}
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
        log_result('API_SCS_RAINBOW_NOTICE', '通知云助理消息 ', url, response, result, data)


def API_SCS_APPOINTMENT_ADD():
    url = scsurl + '/api/v1/appointment'
    data = {
        "province": province['name'],
        "city": city['name'],
        "officename": office['name'],
        "officeid": officeid,
        "number": string.join(random.sample('12345678901234567890', 8)).replace(' ', ''),
        "customername": normal_name,
        "customerlevel": "普通客户",
        "customersex": "男",
        "customertype": "I",
        "customeridcard": normal_idcard,
        "customerphone": normal_phone,
        "businesses": [{
            'bid': business['_id'],
            'bn': business['name'],
            'bs': ["变更收益人", "满期给付"]
        }],
        "seller": {
            'no': teller['code'],
            'account': "1234",
            'name': "销售A"
        },
        "": True,
        "starttime": TODAY + " 10:00:00",
        "endtime": TODAY + " 10:00:00",
        "openid": '1212121212121212121212',
        "type": "wechat"
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
        log_result('API_SCS_APPOINTMENT_ADD', '新增预约 ', url, response, result, data)


def API_SCS_CHECK_VERSION_GET():
    url = scsurl + '/api/v1/upgrade/version?officeid=' + str(officeid) + '&scq=&sct=&scc='
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
        log_result('API_SCS_CHECK_VERSION_GET', '升级版本检测', url, response, result)


def API_SCS_UPDATE_VERSION_PUT():
    url = scqurl + '/api/v1/upgrade/version'
    data = {"scqhref": "/scq/xxxx/xx.xml", "scthref": "/sct/xxxx/xx.xml", "scchref": "/scc/xxxx/xx.xml"}
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
        log_result('API_SCS_UPDATE_VERSION_PUT', '下发版本更新通知', url, response, result, data)


def API_SCS_MYCUSTOMER_LIST_GET():
    url = scsurl + '/api/v1/sellercus?sellerno=10001&officeid=' + str(officeid)
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
        log_result('API_SCS_MYCUSTOMER_LIST_GET', '直销助手-我的客户', url, response, result)


def API_SCS_ORDER_LIST_GET():
    url = scsurl + '/api/v1/policy?policyno=10001&officeid=' + str(officeid)
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
        log_result('API_SCS_ORDER_LIST_GET', '直销助手-保单查询', url, response, result)


def API_SCS_MYORDER_LIST_GET():
    url = scsurl + '/api/v1/sellerpolicy?sellerno=10001&sdate=20150101&edate=20150302&officeid=' + str(
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
        log_result('API_SCS_MYORDER_LIST_GET', '直销助手-我的签单-生效日期', url, response, result)


def API_SCS_SCQIP_SUBMIT(scqmac='F48E388E8449'):
    url = scsurl + '/api/v1/office/scqip'
    form_data = [('scqip', scqurl[7:-5]), ("scqport", scqurl[-4:]), ('officeid', str(officeid)),
                 ('scqmac', scqmac)]
    contenttype, formed_data = encode_multipart_formdata(form_data)
    code, response = public.httpmethod.Post(url, formed_data, headers={'Content-Type': contenttype})
    try:
        assert code == 200
        result = json.loads(response)
        assert result['errcode'] == 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_SCQIP_SUBMIT', '上报排队服务软件IP配置信息', url, response, result)


def API_SCS_OFFICE_GET():
    randomstr = ('abcdefghijklmnopqrstuvwxyz0123456789' + 'abcdefghijklmnopqrstuvwxyz0123456789')
    md5 = string.join(random.sample(randomstr, 32)).replace(' ', '')
    url = scsurl + '/api/v1/office?officeid=%s&confmd5=%s&warnrulesmd5=%s&' \
                   'businessesmd5=%s&windowsmd5=%s&tellersmd5=%s&sccconfmd5=%s&sctconfmd5=%s' % (
                       officeid, md5, md5, md5, md5, md5, md5, md5)
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
        log_result('API_SCS_OFFICE_GET', '获取指定营业厅的配置', url, response, result)
    result = json.loads(response)
    return result


def API_SCS_SCQIP_GET():
    url = scsurl + '/api/v1/office/' + officeid + '/scqip'
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
        log_result('API_SCS_SCQIP_GET', '获取营业厅对应的排队服务软件IP', url, response, result)


def API_SCS_TELLER_PUT():
    url = scsurl + '/api/v1/teller'
    data = {"oldpwd": teller_pwd, "newpwd": teller_pwd, "code": teller['code']}
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
        log_result('API_SCS_TELLER_PUT', '修改柜员密码', url, response, result, data)


def API_SCS_CITYLIST_GET():
    url = scsurl + '/api/v1/cities'
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
        log_result('API_SCS_CITYLIST_GET', '获取全国城市列表', url, response, result)


def API_SCS_WINDOWLIST_GET():
    url = scsurl + '/api/v1/city/%s/window' % city['name']
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
        log_result('API_SCS_WINDOWLIST_GET', '获取指定城市的窗口列表', url, response, result)


def API_SCS_REPORTS_BUSINESS_TIMELINE_GET():
    url = scsurl + '/api/v1/reports/business/timeline?id=%s' % business['_id']
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_BUSINESS_TIMELINE_GET', '获取业务打点流程', url, response, result)


def API_SCS_REPORTS_APPOINTMENT_DETAIL_GET():
    url = scsurl + '/api/v1/reports/appointment/detail?' + daterange + '&filterKey=p&limit=10&sort={"p":"asc"}&start=0'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_APPOINTMENT_DETAIL_GET', '获取预约明细报表', url, response, result)


def API_SCS_REPORTS_APPOINTMENT_LINE_GET():
    url = scsurl + '/api/v1/reports/appointment/line?' + daterange + filterp
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_APPOINTMENT_LINE_GET', '获取预约时间分布', url, response, result)


def API_SCS_REPORTS_BUSINESS_DETAIL_GET():
    url = scsurl + '/api/v1/reports/business/detail?' + daterange + '&evaluate=0' + filterp + '&limit=10&start=0'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_BUSINESS_DETAIL_GET', '获取业务明细报表', url, response, result)


def API_SCS_REPORTS_BUSINESS_STATICSTICS_GET():
    url = scsurl + '/api/v1/reports/business/statistics?' + daterange + filterp + '&grouptype=t&limit=10&start=0'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_BUSINESS_STATICSTICS_GET', '获取业务统计报表', url, response, result)


def API_SCS_REPORTS_BUSINESS_LINE_GET():
    url = scsurl + '/api/v1/reports/business/line?' + daterange + '&grouptype=p&limit=10&p=%s' % province['name']
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_BUSINESS_LINE_GET', '获取业务统计趋势', url, response, result)


def API_SCS_REPORTS_BUSINESS_PIE_GET():
    url = scsurl + '/api/v1/reports/business/pie?' + daterange + '&grouptype=p&limit=10&p=%s' % province['name']
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_BUSINESS_PIE_GET', '获取业务统计比例', url, response, result)


def API_SCS_REPORTS_AVGWAITDURATION_STATISTICS_GET():
    url = scsurl + '/api/v1/reports/avgwaitduration/statistics?' + daterange + filterp + '&grouptype=p&limit=10&start=0'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_AVGWAITDURATION_STATISTICS_GET', '获取平均等候时长统计报表', url, response, result)


def API_SCS_REPORTS_AVGWAITDURATION_LINE_GET():
    url = scsurl + '/api/v1/reports/avgwaitduration/line?' + daterange + '&grouptype=c&p=' + province[
        'name'] + '&c=' + \
          city['name']
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_AVGWAITDURATION_LINE_GET', '获取平均等候时长统计趋势', url, response, result)


def API_SCS_REPORTS_AVGTRANDURATION_STATISTICS_GET():
    url = scsurl + '/api/v1/reports/avgtranduration/statistics?' + daterange + filterp + '&grouptype=o&limit=10&start=0'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_AVGTRANDURATION_STATISTICS_GET', '获取平均办理时长统计报表', url, response, result)


def API_SCS_REPORTS_AVGTRANDURATION_LINE_GET():
    url = scsurl + '/api/v1/reports/avgtranduration/line?' + daterange + '&grouptype=o&p=' + province[
        'name'] + '&c=' + \
          city['name'] + '&o_id=' + str(officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_AVGTRANDURATION_LINE_GET', '获取平均办理时长统计趋势', url, response, result)


def API_SCS_REPORTS_TRANOVERTIME_STATISTICS_GET():
    url = scsurl + '/api/v1/reports/tranovertime/statistics?' + daterange + \
          '&filterKey=tc&filterValue=1&grouptype=t&limit=10&start=0'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_TRANOVERTIME_STATISTICS_GET', '获取办理超时率统计报表', url, response, result)


def API_SCS_REPORTS_TRANOVERTIME_LINE_GET():
    url = scsurl + '/api/v1/reports/tranovertime/line?' + daterange + '&grouptype=o&p=' + province['name'] + '&c=' + \
          city['name'] + '&o_id=' + str(officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_TRANOVERTIME_LINE_GET', '获取办理超时率统计趋势', url, response, result)


def API_SCS_REPORTS_WORKINGLOADRATE_STATISTICS_GET():
    url = scsurl + '/api/v1/reports/workingloadrate/statistics?' + daterange + \
          '&filterKey=tc&filterValue=1&grouptype=t&limit=10&start=0'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_WORKINGLOADRATE_STATISTICS_GET', '获取工作负荷指数统计报表', url, response, result)


def API_SCS_REPORTS_WORKINGLOADRATE_LINE_GET():
    url = scsurl + '/api/v1/reports/workingloadrate/line?' + daterange + '&grouptype=o&p=' + province[
        'name'] + '&c=' + \
          city['name'] + '&o_id=' + str(officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_WORKINGLOADRATE_LINE_GET', '获取工作负荷指数统计趋势', url, response, result)


def API_SCS_REPORTS_EVALUATIONRESULT_STATISTICS_GET():
    url = scsurl + '/api/v1/reports/evaluationresult/statistics?' + daterange + \
          '&filterKey=tc&filterValue=1&grouptype=t&limit=10&start=0'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_EVALUATIONRESULT_STATISTICS_GET', '获取评价结果统计报表', url, response, result)


def API_SCS_REPORTS_EVALUATIONRESULT_LINE_GET():
    url = scsurl + '/api/v1/reports/evaluationresult/line?' + daterange + '&grouptype=o&p=' + province[
        'name'] + '&c=' + \
          city['name'] + '&o_id=' + str(officeid)
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['list'] is not None
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_REPORTS_EVALUATIONRESULT_LINE_GET', '获取评价结果统计趋势', url, response, result)


def API_SCS_UPGRADE_DOWNLOAD_GET():
    url = scsurl + '/api/v1/upgrade/download?path=uploads/scq/%s/upgrade.xml' % upgrade_md5
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        assert response[0].find('filename=upgrade.xml') > 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_UPGRADE_DOWNLOAD_GET', '升级文件下载', url, response, result)


def API_SCS_UPGRADE_RESULT_PUT():
    url = scsurl + '/api/v1/upgrade/result'
    data = {'officeid': str(officeid),
            "result": [{
                'type': "SCQ",
                'md5': "xxxxxxxxxxxxx",
                'version': "xx.xx.xx.xx",
                'time': TODAY + " 17:49:50"
            }, {
                'type': "SCT",
                'md5': "xxxxxxxxxxxxx",
                'version': "xx.xx.xx.xx",
                'time': TODAY + " 17:49:50"
            }, {
                'type': "SCC",
                'windowid': window['_id'],
                'md5': "xxxxxxxxxxxxx",
                'version': "xx.xx.xx.xx",
                'time': TODAY + " 17:49:50"
            }]}
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
        log_result('API_SCS_UPGRADE_RESULT_PUT', '上报升级结果', url, response, result, data)


def API_SCS_RUNNING_STATUS_PUT():
    timestamp = str(int(round(time.time() * 1000))).replace('L', '-0')
    url = scsurl + '/office/?EIO=3&transport=polling&t=%s' % timestamp
    from public.httpmethod import opener
    wp = opener.open(url)
    meta = wp.info()
    id_pre = meta.getheaders('Set-Cookie')[0].split(';')[0]
    id_pre = id_pre[3:]
    url = scsurl + '/api/v1/runningstatus'
    data = {
        "id": '%s;%s' % (id_pre, officeid),
        "sct": {"ip": "", "status": "未连接"},
        "scc": [{"ip": "", "windowname": window['name'], "status": "正常"}],
        "sce": [{"ip": "", "windowname": window['name'], "status": "未连接"}],
        "scb": [{"ip": "", "boxno": "BOX00001", "status": "未连接"}]
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
        log_result('API_SCS_RUNNING_STATUS_PUT', '上报营业厅各个模块运行状态', url, response, result, data, comment='提交bug')


def API_SCS_CALLLOG_GET():
    url = scsurl + '/api/v1/customercalllog?idcard=' + vip_idcard + '&sdate=20150101&edate=20151202&officeid=' + str(
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
        log_result('API_SCS_CALLLOG_GET', '获取客户来电信息', url, response, result, comment='fujian接口')


def API_SCS_OFFICE_STRUCTURE_GET():
    url = scsurl + '/api/v1/office/structure/%s%s' % (city['no'], office['no'])
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
        log_result('API_SCS_OFFICE_STRUCTURE_GET', '根据机构编号获取营业厅的组织结构信息', url, response, result)


def API_SCS_ERRLOG_POST():
    url = scsurl + '/api/v1/errorlog'
    data = {
        "apiname": "获取微信服务号token",
        "apiowner": "自动化测试接口",
        "module": "第三方接口调用", "errcode": "20017",
        "errmsg": "request的get请求出错: connect ECONNREFUSED"}
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
        log_result('API_SCS_ERRLOG_POST', '上报错误日志', url, response, result, data)


def API_SCS_OFFICE_MONITOR_GET():
    url = scsurl + '/api/v1/office/monitor/%s' % officeid
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
        log_result('API_SCS_OFFICE_MONITOR_GET', '微信营业厅监控', url, response, result)


def API_SCS_ALL_OFFICES_GET():
    url = scsurl + '/api/v1/offices'
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
        log_result('AP3I_SCS_ALL_OFFICES_GET', '获取所有营业厅信息', url, response, result)


def API_SCS_OFFICE_EVALUATE_ADD():
    url = scsurl + '/api/v1/office/evaluate'
    data = {
        "province": province['name'],
        "city": city['name'],
        "officename": office['name'],
        "officeid": officeid,
        "customerphone": "97690500",
        "customername": normal_name,
        "customertype": "I",
        "customeridcard": normal_idcard,
        "attitude": "4",
        "environment": "3",
        "efficiency": "2",
        "note": "满意",
        "openid": "456789",
        "type": "wechat"
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
        log_result('API_SCS_OFFICE_EVALUATE_ADD', '新增营业厅评价', url, response, result, data)


def API_SCS_OFFICE_FLOW():
    url = scsurl + '/api/v1/office/flow'
    timestamp = str(int(round(time.time() * 1000))).replace('L', '-0')
    data = {
        "officeid": int(officeid),
        "time": timestamp
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
        log_result('API_SCS_OFFICE_FLOW', '营业厅流量查询', url, response, result, data, comment='接口未实现，待确认')


def API_SCS_ALL_DTDCONF_GET():
    url = scsurl + '/api/v1/dtdinfo'
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
        log_result('API_SCS_ALL_DTDCONF_GET', '获取所有上门服务配置、业务信息', url, response, result, comment='接口未实现')


def API_SCS_DTD_AUTH():
    url = scsurl + '/api/v1/dtdauth?idtype=I&idcard=%s' % normal_idcard
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
        log_result('API_SCS_DTD_AUTH', '客户上门服务认证', url, response, result, comment='接口未实现')


# 3
def API_SCS_CUSTOMER_PHOTO_POST():
    url = scsurl + '/api/v1/customer/photo'
    path = os.path.join(STUFF_DIR, '3.jpg')
    with open(path, 'r') as f:
        content = f.read()
    data = {
        "idtype": "I",
        "idcard": normal_idcard,
        "wlt": "",
        "validperiod": "",
        "file": os.path.join(STUFF_DIR, '3.jpg'),
        "filestream": os.path.join(STUFF_DIR, '3.jpg')
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
        log_result('API_SCS_CUSTOMER_PHOTO_POST', '57.客户照片上传', url, response, result, data, comment='真实照片未实现')


# 2
def API_SCS_CUSTOMER_PHOTO_GET(idcard=normal_idcard):
    url = scsurl + '/api/v1/customer/photo?idcard=%s' % idcard
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        assert response[0].find('filename') > 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_CUSTOMER_PHOTO_GET', '58.客户照片获取', url, response, result, None, comment='已提交bug')


# 1
def API_SCS_OFFICE_IMAGE_GET():
    url = scsurl + '/api/v1/office/%s/image' % officeid
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        assert response[0].find('filename') > 0
        result = PASS
    except:
        result = FAIL
        mlogger.error(traceback.format_exc())
    finally:
        log_result('API_SCS_OFFICE_IMAGE_GET', '59.营业厅图片获取', url, response, result)


'''
def delete_office(idpath):
    url = scsurl + "/api/v1/settings/offices/" + idpath
    code, response = public.httpmethod.Delete(url, '', headers)
    log_result('delete_office', '删除组织结构 ', url, result, code)


def delete_business():
    for i in range(0, len(businesses)):
        url = scsurl + "/api/v1/settings/business?business_id=" + businesses[i][
            '_id'] + '&office_path=' + office_idpath
        code, response = public.httpmethod.Delete(url, '', headers)
        log_result('delete_business', '删除业务 ', url, result, code)


def delete_window():
    url = scsurl + "/api/v1/settings/window/" + window['_id']
    code, response = public.httpmethod.Delete(url, '', headers)
    log_result('delete_window', '删除窗口 ', url, result, code)


def delete_teller():
    url = scsurl + "/api/v1/settings/teller/%s" % officeid
    code, response = public.httpmethod.Get(url)
    log_result('delete_teller', '获取柜员列表 ', url, result, code)
    result = json.loads(result)
    for i in result:
        url = scsurl + "/api/v1/settings/teller/" + i['_id']
        code, response = public.httpmethod.Delete(url, '', headers)
        log_result('delete_teller', '删除柜员 ', url, result, code)


def delete_numberrule():
    for i in range(0, len(numberrule)):
        url = scsurl + "/api/v1/settings/numberrule/" + numberrule[i]['_id']
        code, response = public.httpmethod.Delete(url, '', headers)
        log_result('delete_numberrule', '删除号源 ', url, result, code)

def upload_bf():  # 未使用
    url = scsurl + '/api/v1/upload/upgradepackage?flowChunkNumber=1&flowChunkSize=1048576&flowCurrentChunkSize=51345&flowTotalSize=51345&flowIdentifier=51345-SCQ_Upgrade1000bf&flowFilename=SCQ_Upgrade(1.0.0.0).bf&flowRelativePath=SCQ_Upgrade(1.0.0.0).bf&flowTotalChunks=1'
    code, response = public.httpmethod.Get(url)
    try:
        assert code == 200
        result = json.loads(response)
        assert result['message'] == '文件需上传'
        url_2 = scsurl + '/api/v1/upload/upgradepackage'
        filename = 'SCQ_Upgrade(1.0.0.0).bf'
        filepath = os.path.join(STUFF_DIR, filename)
        filesize = str(os.path.getsize(filepath))
        form_data = [
            ('flowChunkNumber', '1'), ('flowChunkSize', '1048576'), ('flowCurrentChunkSize', filesize),
            ('flowTotalSize', filesize), ('flowIdentifier', filesize + '-' + filename.replace('.', '')),
            ('flowFilename', filename), ('flowRelativePath', filename), ('flowTotalChunks', '1'),
            ('file', "f'%s'" % filepath)
        ]
        contenttype, formed_data = encode_multipart_formdata(form_data)
        headers1 = {'Content-Type': contenttype}
        code, response = public.httpmethod.Post(url_2, formed_data, headers1)
        assert code == 200
        result = json.loads(response)
        assert result['md5'] is not None
        result = PASS
    except:
        result = FAIL
    finally:
        log_result('upload_bf', '上传升级文件', url, response, result, data=filename)
'''


def test_scs_api():
    login()
    test_add_teller_photo()
    API_SCS_CUSTOMERRECORD_SUBMIT()
    API_SCS_CUSTOMERRECORD_GET()
    API_CUS_CALLLOG_GET()
    API_SCS_CUSTOMER_AUTH()
    API_APPLYORDER_OF_TELLER_GET()
    API_SCS_CUSTOMER_OF_NAME_GET()
    API_SCS_CUSTOMERRECORD_LIST_GET()
    API_SCS_NUMBERRULE_GET()
    API_SCS_STUFF_GET()
    API_SCS_QUEUE_GET()
    API_SCS_OFFICEWAITCOUNT_GET()
    API_SCS_OFFICEWAITDETAIL_GET()
    API_SCS_TELLERLOG_SUBMIT()
    API_SCS_RAINBOW_NOTICE()
    API_SCS_APPOINTMENT_ADD()
    API_SCS_CHECK_VERSION_GET()
    API_SCS_UPDATE_VERSION_PUT()
    API_SCS_MYCUSTOMER_LIST_GET()
    API_SCS_ORDER_LIST_GET()
    API_SCS_MYORDER_LIST_GET()
    API_SCS_SCQIP_SUBMIT()
    API_SCS_OFFICE_GET()
    API_SCS_SCQIP_GET()
    API_SCS_TELLER_PUT()
    API_SCS_CITYLIST_GET()
    API_SCS_WINDOWLIST_GET()
    API_SCS_REPORTS_BUSINESS_TIMELINE_GET()
    API_SCS_REPORTS_APPOINTMENT_DETAIL_GET()
    API_SCS_REPORTS_APPOINTMENT_LINE_GET()
    API_SCS_REPORTS_BUSINESS_DETAIL_GET()
    API_SCS_REPORTS_BUSINESS_STATICSTICS_GET()
    API_SCS_REPORTS_BUSINESS_LINE_GET()
    API_SCS_REPORTS_BUSINESS_PIE_GET()
    API_SCS_REPORTS_AVGWAITDURATION_STATISTICS_GET()
    API_SCS_REPORTS_AVGWAITDURATION_LINE_GET()
    API_SCS_REPORTS_AVGTRANDURATION_STATISTICS_GET()
    API_SCS_REPORTS_AVGTRANDURATION_LINE_GET()
    API_SCS_REPORTS_TRANOVERTIME_STATISTICS_GET()
    API_SCS_REPORTS_TRANOVERTIME_LINE_GET()
    API_SCS_REPORTS_WORKINGLOADRATE_STATISTICS_GET()
    API_SCS_REPORTS_WORKINGLOADRATE_LINE_GET()
    API_SCS_REPORTS_EVALUATIONRESULT_STATISTICS_GET()
    API_SCS_REPORTS_EVALUATIONRESULT_LINE_GET()
    API_SCS_UPGRADE_DOWNLOAD_GET()
    API_SCS_UPGRADE_RESULT_PUT()
    API_SCS_RUNNING_STATUS_PUT()
    API_SCS_CALLLOG_GET()
    API_SCS_OFFICE_STRUCTURE_GET()
    API_SCS_ERRLOG_POST()
    API_SCS_OFFICE_MONITOR_GET()
    API_SCS_ALL_OFFICES_GET()
    API_SCS_OFFICE_EVALUATE_ADD()
    API_SCS_OFFICE_FLOW()
    API_SCS_ALL_DTDCONF_GET()
    API_SCS_DTD_APPOINTMENT_ADD()
    API_SCS_DTD_AUTH()
    API_SCS_CUSTOMER_PHOTO_POST()
    API_SCS_CUSTOMER_PHOTO_GET()
    API_SCS_OFFICE_IMAGE_GET()
    idcard = newidcard()
    ticket = API_SCS_TICKET_ADD(idcard, business['_id'], isvip=False)
    API_SCS_APPOINTMENT_STATUS(idcard)
    API_SCS_TICKET_AUTH(idcard)
    API_SCS_TICKETLOG_SUBMIT(ticket)

if __name__ == '__main__':
    test_scs_api()
