#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@ author : yangli
@ date : 2017/8/6
"""

import EagleConfigParser

def eprint(message):
    ecp = EagleConfigParser.EagleConfigParser()
    ecp.get_print_flag()
    print message