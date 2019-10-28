# -*- encoding: utf-8 -*-
import time, urllib2, cookielib
from LogMethod import mlogger as mlogger
from urllib2 import Request, urlopen, URLError, HTTPError
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)


def getTime():
    '''获取当前时间的时间戳，并以一定的形式显示'''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def Put(url, data, headers=None):
    '''HTTP请求-PUT方法'''
    mlogger.debug('请求    ' + url)
    mlogger.debug('数据    ' + str(data))
    req = urllib2.Request(url, data, headers)
    req.get_method = lambda: 'PUT'
    return execute(req)


def Post(url, data, headers=None):
    '''HTTP请求-POST方法'''
    mlogger.debug('请求    ' + url)
    mlogger.debug('数据    ' + str(data))
    req = urllib2.Request(url, data, headers)
    return execute(req)


def Get(url):
    '''HTTP请求-GET方法'''
    mlogger.debug('请求    ' + url)
    return execute(url)


def Delete(url, data=None, headers=None):
    '''HTTP请求-DELETE方法'''
    mlogger.debug('请求    ' + url)
    mlogger.debug('数据    ' + str(data))
    if data is None:
        req = urllib2.Request(url)
    elif headers is None:
        req = urllib2.Request(url, data)
    else:
        req = urllib2.Request(url, data, headers)
    req.get_method = lambda: 'DELETE'
    return execute(req)


def getcode(req):
    code = ''
    content = ''
    try:
        wp = opener.open(req)
        code = wp.getcode()
    except URLError, e:
        if hasattr(e, 'reason'):
            content = e.reason
        if hasattr(e, 'code'):
            code = e.code
    finally:
        mlogger.debug('结果    ' + str(code) + ' ' + str(content))
        return code, content


def execute(req):
    code = ''
    content = ''
    try:
        wp = opener.open(req)
        content = wp.read()
        code = wp.getcode()
        meta = wp.info()
        if meta.getheaders('Content-Disposition') != list():
            content = meta.getheaders('Content-Disposition')
    except URLError, e:
        if hasattr(e, 'reason'):
            content = e.reason
        if hasattr(e, 'code'):
            code = e.code
    finally:
        mlogger.debug('结果    ' + str(code) + ' ' + str(content))
        return code, content
