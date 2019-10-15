#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium.webdriver.support.ui import Select
import find
import check

# 清空输入框的内容
def clear(element):
    if isinstance(element, str):
        find.element(element).clear()
    else:
        element.clear()


# 某个元素输入文本值
def type(element, text):
    check.wait_element(element)
    if isinstance(element, str):
        find.element(element).clear()
        find.element(element).send_keys(text)
    else:
        element.clear()
        element.send_keys(text)


# 点击某个元素
def click(element):
    check.wait_element(element)
    if isinstance(element, str):
        find.element(element).click()
    else:
        element.click()


# 获取某个元素的文本内容
def get_text(element):
    check.wait_element(element)
    if isinstance(element, str):
        return str(find.element(element).text)
    else:
        return element.text


# 获取元素的某个属性值
def get_attr(element, attribute):
    if isinstance(element, str):
        return find.element(element).get_attribute(attribute)
    else:
        return element.get_attribute(attribute)


# 选择下拉列表的某个选项
def select(element, label):
    if isinstance(element, str):
        return Select(find.element(element)).select_by_visible_text(label)
    else:
        el = Select(element)
        return el.select_by_visible_text(label)


def get_select_value(element):
    if isinstance(element, str):
        return Select(find.element(element)).first_selected_option.text
    else:
        el = Select(element)
        return el.first_selected_option.text


# def select_input(element, label):
#     location = str(element)
#     flag = False
#     if "select" in str(location):
#         click(location.replace("select", "div"))
#         time.sleep(1)
#         index = 1
#         while index:
#             option = location.replace("select", "ul/li")+"["+str(index)+"]"
#             if not check.exist_element(option):
#                 break
#             elif label == get_text(option):
#                 oper.click(option)
#                 flag = True
#                 break
#             index +=1
#         if not flag:
#             return check.SYSException("没有找到选项"+label)
#     else:
#         return check.SYSException("请输入正确的select下拉列表位置："+element)


