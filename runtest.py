#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys


# 获取指定路径的用例集合
def run_test(test_case_path ="\\case", file_front="test_"):
    """根据指定的路径和文件前缀收集测试用例"""
    test_case_path = input(
        "<第一步：选择要执行的用例的文件路径；输入路径：\\case"
        "\ ; 多个路径写法：\\case\DEMO1;\\case\DEMO2 >\n->输入用例路径：")
    file_front = input("<第二步：选择要执行的用例的文件名前缀；比如：test_  或者 test_aa_  >\n->输入要执行的用例的前缀：")
    folderPath = sys.path[0]
    suiteName = os.path.realpath(sys.argv[0]).replace(folderPath, "")[1:-3]
    batPath = folderPath + "\\" + suiteName + ".bat"
    outputFile = open(batPath, "w")
    outputFile.truncate()
    list = os.listdir(sys.path[0])
    outputFile.write("py.test ")
    path_input1 = test_case_path.split(";")
    path_num = len(path_input1)
    for i in range(0, path_num):
        test_case_path = folderPath + "\\case" + path_input1[i]
        g = os.walk(test_case_path)
        fileName = None
        folderName = None

        for path, d, filelist in g:
            for filePath in filelist:
                if filePath.endswith(".py") and filePath.startswith(file_front) and not filePath.__contains__(
                        "__init__") and not filePath.__contains__("Suite"):
                    outputFile.write(os.path.join(path, filePath).replace(os.getcwd(), ".").replace("\\", "/") + " ")
    # driver_path = helper.get_chromedriver_path().replace(folderPath, ".").replace("\\", "/")
    # outputFile.write("--alluredir ./report")
    outputFile.write("--html=./report/report.html")
    # outputFile.write("--driver Chrome --driver-path " + driver_path)
    outputFile.close()

# 运行收集用例
run_test()
