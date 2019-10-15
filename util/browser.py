#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import selenium.webdriver
import selenium.webdriver.common.action_chains
import selenium.webdriver.common.keys
import time
import find
import platform
import settings
import get

# 获取运行平台的类型
sysstr = platform.system()


# 获取chromedriver绝对路径
def get_chromedriver_path():
    if sysstr == "Windows":
        return str(settings.project_path + "/driver/chromedriver.exe")
    else:
        linux_chromedriver_path = get.get_conf["linux_browserdriver_path"]["chrome_driver_path_linux"]
        return linux_chromedriver_path


# 获取firefoxdriver绝对路径
def get_firefoxdriver_path():
    if sysstr == "Windows":
        return str(settings.project_path + "/driver/geckodriver.exe")
    else:
        linux_firefoxdriver_path = get.get_conf["linux_browserdriver_path"]["firefox_driver_path_linux"]
        return linux_firefoxdriver_path


# 获取iedriver绝对路径
def get_iedriver_path():
    if sysstr == "Windows":
        return str(settings.project_path + "/driver/IEDriverServer.exe")


selenium_browser = None


# 启动浏览器
def start_browser():
    browser = "Chrome"
    global selenium_browser
    if browser == "Chrome":
        chrome_driver = get_chromedriver_path()
        os.environ["webdriver.chrome.driver"] = chrome_driver
        option = selenium.webdriver.ChromeOptions()
        option.add_argument("--start-maximized")

        option.add_argument("--test-type")
        option.add_argument("--disable-web-security")
        selenium_browser = selenium.webdriver.Chrome(chrome_options=option,
                                                     executable_path=chrome_driver,
                                                     )
    elif browser == "Firefox":
        kill_firefox_process()
        firefox_driver = get_firefoxdriver_path()
        os.environ["webdriver.firefox.driver"] = firefox_driver
        selenium_browser = selenium.webdriver.Firefox(executable_path=firefox_driver)
    elif browser == "IE":
        kill_ie_process()
        ie_driver = get_iedriver_path()
        os.environ["webdriver.Ie.driver"] = ie_driver
        selenium_browser = selenium.webdriver.Ie(executable_path=ie_driver)
    return selenium_browser


# 打开url
def open(url=None):
    start_browser().get(url)


# 获取当前页的url
def get_url():
    url = selenium_browser.current_url
    return url


# 获取当前页的title
def get_title():
    title = selenium_browser.title
    return title


# 释放selenium对象，关闭driver和chrome进程
def stop():
    selenium_browser.close()


def kill_chrome_process():
    """杀掉谷歌进程"""
    killed = False
    # noinspection PyBroadException
    try:
        while not killed:
            o = os.popen('tasklist /FI "IMAGENAME eq chrome.exe"')
            text = str(o.read())
            if "chrome.exe" in text:
                os.popen("taskkill /im chrome.exe /F")
                time.sleep(1)
            else:
                killed = True
        killed = False
        while not killed:
            o = os.popen('tasklist /FI "IMAGENAME eq chromedriver.exe"')
            text = str(o.read())
            if "chromedriver.exe" in text:
                os.popen("taskkill /im chromedriver.exe /F")
                time.sleep(1)
            else:
                killed = True
    except:
        print("进程chrome.exe 或者 chromedriver.exe不存在")


def kill_firefox_process():
    """杀掉Firefox进程"""
    killed = False
    # noinspection PyBroadException
    try:
        while not killed:
            o = os.popen('tasklist /FI "IMAGENAME eq firefox.exe"')
            text = str(o.read())
            if "firefox.exe" in text:
                os.popen("taskkill /im firefox.exe /F")
                time.sleep(1)
            else:
                killed = True
        killed = False
        while not killed:
            o = os.popen('tasklist /FI "IMAGENAME eq geckodriver.exe"')
            text = str(o.read())
            if "geckodriver.exe" in text:
                os.popen("taskkill /im geckodriver.exe /F")
                time.sleep(1)
            else:
                killed = True
    except:
        print("进程firefox.exe 或者 geckodriver.exe不存在")


def kill_ie_process():
    """杀掉IE进程"""
    killed = False
    # noinspection PyBroadException
    try:
        while not killed:
            o = os.popen('tasklist /FI "IMAGENAME eq iexplore.exe"')
            text = str(o.read())
            if "iexplore.exe" in text:
                os.popen("taskkill /im iexplore.exe /F")
                time.sleep(1)
            else:
                killed = True
        killed = False
        while not killed:
            o = os.popen('tasklist /FI "IMAGENAME eq IEDriverServer.exe"')
            text = str(o.read())
            if "IEDriverServer.exe" in text:
                os.popen("taskkill /im IEDriverServer.exe /F")
                time.sleep(1)
            else:
                killed = True
    except:
        print("进程iexplore.exe 或者 IEDriverServer.exe不存在")


# 获取selenium对象
def get_selenium():
    return selenium_browser


# 保持浏览器页面页签始终只有一个
def keep_window():
    get_selenium().close()
    switch_window(0)


# 切换浏览器页签
def switch_window(window_index=0):
    handles = get_selenium().window_handles
    get_selenium().switch_to.window(handles[window_index])


# 切入iframe，解决获取不到元素的问题
def switch_iframe(iframe=None):
    if not iframe:
        return get_selenium().switch_to.frame(find.element("t,iframe"))
    elif str(iframe).lower() == "default":
        return get_selenium().switch_to.default_content()
    else:
        return get_selenium().switch_to.frame(iframe)


# 切入iframe后，记得返回主文档才能操作主文档的内容
def switch_default():
    get_selenium().switch_to.default_content()


# 返回上一级iframe
def switch_parent_iframe():
    get_selenium().switch_to.parent_frame()
