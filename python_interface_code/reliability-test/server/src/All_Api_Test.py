# coding: utf-8
from unittest import TestCase
from component.scs import *
from component.scq import *
from component.sce import *
from component.scb import *
from component.scw import *
from component.scc import *
from component.sca import *
from env.setting import *
import traceback


def evaluation_local(ticket):  # 本地评价
    ticketid = ticket['ticketid']
    API_SCQ_EVALUATION_PUT(ticketid, value=1)  # 评价
    API_SCS_TICKET_EVALUATION_PUT(ticket)


def call_local(ticket):  # 本地呼叫-欢迎
    time.sleep(5)
    ticketid = ticket['ticketid']
    assert ticketid is not None
    API_SCQ_TELLER_LOGINSTATUS()
    API_SCQ_TICKET_STATUS_PUT(ticketid, 'DOING')
    API_SCQ_REQUEST_WELCOME(ticketid)  # 欢迎
    API_SCQ_IDCARD_BIND(ticketid)  # 更新票的身份证号码
    API_SCQ_TICKET_STATUS_PUT(ticketid, 'DONE')


class ChinaLifeTest(TestCase):
    @classmethod
    def setUpClass(self):
        # restart_scq()
        # restart_scc()
        # restart_smartcounterwechat()
        pass

    def test_zzz_api(self):
        try:
            ticket = API_SCS_TICKET_ADD(newidcard(), businessid=business['_id'], isvip=False)
            API_SCA_TICKET_STATUS_PUT_V2(ticket=ticket)
            test_scq_api()
            test_sca_api()
            test_scb_api()
            test_scc_api()
            test_sce_api()
            test_scs_api()
            test_scw_api()
        except:
            mlogger.error(traceback.format_exc())

    def test_local_ticket_and_call(self):
        mlogger.info('\n\n----------TestCase: 本地-遍历取票----------\n')
        login()
        set_officeconf()
        update_baseconf(rule2=True)
        for operate in operations:
            try:
                ticket = API_SCQ_TICKET_ADD(operate['business'], operate['idcard'])
                assert ticket['errcode'] == 0
                call_local(ticket)
                evaluation_local(ticket)
            except:
                mlogger.error(traceback.format_exc())

    def test_local_ticket_and_yitihua(self):
        mlogger.info('\n\n----------TestCase: 本地一体化-遍历取票----------\n')
        restart_scq()
        restart_scc(mode='evaluation')
        try:
            for operate in operations:
                ticket = API_SCQ_TICKET_ADD(operate['business'], operate['idcard'])
                assert ticket is not None
                call_local(ticket)
                API_SCC_EVALUATOR_EVALUATION(ticket)
                API_SCC_EVALUATION_SUBMIT(ticket)
        except:
            mlogger.error(traceback.format_exc())
        finally:
            restart_scc()

    def test_local_ticket_and_discard(self):
        mlogger.info('\n\n----------TestCase: 弃票----------\n')
        ticket = API_SCQ_TICKET_ADD(business, newidcard())
        assert ticket is not None
        ticketid = ticket['ticketid']
        import time
        time.sleep(10)
        API_SCC_TICKET_PUT(ticketid)
        API_SCC_TICKET_DEL(ticketid)
        API_SCQ_TICKET_STATUS_PUT(ticketid, 'DISCARD')

    def test_local_ticket_and_trans(self):
        mlogger.info('\n\n----------TestCase: 转移业务----------\n')
        assert business is not None
        assert vipbusiness is not None
        ticket = API_SCQ_TICKET_ADD(business, newidcard())
        assert ticket is not None
        ticketid = ticket['ticketid']
        API_SCQ_TICKET_TRANSFER(ticketid, business, vipbusiness)

    def test_wechat_ticket_and_local_call(self):
        mlogger.info('\n\n----------TestCase2: 微信遍历预约-本地取票-本地叫号-本地评价----------\n')
        login()
        set_officeconf()
        update_baseconf(rule2=False)
        for operate in operations:
            response = scw_appoint2017(operate['business'], operate['idcard'], operate['phone'])
            assert response['message'] == "预约成功"
            number = response['number']
            ticket = API_SCQ_TICKET_ADD(idcard=operate['idcard'], number=number)
            call_local(ticket)
            evaluation_local(ticket)

    def test_wechat_ticket_and_wechat_call(self):
        mlogger.info('\n\n----------TestCase: 微信预约取票-本地取票-本地叫号-远程评价----------\n')  # 只有手机虚拟取号的才有微信叫号流程
        idcard = newidcard()
        response = scw_appoint2017(business, idcard, newphone)
        API_SCS_APPOINTMENT_STATUS(idcard)
        assert response['message'] == "预约成功"
        number = response['number']
        ticket = API_SCQ_TICKET_ADD(idcard=idcard, number=number)
        assert ticket is not None
        call_local(ticket)
        API_SCW_EVALUATION_REQUEST(ticket['ticketid'], number)  # 评价

    def test_wechat_appoint_and_del(self):
        mlogger.info('\n\n----------TestCase: 微信预约-取消预约----------\n')
        idcard = newidcard()
        response = scw_appoint2017(business, idcard, newphone)
        assert response['message'] == "预约成功"
        number = response['number']
        API_SCS_APPOINTMENT_PUT(number)  # 2017-7-28
        API_SCW_APPOINTMENT_PUT(number)  # 暂未实现
        API_SCS_APPOINTMENT_DEL(number)  # 2017-7-28

    def test_wechat_ticket_and_discard(self):
        mlogger.info('\n\n----------TestCase2: 微信预约-本地取票-弃票----------\n')
        idcard = newidcard()
        response = scw_appoint2017(business, idcard, newphone)
        assert response['message'] == "预约成功"
        number = response['number']
        ticket = API_SCQ_TICKET_ADD(idcard=idcard, number=number)
        assert ticket is not None
        ticketid = ticket['ticketid']
        import time
        time.sleep(10)
        API_SCQ_TICKET_STATUS_PUT(ticketid, 'DISCARD')

    def test_wechat_shake_and_wechat_ticket(self):
        mlogger.info('\n\n----------TestCase: 摇一摇取票-远程叫号-远程评价----------\n')
        ticket = None
        ticketnumber = scw_shake_ticket()['data']
        for t in API_SCQ_TELLER_LOGINSTATUS()['tickets']:
            if t['ticketnumber'] == ticketnumber:
                ticket = t
                break
        ticketid = ticket['ticketid']
        API_SCQ_TICKET_STATUS_PUT(ticketid, 'DOING')
        API_SCW_TICKET_STATUS_PUT(ticketid, 'DONE')
        scwid = scw_ticket2_get(ticketnumber)
        scw_ticket_evaluation_put(scwid)
