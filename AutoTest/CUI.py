#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright 2018 黎慧剑
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Auto Test 控制台
基于HiveNetLib的prompt_plus实现

@module CUI
@file CUI.py

"""

import sys
import os
# 装载本地扩展库
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'ExtLib'))

__MOUDLE__ = 'CUI'  # 模块名
__DESCRIPT__ = u'AutoTest控制台'  # 模块描述
__VERSION__ = '0.1.0'  # 版本
__AUTHOR__ = u'黎慧剑'  # 作者
__PUBLISH__ = '2019.03.24'  # 发布日期


if __name__ == '__main__':
    # 当程序自己独立运行时执行的操作
    print(os.path.abspath(os.path.dirname(__file__)))
