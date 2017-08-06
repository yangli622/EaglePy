#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@ author : yangli
@ date : 2017/8/6
"""

import os
import sys
import re
import ConfigParser

class EagleConfigParser(object):
    def __init__(self):
        self.path = os.path.join(re.sub('EaglePy.*$', 'EaglePy', os.path.realpath(__file__)), 'config', 'config.txt')
        self.config_path = self.path

    # 获取指定section，指定option的值
    def get_option_value(self, filepath, section, option):
        value = None
        if os.path.isfile(filepath):
            conf = ConfigParser.ConfigParser()
            conf.read(filepath)
            value = conf.get(section, option)
        return value

    # 更新指定section，指定option的值
    def update_option_value(self, filepath, section, option, value):
        if os.path.isfile(filepath):
            conf = ConfigParser.ConfigParser()
            conf.read(filepath)
            conf.set(section, option, value)
            return True
        else:
            return False

    def get_log_flag(self):
        flag = False
        config_path = self.config_path
        if os.path.isfile(config_path):
            if self.get_option_value(config_path, 'Log', 'flag') == 'True':
                flag = True
        return flag

    def get_print_flag(self):
        flag = False
        config_path = self.config_path
        if os.path.isfile(config_path):
            if self.get_option_value(config_path, 'Print', 'flag') == 'True':
                flag = True
        return flag

if __name__ == "__main__":
    conf = EagleConfigParser()
    print conf.get_log_flag()