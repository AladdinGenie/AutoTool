# coding:utf-8

import time
import os
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
ROOT_PATH = os.path.dirname(CURRENT_PATH)
TARGET_DIR = os.path.join(ROOT_PATH, 'report')
MODEL = os.path.join(TARGET_DIR, 'model.html')
START_TIME = time.localtime()


def reformat(parm):
    """
    针对多步骤的用例，如步骤、检查点、实际结果
    1、连续两次逗号的，中间用-来分隔
    2、以逗号结尾的，以-来结尾
    3、逗号替换为一条横线
    """
    if isinstance(parm, str):
        parm = parm.replace(',,', ',-,').replace(',,', ',-,')
        if parm.endswith(','):
            parm += '-'
        parm = parm.replace(',', '<hr/>')
    return parm


def parse_head():
    return '''<tr>
                  <th>序号</th>
                  <th>接口编号</th>
                  <th>用例描述</th>
                  <th>接口url</th>
                  <th class="test_result">结果</th>
                  <th>详情</th>
                  <th>备注</th>
                </tr>'''


class HtmlReport:
    def __init__(self, project, version, debug=True):
        try:
            self.begin = datetime.datetime.now()
            self.test_time = time.strftime("%Y-%m-%d %H:%M:%S", START_TIME)
            reportname = 'report.html' if debug else 'report_%s.html' % time.strftime("%Y%m%d%H%M%S", START_TIME)
            self.output = os.path.join(TARGET_DIR, reportname)
            self.index = 0
            with open(MODEL) as f:
                html = f.read()
                html = html.replace('{{project}}', project)
                html = html.replace('{{version}}', version)
                html = html.replace('{{date}}', self.test_time)
                html = html.replace('{{content_head}}', parse_head())
            with open(self.output, 'w+') as f:
                f.write(html)
        except:
            raise

    def finish(self):
        try:
            runtime = str(datetime.datetime.now() - self.begin).split('.')[0]
            with open(self.output, 'r+') as f:
                html = f.read()
                html = html.replace('{{runtime}}', runtime)
                html = html.replace('{{content_code}}', '')
                with open(self.output, 'w+') as f1:
                    f1.write(html)
        except:
            raise

    def add_record(self, result):
        try:
            self.index += 1
            # result['checkpoint'] = reformat(result['checkpoint'])
            # result['response'] = reformat(result['response'])
            # result['step'] = reformat(result['step'])
            detail = '''数据：%s</br>返回值：%s''' % (result['data'], result['response'])
            new = '''{{content_code}}<tr class="test_case"><td name="序号" class="index">%s</td>''' % self.index
            new += '''<td class="id">%s</td>''' % result['id']
            new += '''<td class="">%s</td>''' % result['description']
            new += '''<td class="">%s</td>''' % result['url']
            new += '''<td class="result" value="%s"></td>''' % result['result']  # 显示图片，fail, pass, notRun
            new += '''<td><a data-toggle="expand" data-target="#detail%d">查看</a></td>''' % self.index
            new += '''<td class="comment" contenteditable="true">%s</td>''' % result['comment']
            new += '''</tr>
                <tr>
                    <td colspan="7" id="detail%d" class="expand hide">
                        <div class="detail_info">%s</div>
                    </td>
                </tr>''' % (self.index, detail)
            # if result['result'] != 'pass':
            #     new += '''<td><a data-toggle="expand" data-target="#detail%d">查看</a></td></tr>''' % self.index
            #     new += ''' <tr><td colspan="11" id="detail%d" class="expand hide"><div class="detail_info">%s
            #     </div></td></tr>''' % (self.index, result['error'])
            # else:
            #     new += '''<td><a data-toggle="expand" data-target=""></a></td></tr>'''
            with open(self.output, 'r+') as f:
                html = f.read()
                html = html.replace('{{content_code}}', new)
                with open(self.output, 'w+') as f1:
                    f1.write(html)
        except:
            raise
