# -*- encoding: utf-8 -*-

import logging
import os
CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
ROOT_PATH = os.path.dirname(CURRENT_PATH)
LOG_DIR = os.path.join(ROOT_PATH, 'log')


class MyClass(object):
    def __init__(self, logfile):
        '''
        Constructor
        '''
        #         %(filename)s
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s [%(levelname)-8s] %(message)s',
                            datefmt='%a,%Y-%m-%d %H:%M:%S',
                            filename=logfile,
                            filemode='w')
        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(logging.Formatter('%(levelname)-8s %(message)s'))
        logging.getLogger('').addHandler(console)
        pass

    def debug(self, log, coding='utf-8'):
        try:
            logging.debug(str(log).decode(coding))
        except:
            pass

    def info(self, log, coding='utf-8'):
        logging.info(str(log).decode(coding))

    def warn(self, log, coding='utf-8'):
        logging.warning(str(log).decode(coding))

    def error(self, log, coding='utf-8'):
        logging.error(str(log).decode(coding))


mlogger = MyClass(os.path.join(LOG_DIR, 'run.log'))
