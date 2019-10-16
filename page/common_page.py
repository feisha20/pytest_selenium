# -*- coding=UTF-8 -*-
import oper
import check


class List:
    """列表xpath"""
    list_table = "x, //*/table[1]/tbody[1]"  # 表格table
    list_num = "x, /html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]//*/ul[1]/li[1]"

class load:
    loading = "x, //span[@class='ant-spin-dot']"


def table(row, col):
    """根据表格的横纵坐标获取数据"""
    grid_xpath = List.list_table + "/tr[" + str(row) + "]/td[" + str(col) + "]"
    data = oper.get_text(grid_xpath)
    return data


def table_num():
    """获取表格的数据总数"""
    num_text = oper.get_text(List.list_num)
    num = int(num_text.split(" ")[1])
    return num

def is_loading():
    check.wait_element_disappear(load.loading)
