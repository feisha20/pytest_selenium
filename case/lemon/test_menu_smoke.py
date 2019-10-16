# -*- coding=UTF-8 -*-
from page import login_page
from page import home_page
from page import common_page
import browser
import pytest
import sys
import get


@pytest.fixture(scope="module")
def setup():
    login_page.login("admin", "Aa123456", "999999")
    yield
    browser.stop()


# 遍历系统所有菜单
def test_menu(setup):
    menu_list = get.get_test_data("menu.yaml")
    menu = list(menu_list.keys())
    for i in range(len(menu)):
        menu1 = menu[i]
        print(menu1)
        home_page.click_menu(menu1)
        item = str(menu_list[menu1]).split(",")
        for ii in range(len(item)):
            item1 = item[ii]
            print("--" + item1)
            home_page.click_item(item1)
            common_page.is_loading()


if __name__ == '__main__':
    pytest.main([sys.argv[0]])
