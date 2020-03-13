# -*- coding: utf-8 -*-
import datetime
import os
import time


from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException,  WebDriverException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from single import Sin
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import random
import re
from crm_fengzhuang import fengzhuang

class qianke():


    def crm_job(self):
        time.sleep(2)
        t = 1
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/home_bottom_tab_button_work").click()
        time.sleep(2)
        TouchAction(Sin().driver).press(x=1006, y=1917).move_to(x=1043, y=1288).release().perform()
        time.sleep(2)
        element = "//android.view.View[@content-desc='CRM开发版']"
        m = fengzhuang()
        m.swipe_element(element, t)

    def xinzengqianke(self):

        t = fengzhuang()
        name = t.name()
        qianke_name = "自动"+name
        time.sleep(2)
        #TouchAction(Sin().driver).tap(x=72, y=159).perform()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "(//android.view.View[@content-desc='进入'])[1]").click()
        time.sleep(2)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='新建潜客']").click()
        time.sleep(2)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='添加潜客']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.view.View[3]/android.widget.EditText").send_keys(qianke_name)
        time.sleep(1)

        tel = t.tel()
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='添加潜客']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[3]/android.view.View[3]/android.widget.EditText").send_keys(tel)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "(//android.view.View[@content-desc='请选择'])[1]").click()
        time.sleep(1)
        n=1
        ele=Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='添加潜客']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[4]/android.view.View[4]/android.view.View/android.view.View[2]/android.view.View")
        t.swipe(ele,n)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='确认']").click()
        '''
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "(//android.view.View[@content-desc='请选择'])[1]").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='添加潜客']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[10]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]").click()
        '''
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='请选择']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "(//android.widget.RadioButton[@content-desc=''])[2]").click()
        time.sleep(1)
        try:
            Sin().driver.find_element_by_xpath(
                "//android.webkit.WebView[@content-desc='添加潜客']/android.view.View/android.view.View/android.view.View/"
                "android.view.View[8]/android.view.View[3]/android.widget.EditText").send_keys("自动化楼盘")
        except WebDriverException:
            time.sleep(1)
            Sin().driver.find_element_by_xpath(
                "//android.webkit.WebView[@content-desc='添加潜客']/android.view.View/android.view.View/android.view.View/"
                "android.view.View[8]/android.view.View[3]/android.widget.EditText").send_keys("自动化楼盘")
        time.sleep(1.5)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='展开更多']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='添加潜客']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[10]/android.view.View[2]/android.widget.EditText").send_keys("111")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='保存']").click()
        time.sleep(1)
        t = Sin().driver.find_element_by_xpath(
           "//android.webkit.WebView[@content-desc='潜客详情']/android.view.View/android.view.View[2]/android.view.View")
        #Sin().driver.refresh()
        #time.sleep(0.4)

        time.sleep(0.5)
        '''
        try:
            t = Sin().driver.find_element_by_xpath(
                  "//android.webkit.WebView[@content-desc='潜客详情']/android.view.View/android.view.View[2]/android.view.View")
        except NoSuchElementException:
            time.sleep(0.5)
            t = Sin().driver.find_element_by_xpath(
                "//android.webkit.WebView[@content-desc='潜客详情']/android.view.View/android.view.View[2]/android.view.View")
        '''
       # t = WebDriverWait(Sin().driver, 10).until(
         #      EC.visibility_of_element_located((By.XPATH, "//android.webkit.WebView[@content-desc='潜客详情']/android.view.View/android.view.View[2]/android.view.View")))


        #except (StaleElementReferenceException,TimeoutException):
          #  print("nihao")
            ##Sin().driver.refresh()
        #t = WebDriverWait(Sin().driver, 5).until(
         #    EC.presence_of_element_located((By.XPATH, "//android.webkit.WebView[@content-desc='潜客详情']/android.view.View/android.view.View[2]/android.view.View"))).get_attribute(name='content-desc')
        #print("t="+t)


       #t1 = t.get_attribute(name='content-desc')
            #time.sleep(1)
        t1 = t.get_attribute(name='content-desc')

        #t = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='操作成功']")

        t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动')]")
        t4 = t2.get_attribute(name='content-desc')
        t5 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'%s')]" % tel)
        t6 = t5.get_attribute(name='content-desc')
        print(t1)
        return t4,t6,tel,qianke_name

    def bianjiqianke(self):
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='编辑资料']").click()
        time.sleep(1)
        ele2 = Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='编辑潜客']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.view.View[3]/android.widget.EditText")
        ele2.click()
        time.sleep(1)
        ele3 = ele2.get_attribute('text')
        t = fengzhuang()
        t.edittextclear(ele3)
        ele2.send_keys("自动编辑")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='确定']").click()
        time.sleep(0.5)
        t = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='操作成功']")
        t1 = t.get_attribute(name='content-desc')
        t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动')]")
        t4 = t2.get_attribute(name='content-desc')
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='跟进情况']").click()
        time.sleep(1)
        t5 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'变更为 自动')]")
        t6 = t5.get_attribute(name='content-desc')
        return t1,t4,t6

    def q_genjingqingkuang(self):
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='跟进情况']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='填写跟进']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "(//android.view.View[@content-desc='请选择'])[1]").click()
        time.sleep(1)
        t = fengzhuang()
        n = 1
        ele = Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='填写跟进']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.view.View[4]/android.view.View/android.view.View[2]/android.view.View")
        t.swipe(ele, n)
        time.sleep(1)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "(//android.view.View[@content-desc='请选择'])[1]").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "(//android.view.View[@content-desc='请选择'])[1]").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='请选择']").click()
        time.sleep(1)
        n1 = 1
        ele1 = Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='填写跟进']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[5]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View")
        t.swipe(ele1, n1)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='填写跟进']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[6]/android.view.View[3]/android.widget.EditText").send_keys("自动化测试(潜客跟进测试)")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='确定']").click()
        time.sleep(0.5)
        t = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='跟进成功']")
        t1 = t.get_attribute(name='content-desc')
        t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动化测试')]")
        t4 = t2.get_attribute(name='content-desc')
        return t1,t4

    def shaixuanqianke(self):
        Sin().driver.find_element_by_xpath(
           "//android.widget.TextView[@content-desc='返回']").click()
        #time.sleep(1)
        #Sin().driver.find_element_by_xpath(
          #  "//android.view.View[contains(@content-desc,'潜客 今日新增')]").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='潜客列表']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[1]/android.view.View[5]/android.widget.EditText").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='潜客列表']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[1]/android.view.View[3]/android.widget.EditText").send_keys("自动")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='搜索']").click()
        time.sleep(2)

        i = 1
        f=0
        a = 1
        list = []
        while i < 100:
            try:
                x = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='潜客列表']/android.view.View/android.view.View/android.view.View/"
                    "android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[2]"%i)
                time.sleep(1)
                x2 = x.get_attribute(name='content-desc')
                list.append(x2)         #把数据添加到数组列表
                i = i+1
                time.sleep(1)
                if i == 4 and a == 1:
                    b = 1
                    m = fengzhuang()
                    m.swipe_app(b)      #第一次滑动幅度小,滑动半条数据
                    a = a+1

                if i > 4:
                    i = i - 1          #第二次及以上滑动整条数据
                    b = 2
                    m = fengzhuang()
                    m.swipe_app(b)

                if list[f] == "自动一":     #滑到到最后一条数据跳出循环
                    print("列表读取完成，退出")
                    break
                f = f + 1

            except NoSuchElementException:
                f = f - 1
                print("列表读取完成，退出")
                break
        #print(list)
        return list,f