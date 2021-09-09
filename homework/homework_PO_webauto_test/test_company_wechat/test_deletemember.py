#!/usr/bin/python3
# -*- coding:utf-8 -*-
import allure

#定义一个测试类
@allure.feature("删除成员")
class TestDeleteMenber:

    @allure.story("删除成员成功")
    def test_deletemember(self,setup_teardown,get_datas_byfixture):
        delete_success_text = setup_teardown.pagehome_go_to_pagecontact().delete_member(get_datas_byfixture[2])
        assert "删除成功" == delete_success_text
