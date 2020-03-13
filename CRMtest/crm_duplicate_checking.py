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

class duplicate_checking():

    def crm_job(self):
        time.sleep(2)
        t1 = fengzhuang()
        t = 1
        Sin().driver.find_element_by_xpath("//android.widget.RelativeLayout[@content-desc='工作[1]']/android.widget.TextView").click()
        time.sleep(2)
        TouchAction(Sin().driver).press(x=1006, y=1917).move_to(x=1043, y=1288).release().perform()
        time.sleep(2)
        element = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.be/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View[4]/android.view.View/android.view.View[1]/android.view.View"
        t1.swipe_element(element,t)
        time.sleep(3)

    def qiankechachong(self):
        TouchAction(Sin().driver).tap(x=82, y=176).perform()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='客户查重']").click()
        time.sleep(1)
        mobile = '15033174430'
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='查重']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.widget.EditText").send_keys(mobile)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='查重']").click()
        time.sleep(1)
        t = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='查重']/android.view.View/"
            "android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")
        t1 = t.get_attribute(name='content-desc')
        time.sleep(1)
        t2 = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='查重']/android.view.View/"
            "android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[1]")
        t3 = t2.get_attribute(name='content-desc')
        time.sleep(1)
        t4 = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='查重']/android.view.View/"
            "android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[3]")
        t5 = t4.get_attribute(name='content-desc')

        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='返回']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='查重']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.view.View[2]/android.view.View[1]").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='查重']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.widget.EditText").send_keys(mobile)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='查重']").click()
        time.sleep(1)
        t6 = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='查重']/android.view.View/"
            "android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")
        t7 = t6.get_attribute(name='content-desc')
        return mobile, t1, t3, t5, t7

    def shangjiachachong(self):
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='商家员工查重']").click()
        mobile = '13800135000'
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='查重']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.widget.EditText").send_keys(mobile)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='查重']").click()
        time.sleep(1)
        t = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='查重']/android.view.View/"
            "android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")
        t1 = t.get_attribute(name='content-desc')
        time.sleep(1)
        t2 = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='查重']/android.view.View/"
            "android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[1]")
        t3 = t2.get_attribute(name='content-desc')
        time.sleep(1)
        t4 = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='查重']/android.view.View/"
            "android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[4]")
        t5 = t4.get_attribute(name='content-desc')
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='返回']").click()
        mobile1 = '13800135088'
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='查重']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.widget.EditText").send_keys(mobile1)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='查重']").click()
        time.sleep(1)
        t6 = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='查重']/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]")
        t7 = t6.get_attribute(name='content-desc')
        return mobile, t1, t3, t5, t7