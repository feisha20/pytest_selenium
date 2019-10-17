#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys

project_folder = os.getcwd()[0:os.getcwd().find("pytest_selenium")]
sys.path.append(project_folder + "pytest_selenium")
sys.path.append(project_folder + "pytest_selenium//util")
sys.path.append(project_folder + "pytest_selenium//page")

import pytest
from py._xmlgen import html

driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    outcome = yield
    pytest_html = item.config.pluginmanager.getplugin('html')

    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):  # 失败截图
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    extra.append(pytest_html.extras.text('some string', name='Different title'))
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码


def capture_screenshot():
    '''截图保存为base64'''
    return driver.get_screenshot_as_base64()


def pytest_configure(config):
    # 添加项目地址与项目名称
    config._metadata["项目名称"] = "Pytest自动化项目"
    config._metadata['项目地址'] = 'http://aatp.topideal.work'
    # 删除没有必要的环境变量
    config._metadata.pop("JAVA_HOME")

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("公司: 卓志厦门研发中心")])
    prefix.extend([html.p("部门: 测试部")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('描述'))
    cells.pop(-1)  # 删除link列header


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop(-1)  # 删除link列
