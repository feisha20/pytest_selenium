# -*- coding=UTF-8 -*-
from page import login_page
from page import home_page
from page import calendar_page
from page import common_page
import browser
import pytest
import sys
import time


@pytest.fixture(scope="module")
def setup():
    login_page.login("admin", "Aa123456", "999999")
    yield
    browser.stop()


@pytest.fixture(scope="function")
def setup_function():
    yield
    browser.get_selenium().refresh()


@pytest.mark.parametrize("addr", ["香港", "澳门"])
@pytest.mark.parametrize("desc", ["这是节假日描述"])
def test_add_calendar(addr, desc, setup, setup_function):
    """ 新增节假日"""
    home_page.goto_page("基础资料", "日历管理")
    calendar_page.tab12()
    calendar_page.add_page()
    time.sleep(2)
    calendar_page.save_calendar(addr, desc)


# def test_get_list_data(setup, setup_function):
#     """获取列表数据"""
#     time.sleep(3)
#     data = []
#     for i in range(2,7):
#         data_cell = common_page.table(1, i)
#         data.append(data_cell)
#     nums = common_page.table_num()
#     print("第一行数据：" + str(data))
#     print("列表数据总数为：" + str(nums))
#
#
# @pytest.mark.parametrize("addr", ["香港"])
# def test_del_calendar(addr, setup, setup_function):
#     """删除节假日"""
#     calendar_page.search_by_addr(addr)
#     num = common_page.table_num()
#     time.sleep(1)
#     print("删除前查询到数据" + addr + str(num))
#     calendar_page.del_calendar()
#     time.sleep(1)
#     num2 = common_page.table_num()
#     print("删除后查询到数据" + addr + str(num2))


if __name__ == '__main__':
    pytest.main([sys.argv[0]])
