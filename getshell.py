#!/usr/bin/python3
# -*- coding:UTF-8 -*-
import conn
import os
import sys


# 获取执行shell命令
def run_test():
    shell = conn.read_db("select shell from run_shell limit 1")[0]["shell"]
    print(shell)
    folderPath = sys.path[0]
    print(folderPath)
    suiteName = os.path.realpath(sys.argv[0]).replace(folderPath, "")[1:-3]
    batPath = folderPath + "/" + suiteName + ".sh"
    outputFile = open(batPath, "w")
    outputFile.truncate()
    outputFile.write(shell)


run_test()
