#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import browser
import check


def element(selector):
    if ',' not in selector:
        return browser.get_selenium().find_element_by_id(selector)
    selector_by = selector.split(',')[0]
    selector_value = selector.split(',')[1]
    selector_value = selector_value.replace(" ", "")

    try:
        if selector_by == "i" or selector_by == 'id':
            ele = browser.get_selenium().find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            ele = browser.get_selenium().find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            ele = browser.get_selenium().find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link':
            ele = browser.get_selenium().find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            ele = browser.get_selenium().find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            ele = browser.get_selenium().find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            ele = browser.get_selenium().find_element_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'selector_selector':
            ele = browser.get_selenium().find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
    except:
        raise check.SYSException("找不到元素")

    return ele
