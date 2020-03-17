# -*- coding: utf-8 -*-
import datetime
import os
import time

from selenium.common.exceptions import NoSuchElementException

from single import Sin
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import random
import re
from crm_fengzhuang import fengzhuang

class d_job_report():

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

    def add_daily(self):
        TouchAction(Sin().driver).tap(x=82, y=176).perform()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='工作汇报']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='新增汇报']").click()
        time.sleep(1)
        #Sin().driver.find_element_by_xpath(
          #  "//android.widget.Button[@content-desc='新增日报']").click()
        TouchAction(Sin().driver).tap(x=540, y=1670).perform()
        time.sleep(1)

        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建日报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[3]/android.view.View/android.view.View[3]/android.widget.EditText").send_keys("自动化日报总结")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建日报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[4]/android.view.View/android.view.View[3]/android.widget.EditText").send_keys("自动化日报计划")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='选择文件']").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/checkbox").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/btn_send").click()
        time.sleep(1)
        t = fengzhuang()
        b = 2
        t.swipe_app(b)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
           "//android.webkit.WebView[@content-desc='新建日报']/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View[4]").click()
        time.sleep(1)
        ele1 = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='新建日报']/android.view.View/"
            "android.view.View/android.view.View/android.view.View[6]/android.view.View[1]/android.view.View[2]")
        g = 14
        t.swipe(ele1, g)
        time.sleep(1)
        flag=Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='新建日报']/android.view.View/" 
            "android.view.View/android.view.View/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[22]/android.widget.CheckBox")
        ha = flag.get_attribute("checked")
        time.sleep(1)
        #print(ha)
        if ha == "false":   #判断按钮是否选中，返回的是String类型，不是boolean值
            Sin().driver.find_element_by_xpath(
                "//android.view.View[@content-desc='赵怡']").click()
        else:
            print("该按钮已选中，无需选择")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='确定']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='提交']").click()
        time.sleep(0.5)
        h1 = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='发布成功']")
        h = h1.get_attribute(name='content-desc')
        time.sleep(1)
        return h

    def add_weekly(self):
        Sin().driver.find_element_by_xpath(
            "//android.widget.TextView[@content-desc='返回']").click()
        #Sin().driver.find_element_by_xpath(
           # "//android.view.View[@content-desc='工作汇报']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='新增汇报']").click()
        time.sleep(1)
        # Sin().driver.find_element_by_xpath(
        #  "//android.widget.Button[@content-desc='新增日报']").click()
        TouchAction(Sin().driver).tap(x=562, y=1813).perform()
        time.sleep(1)

        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建周报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[3]/android.view.View/android.view.View[3]/android.widget.EditText").send_keys("自动化周报总结")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建周报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[4]/android.view.View/android.view.View[3]/android.widget.EditText").send_keys("自动化周报计划")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='选择文件']").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/checkbox").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/btn_send").click()
        time.sleep(1)
        t = fengzhuang()
        b = 2
        t.swipe_app(b)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建周报']/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View[4]").click()
        time.sleep(1)

        flag = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='新建周报']/android.view.View/"
                "android.view.View/android.view.View/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.CheckBox")
        ha = flag.get_attribute("checked")     #isSelected()判断选中没有效果
        time.sleep(1)
        print(ha)
        if ha == "false":  # 判断按钮是否选中，返回的是String类型，不是boolean值
            Sin().driver.find_element_by_xpath(
                "//android.webkit.WebView[@content-desc='新建周报']/android.view.View/android.view.View/android.view.View/"
                "android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.CheckBox").click()
        else:
            print("该按钮已选中，无需选择")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='确定']").click()
        time.sleep(2)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='提交']").click()
        time.sleep(0.5)
        try:
            h1 = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='发布成功']")
            h = h1.get_attribute(name='content-desc')
        except NoSuchElementException:
            print("该元素不存在")
        time.sleep(1)
        return h

    def add_monthly(self):
        Sin().driver.find_element_by_xpath(
            "//android.widget.TextView[@content-desc='返回']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='新增汇报']").click()
        time.sleep(1)
        TouchAction(Sin().driver).tap(x=599, y=1969).perform()
        time.sleep(1)

        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建月报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[3]/android.view.View/android.view.View[3]/android.widget.EditText").send_keys("自动化月报总结")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建月报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[4]/android.view.View/android.view.View[3]/android.widget.EditText").send_keys("自动化月报计划")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='选择文件']").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/checkbox").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/btn_send").click()
        time.sleep(1)
        t = fengzhuang()
        b = 2
        t.swipe_app(b)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建月报']/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View[4]").click()
        time.sleep(1)

        flag = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='新建月报']/android.view.View/"
            "android.view.View/android.view.View/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.CheckBox")
        ha = flag.get_attribute("checked")  # isSelected()判断选中没有效果
        time.sleep(1)
        print(ha)
        if ha == "false":  # 判断按钮是否选中，返回的是String类型，不是boolean值
            Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建月报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.CheckBox").click()
        else:
            print("该按钮已选中，无需选择")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='确定']").click()
        time.sleep(2)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='提交']").click()
        time.sleep(0.5)
        try:
            h1 = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='发布成功']")
            h = h1.get_attribute(name='content-desc')
        except NoSuchElementException:
            print("该元素不存在")
        time.sleep(1)
        return h

    def filtrate_type(self):
        Sin().driver.find_element_by_xpath(
           "//android.widget.TextView[@content-desc='返回']").click()
        #Sin().driver.find_element_by_xpath(
           # "//android.view.View[@content-desc='工作汇报']").click()
        time.sleep(1)

        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='日报']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='周报']").click()
        time.sleep(1)

        i = 1
        f = 0
        list = []
        list2 = []
        while i < 100:         #筛选周报
            try:
                x = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='日报列表']/android.view.View/android.view.View/android.view.View/"
                    "android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[5]" % i)
                r_time1 = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='日报列表']/android.view.View/android.view.View/android.view.View/"
                    "android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[3]" % i)

                time.sleep(1)
                r_time = r_time1.get_attribute(name='content-desc')
                x2 = x.get_attribute(name='content-desc')
                list.append(x2)  # 把数据添加到数组列表
                list2.append(r_time)
                i = i + 1
                time.sleep(1)
                if i > 4:
                    if i > 5:
                        i = i - 1
                    b = 2
                    m = fengzhuang()
                    m.swipe_app(b)
                    if list2[f] == list2[f - 1]:
                        print("列表已滑到底部，无更多数据")
                        break
                f = f + 1
            except NoSuchElementException:
                f = f - 1
                print("周报列表读取完成，退出")
                break
        print(list)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='周报']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='月报']").click()
        time.sleep(1)
        n = 1
        k = 0
        list1 = []
        list3 = []
        while n < 9:  # 筛选月报
            try:
                x = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='日报列表']/android.view.View/android.view.View/android.view.View/"
                    "android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[4]" % n)
                r_time1 = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='日报列表']/android.view.View/android.view.View/android.view.View/"
                    "android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[3]" % n)

                time.sleep(1)
                r_time = r_time1.get_attribute(name='content-desc')
                x2 = x.get_attribute(name='content-desc')
                list1.append(x2)  # 把数据添加到数组列表
                list3.append(r_time)
                n = n + 1
                time.sleep(1)
                if n > 4:
                    if n > 5:
                        n = n - 1
                    b = 2
                    m = fengzhuang()
                    m.swipe_app(b)
                    if list3[k] == list3[k - 1]:
                        print("列表已滑到底部，无更多数据")
                        break
                k = k + 1
            except NoSuchElementException:
                k = k - 1
                print("月报列表读取完成，退出")
                break
        print(list1)

        return list,f,list1,k

    def filtrate_date(self):
        #Sin().driver.find_element_by_xpath(
        #    "//android.widget.TextView[@content-desc='返回']").click()
        #Sin().driver.find_element_by_xpath(
          #  "//android.view.View[@content-desc='工作汇报']").click()
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='新增汇报']").click()
        time.sleep(1)
        # Sin().driver.find_element_by_xpath(
        #  "//android.widget.Button[@content-desc='新增日报']").click()
        TouchAction(Sin().driver).tap(x=540, y=1670).perform()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建日报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[1]/android.view.View[4]").click()
        time.sleep(1)
        TouchAction(Sin().driver).tap(x=515, y=1821).perform()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建日报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[3]/android.view.View/android.view.View[3]/android.widget.EditText").send_keys("自动化日报总结")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新建日报']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[4]/android.view.View/android.view.View[3]/android.widget.EditText").send_keys("自动化日报计划")

        time.sleep(1)
        t = fengzhuang()
        b = 2
        t.swipe_app(b)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='提交']").click()
        time.sleep(1)
        TouchAction(Sin().driver).tap(x=82, y=176).perform()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='月报']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='日报']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='日期']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[contains(@content-desc,'昨天')]").click()
        time.sleep(1)
        i = 1
        f = 0
        list = []
        list1 = []
        while i < 100:  # 筛选昨天日报
            try:
                x = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='日报列表']/android.view.View/android.view.View/android.view.View/"
                    "android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[4]" % i)
                r_time1 = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='日报列表']/android.view.View/android.view.View/android.view.View/"
                    "android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[3]" % i)
                time.sleep(1)
                x2 = x.get_attribute(name='content-desc')
                r_time = r_time1.get_attribute(name='content-desc')
                list.append(x2)  # 把数据添加到数组列表
                list1.append(r_time)
                #print(list1)
                i = i + 1
                time.sleep(1)
                if i > 4:
                    if i >5:
                       i = i - 1
                    b = 2
                    m = fengzhuang()
                    m.swipe_app(b)
                    if list1[f] == list1[f - 1]:
                        print("列表已滑到底部，无更多数据")
                        break
                f = f + 1
                time.sleep(1)

            except NoSuchElementException:
                f = f - 1
                print("昨天日报列表读取完成，退出")
                break
        print(list)
        return list,f

    def shaixuan(self):
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='筛选']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='我提交的报告']").click()
        time.sleep(1)
        i = 1
        f = 0
        list = []
        list1 = []
        while i < 100:  # 筛选我提交的报告
            try:
                x = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='日报列表']/android.view.View/android.view.View/android.view.View/android.view.View[2]/"
                    "android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[7]/android.view.View[1]" % i)
                r_time1 = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='日报列表']/android.view.View/android.view.View/android.view.View/"
                    "android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[3]" % i)
                time.sleep(1)
                x2 = x.get_attribute(name='content-desc')
                r_time = r_time1.get_attribute(name='content-desc')
                list.append(x2)  # 把数据添加到数组列表
                list1.append(r_time)
                # print(list1)
                i = i + 1
                time.sleep(1)
                if i > 4:
                    if i > 5:
                        i = i - 1
                    b = 2
                    m = fengzhuang()
                    m.swipe_app(b)
                    if list1[f] == list1[f - 1]:
                        print("列表已滑到底部，无更多数据")
                        break
                f = f + 1
                time.sleep(1)

            except NoSuchElementException:
                f = f - 1
                print("我提交的报告列表读取完成，退出")
                break
        print(list)
        return list,f