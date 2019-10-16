# -*- coding=UTF-8 -*-
import oper
import check
import time

class Calendar:
    list_tab1 = "x, //*[@id='activeTabKey']/label[1]/span[1]"  # tab1 世界日历
    list_tab2 = "x, //*[@id='activeTabKey']/label[2]"  # tab2 节假日管理
    add_btn = "x, //*[@id='main']/div[2]/div/div/div/div[2]/div/button"  # 新增按钮
    date_input = "x, /html[1]/body[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/input[1]"  # 节假日期
    addr_input = "x, //div[@class='item']//input[@id='areaAddress']"  # 地区
    holidayDesc_input = "x, //div[@class='item']//input[@id='holidayDesc']"  # 节日描述
    save_btn = "x, /html/body/div[2]/div/div[2]/div/div[1]/div[3]/button[1]"  # 保存按钮
    cancel_btn = "x, /html/body/div[2]/div/div[2]/div/div[1]/div[3]/button[2]"  # 返回按钮
    search_addr_input = "x, //*[@id='areaAddress']"  # 搜索-地址
    search_btn = "x, //*[@id='main']/div[2]/div/div/div/div[2]/form/div[4]/div/div/button"  # 搜索-按钮
    list_del_btn = "x, //*[@id='main']/div[2]/div/div/div/div[3]/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[7]/span/a[2]"
    comfirm_btn = "x, /html/body//*/div/div/div/div[2]/div/div/div[2]/button[2]"
    list_nums_text = "x, //*[@id='main']/div[2]/div/div/div/div[3]/div[1]/div/div/ul/li[1]"


def tab1():
    """切换到世界日历TAB"""
    oper.click(Calendar.list_tab1)


def tab12():
    """切换到日历管理TAB"""
    oper.click(Calendar.list_tab2)


def add_page():
    """打开新增页面"""
    oper.click(Calendar.add_btn)


def save_calendar(addr, desc):
    """保存节假日"""
    oper.type(Calendar.addr_input, addr)
    oper.type(Calendar.holidayDesc_input, desc)
    oper.click(Calendar.save_btn)


def search_by_addr(addr):
    """根据地区搜索"""
    oper.type(Calendar.search_addr_input, addr)
    oper.click(Calendar.search_btn)


def del_calendar():
    """删除节假日"""
    if check.wait_element(Calendar.list_del_btn):
        oper.click(Calendar.list_del_btn)
        oper.click(Calendar.comfirm_btn)
    else:
        print("没有数据，无法删除")


def get_list_num():
    """获取列表条数"""
    num = oper.get_text(Calendar.list_nums_text)
    return num