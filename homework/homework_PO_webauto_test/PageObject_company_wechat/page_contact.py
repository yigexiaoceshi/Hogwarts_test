#!/usr/bin/python3
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from homework.homework_PO_webauto_test.PageObject_company_wechat.page_base import PageBase
from time import sleep

#企业微信_通讯录页面，定义一个类
class PageContact(PageBase):
    #通讯录页面，方法1：点击【添加成员】跳转添加成员页面(和添加成员页面形成循环调用，import语句放于方法内部)
    def pagecontact_go_to_pageaddmember(self):
        from homework.homework_PO_webauto_test.PageObject_company_wechat.page_addmember import PageAddMember
        return PageAddMember(self.br)

    #通讯录页面，方法2：获取成员列表数据(用作断言)
    # def get_members(self):
    #     members = self.br.find_elements(By.CSS_SELECTOR,'#member_list>.member_colRight_memberTable_tr>.member_colRight_memberTable_td:nth-child(5)')
    #     print(members)
    #     phone_list = []
    #     for member in members:
    #         phone_list.append(member.text)
    #     print(phone_list)
    #     return phone_list

    #通讯录页面，方法2第二种写法，获取整个列表所有手机号（含翻页数据）：
    def get_members(self,phone_number):
        """
        思路1：
        1、获取页面总页数（字符串切片），赋值给变量n
        2、循环n次，即从0到n-1，首次循环n=0时在第一页，获取当前页
        3、从第二次循环开始，判断下一页按钮是否可点击，可点击时点击下一页，然后获取页面数据
        需要注意：
        1、获取到的每个页面的数据如果先全部塞到members列表里，遍历完页面再获取text的话行不通，因为在获取对象内容的时候是从当前页面开始解析，当前页面之前的页面会提示找不到
        2、所以只能每个页面获取到对象后，优先把text提取出来塞到members里即可
        :return:
        """
        members = []
        for i in range(1,4):
            # buttom_left = self.br.execute_script("return document.querySelector('.js_pre_page')")
            buttom_right = self.br.execute_script("return document.querySelector('.js_next_page')")
            if i == 1:
                member_start = self.br.find_elements(By.CSS_SELECTOR, '#member_list>.member_colRight_memberTable_tr>.member_colRight_memberTable_td:nth-child(5)')
                print(member_start)
                for member in member_start:
                    members.append(member.text)
            else:
                if buttom_right.is_enabled():
                    self.br.find_element(By.CSS_SELECTOR, '.js_next_page').click()
                    sleep(2)
                    member_middle = self.br.find_elements(By.CSS_SELECTOR, '#member_list>.member_colRight_memberTable_tr>.member_colRight_memberTable_td:nth-child(5)')
                    print(member_middle)
                    for member in member_middle:
                        members.append(member.text)
                else:
                    pass
                    # member_end = self.br.find_elements(By.CSS_SELECTOR,'#member_list>.member_colRight_memberTable_tr>.member_colRight_memberTable_td:nth-child(5)')
                    # print(member_end)
                    # members.append(member_end)
        print(members)
        self.br.find_element(By.ID,'memberSearchInput').send_keys(phone_number)
        self.br.find_element(By.CSS_SELECTOR,'.js_del_member').click()
        self.br.find_element(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        sleep(1)
        return members
        #思路2：
        # 1、定义上一页按钮，下一页按钮，使用if_elif_else判断语句
        # 2、上一页按钮不可点击时，获取第一页数据，提取text放到members
        # 3、上一页和下一页按钮均可点击时，获取中间页面数据，提取text放到members
        # 4、下一页按钮不可点击时，获取最后一页数据，提取text放到members
    # 通讯录页面，方法3：删除成员
    def delete_member(self,phone_number):
        self.br.find_element(By.ID,'memberSearchInput').send_keys(phone_number)
        print("已输入电话进行搜索")
        self.br.find_element(By.CSS_SELECTOR,'.js_del_member').click()
        sleep(1)
        print("已经点击删除，等待一秒，等待二次确认弹窗出现")
        self.br.find_element(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        print("点击弹窗的确认按钮，确定删除")
        delete_success = self.br.find_element(By.ID,'js_tips').text
        print("获取删除成功文本")
        print(delete_success)
        return delete_success