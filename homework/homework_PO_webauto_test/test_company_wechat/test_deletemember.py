#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pytest
import yaml
from homework.homework_PO_webauto_test.PageObject_company_wechat.page_home import PageHome

def get_datas():
    with open("/Users/liyong/Desktop/study/homework/homework_PO_webauto_test/test_company_wechat/member_list_data.yaml") as file:
        datas = yaml.safe_load(file)
        my_data = datas.get("datas").get("data")
        my_ids = datas.get("datas").get("ids")
        print(datas)
        print(my_data)  #返回一个列表嵌套列表
        print(my_ids)   #返回一个列表
        return (my_data,my_ids)

#定义一个方法，使datas数组里的用例按照一组一组传入
@pytest.fixture(params=get_datas()[0],ids=get_datas()[1])
def get_datas_byfixture(request):
    print(f"request.param：{request.param}")
    return request.param

class TestDeleteMenber:
    def test_deletemember(self,get_datas_byfixture):
        page_home = PageHome()
        delete_success = page_home.pagehome_go_to_pagecontact().delete_member(get_datas_byfixture[2])
        assert "删除成功" == delete_success
