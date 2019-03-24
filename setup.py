#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
#  Copyright 2018 黎慧剑
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


"""The setup.py file for Python AutoTest."""

from setuptools import setup, find_packages


LONG_DESCRIPTION = """
AutoTest 是一套开源自动测试框架，对自动测试提出标准的数据模型和处理流程，
可通过插件方式扩展自动测试的能力。
""".strip()

SHORT_DESCRIPTION = """
开源自动测试框架.""".strip()

DEPENDENCIES = [
    'HiveNetLib>=0.1.0'
]

# DEPENDENCIES = []

TEST_DEPENDENCIES = []

VERSION = '0.1.0'
URL = 'https://github.com/snakeclub/AutoTest'

setup(
    # pypi中的名称，pip或者easy_install安装时使用的名称
    name="AutoTest",
    version=VERSION,
    author="黎慧剑",
    author_email="snakeclub@163.com",
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license="Mozilla Public License 2.0",
    keywords="AutoTest Test Frameworks",
    url=URL,
    # 需要打包的目录列表, 可以指定路径packages=['path1', 'path2', ...]
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
    package_data={'': ['*.json']},  # 这里将打包所有的json文件
    # 此项需要，否则卸载时报windows error
    zip_safe=False
)
