# -*- coding=UTF-8 -*-
import oper
import check
import browser


class Login:
    url = "http://uat.lemon.topideal.work"  # 登录地址
    username = "x, //input[@id='username']"  # 用户名
    password = "x, //input[@id='password']"  # 密码
    check = "x, //input[@id='check']"  # 验证码
    submit_btn = "x, //*[@id='root']/div/div/div[1]/div/div/form/div[4]/button"  # 登录按钮


def login(username, password, check):
    browser.open(Login.url)
    oper.type(Login.username, username)
    oper.type(Login.password, password)
    oper.type(Login.check, check)
    oper.click(Login.submit_btn)
