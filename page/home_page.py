# -*- coding=UTF-8 -*-
import oper
import check

class Menu:
    """顶部导航菜单"""
    m_base = "l, 基础资料"
    m_risk = "l, 风险管理"


class Item:
    """侧边栏菜单"""
    i_calendar = "x, //*[@id='root']/div/div/aside/div/ul/li[1]/a"  # 日历管理
    i_enterprise = "x, //*[@id='root']/div/div/aside/div/ul/li[2]/a"  # 企业管理


def goto_calendar_page():
    """进入日历管理页面"""
    check.wait_element(Menu.m_base)
    oper.click(Menu.m_base)
    oper.click(Item.i_calendar)

