# -*- coding=UTF-8 -*-
import oper
import check
import browser


class Baidu:
    url = "http://www.baidu.com"  # 百度地址
    tb_keyword = "x, //*[@id='kw']"  # 百度输入框
    btn_search = "x, //*[@id='su']"  # 百度按钮
    lk_news = "x, //a[@name='tj_trnews']"  # 百度新闻链接
    nums_text = "x, //span[@class='nums_text']"  # 百度搜索结果数量


def home():
    """打开百度首页"""
    browser.open(Baidu.url)


def search(keyword):
    """输入关键字搜索"""
    oper.type(Baidu.tb_keyword, keyword)
    oper.click(Baidu.btn_search)


def get_search_result():
    """获取搜索的结果数量"""
    check.wait_element(Baidu.nums_text)
    result = oper.get_text(Baidu.nums_text)
    print(result)

