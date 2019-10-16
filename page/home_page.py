# -*- coding=UTF-8 -*-
import oper


def goto_page(menu, item):
    """通过菜单名称打开相应的页面"""
    menu_xpath = "l," + str(menu)
    item_xpath = "l," + str(item)
    oper.click(menu_xpath)
    oper.click(item_xpath)


def click_menu(menu):
    """点击顶部菜单"""
    menu_xpath = "l," + str(menu)
    oper.click(menu_xpath)


def click_item(item):
    """点击侧边菜单"""
    item_xpath = "l," + str(item)
    oper.click(item_xpath)