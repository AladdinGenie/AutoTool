# -*- encoding: utf-8 -*-

import os
import time

result = ''  # 测试结果记录
count = 0  # 序号
CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
PARENT_DIR = os.path.dirname(CURRENT_PATH)
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
reportfile = os.path.join(PARENT_DIR, os.path.join('report', 'report%s.html' % today))
stuff_dir = os.path.join(PARENT_DIR, 'stuff')
if os.path.exists(reportfile):
    os.remove(reportfile)

'''生成HTML报告'''


def GetReport():
    global result
    f = open(os.path.join(stuff_dir, 'ReportHead'), 'r')
    reportHead = f.readlines()  # HTML报告头
    f.close()
    f = open(os.path.join(stuff_dir, 'ReportEnd'), 'r')
    reportEnd = f.readlines()  # HTML报告尾
    f.close()
    f = open(reportfile, 'w')
    f.writelines(reportHead)  # 写入头
    f.writelines(result)  # 测试结果记录
    f.writelines(reportEnd)  # 写入尾
    f.close()


def appendResult(id, desc, code, success, detail=''):
    global result
    global count
    count += 1  # 序号自增
    result += '<tr>'  # 表头
    result += '<td nowrap="nowrap">' + str(count) + '</td>'  # 数据（序号）
    result += '<td nowrap="nowrap">' + id + '</td>'  # 数据（接口编号）
    result += '<td nowrap="nowrap">' + desc + '</td>'  # 数据（功能描述）
    result += '<td nowrap="nowrap">' + str(code) + '</td>'  # 数据（返回码）
    if success:
        result += '<td nowrap="nowrap" bgcolor="##9BCD9B">' + '通过' + '</td>'
    else:
        result += '<td nowrap="nowrap" bgcolor="#EEAD0E">' + '不通过' + '</td>'  # 数据（结果）
    result += '<td>' + str(detail) + '</td>'  # 数据（详情）
    result += '</tr>'  # 表尾
