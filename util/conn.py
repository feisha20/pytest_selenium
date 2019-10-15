# -*- coding: UTF-8 -*-
import pymysql
import browser

# 数据库配置文件
conf_file = browser.configFileName


# 创建数据库连接
con = pymysql.connect(
    host=browser.get_config_item("database", "host"),
    port=int(browser.get_config_item("database", "port")),
    user=browser.get_config_item("database", "user"),
    password=browser.get_config_item("database", "password"),
    db=browser.get_config_item("database", "db"),
    charset="utf8",
)


host = browser.get_config_item("database", "host")

# 读数据库
def read_db(sql):
    con.ping(reconnect=True)
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result


# 写数据库
def write_db(sql):
    con.ping(reconnect=True)
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()

