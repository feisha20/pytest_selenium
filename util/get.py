# -*- coding: UTF-8 -*-
import yaml
import settings


def get_yaml_data(yaml_file):
    """获取yaml文件内容"""
    file = open(yaml_file, 'r', encoding="utf-8")
    data = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return data


def get_conf():
    """获取配置文件信息"""
    conf_file = settings.config_path + "conf.yaml"
    data = get_yaml_data(conf_file)
    return data