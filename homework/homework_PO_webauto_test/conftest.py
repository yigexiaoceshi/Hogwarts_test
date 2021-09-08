#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List

import pytest
import yaml

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:  #遍历所有测试用例，item就是测试用例
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
