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

#定义一个测试类
class TestAddMember:
    #测试用例1：添加成员正常流程
    def test_addmember_success(self,get_datas_byfixture):
        page_home = PageHome()
        members = page_home.pagehome_go_to_addmember().addmember_success(get_datas_byfixture[0],get_datas_byfixture[1],get_datas_byfixture[2]).get_members(get_datas_byfixture[2])
        assert get_datas_byfixture[2] in members

    #测试用例2：添加成员失败
    def test_addmember_fail(self):
        pass


    #用例3：获取成员列表
    # def