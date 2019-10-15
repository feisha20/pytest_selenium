#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import find
import browser
import re


# 等待某个元素出现
def wait_element(elementSequence, timeout=10):
    def _wait_element():
        return exist_element(elementSequence)

    return handleTimeout(_wait_element, timeout)


# 等待某个元素消失
def wait_element_disappear(elementSequence, timeout=10):
    def _wait_element_disappear():
        return not exist_element(elementSequence)

    return handleTimeout(_wait_element_disappear, timeout)


# 等待某段文字出现
def wait_text(content, timeout=10):
    def _wait_text():
        return exist_text(content)

    return handleTimeout(_wait_text, timeout)


# 等待某段文字消失
def wait_text_disappear(content, timeout=10):
    def _wait_text_disappear():
        return not exist_text(content)

    return handleTimeout(_wait_text_disappear, timeout)


# 判断元素是否存在
def exist_element(elementSequence):
    try:
        if find.element(elementSequence):
            return True
    except:
        return False


def displayed_element(elementSequence):
    try:
        if find.element(elementSequence).is_displayed():
            return True
    except:
        return False


# 判断页面是否存在iframe
def exist_iframe(iframe=None):
    try:
        if not iframe:
            return find.element("t,iframe")
        else:
            return find.element(iframe)
    except:
        return False


# 判断文字是否存在
def exist_text(content):
    try:
        if find.element("x,//*[text()='" + content + "']").is_displayed():
            return True
    except:
        return False


# 定义系统异常
class SYSException(Exception):
    print(Exception)
    pass

# 判断是否有页面异常出现，并尝试恢复动作
def handleTimeout(func, timeout=10, *args, **paramMap):
    while timeout > 0:
        rst = None
        try:
            rst = func(*args, **paramMap)
            if exist_text("502 Bad Gateway"):
                rst = SYSException("页面异常502")
                break
            elif exist_text("HTTP Status 404 - "):
                rst = SYSException("页面异常404")
                break
            elif exist_text("500 - 系统发生内部错误."):
                rst = SYSException("页面异常500")
            elif exist_text("服务器理解客户的请求，但拒绝处理它"):
                rst = SYSException("403 错误")
            elif rst and not isExcept(rst):
                break
        except:
            browser.switch_iframe("Default")
            if rst and not isExcept(rst):
                break
        time.sleep(1)
        timeout -= 1
    if isExcept(rst):
        raise rst
    elif rst == None:
        raise SYSException("》》》》》方法没有返回值")
    elif rst:
        return rst


def isExcept(e, eType=Exception):
    return isinstance(e, eType)


def getTimeout():
    return 120

# 验证邮箱格式
def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0