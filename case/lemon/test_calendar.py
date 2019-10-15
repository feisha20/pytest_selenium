from page import login_page
from page import home_page
from page import calendar_page
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


# 新增节假日
@pytest.mark.parametrize("addr", ["香港", "澳门"])
@pytest.mark.parametrize("desc", ["这是节假日描述"])
def test_add_calendar(addr, desc, setup, setup_function):
    home_page.goto_calendar_page()
    calendar_page.tab12()
    calendar_page.add_page()
    time.sleep(2)
    calendar_page.save_calendar(addr, desc)


# 删除节假日
@pytest.mark.parametrize("addr", ["香港"])
def test_del_calendar(addr, setup, setup_function):
    num = calendar_page.search_by_addr(addr)
    time.sleep(1)
    print("删除前查询到数据" + addr + num)
    calendar_page.del_calendar()
    time.sleep(1)
    num2 = calendar_page.get_list_num()
    print("删除后查询到数据" + addr + num2)


if __name__ == '__main__':
    pytest.main([sys.argv[0]])
