#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

# 项目配置信息
projectName = "pytest_selenium"  # 项目名称
file_path = os.path.abspath(os.getcwd())  # 获取当前执行文件目录
index = int(file_path.index(projectName))
project_path = file_path[0:index] + projectName  # 项目路径

# 项目工作目录
config_path = project_path + "/conf/"
data_path = project_path + '/data/'

