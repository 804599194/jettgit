# -*- coding: utf-8 -*-
import datetime
import os
import time

from selenium.common.exceptions import NoSuchElementException, WebDriverException

from single import Sin
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import random
import re
from crm_fengzhuang import fengzhuang


class Login():


    def login(self):
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/et_pwd_login").send_keys("qweasdzxc807158")
        time.sleep(1)
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/tv").click()
        time.sleep(2)
        Sin().driver.find_element_by_xpath(
            "//android.widget.RelativeLayout[@content-desc='工作[1]']/android.widget.TextView").click()
        time.sleep(5)

    def crm_job(self):
        try:
            login = Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/et_pwd_login")
            login1 = login.is_displayed()
            print(login1)
            if login1 == True:
                login.send_keys("qweasdzxc807158")
                time.sleep(1)
                Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/tv").click()
        except NoSuchElementException:
            pass

        time.sleep(2)
        t = 1
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/home_bottom_tab_button_work").click()
        #time.sleep(2)
        #TouchAction(Sin().driver).press(x=1006, y=1917).move_to(x=1043, y=1288).release().perform()
        time.sleep(2)

        # 范围时间
        d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '6:00', '%Y-%m-%d%H:%M')
        d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '8:00', '%Y-%m-%d%H:%M')

        # 当前时间
        n_time = datetime.datetime.now()
        if n_time > d_time and n_time < d_time1:
            element = "//android.view.View[@content-desc='CRM']"
        else:
            element = "//android.view.View[@content-desc='CRM']"
        m = fengzhuang()
        m.swipe_element(element,t)
        time.sleep(2)
        try:             #寻找元素失败后等待1秒重新寻找
            t1 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'李和健')]")
            t2 = t1.get_attribute(name='content-desc')
            t = Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/title").text
        except NoSuchElementException:
            time.sleep(1)
            t1 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'李和健')]")
            t2 = t1.get_attribute(name='content-desc')
            t = Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/title").text
        return t2,t

    def xinzengshangjia(self):
        Sin().driver.find_element_by_xpath(
            "(//android.view.View[@content-desc='进入'])[3]").click()
        time.sleep(2)
        try:
            Sin().driver.find_element_by_xpath(
                "//android.view.View[@content-desc='新建商家']").click()
        except WebDriverException:
            print("出错啦")
            time.sleep(1)
            Sin().driver.find_element_by_xpath(
                "//android.view.View[@content-desc='新建商家']").click()
        #i=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        i = str(random.randint(1, 10000000))
        t = "商家"+i
        m = "自动化"
        mobile=m+"-"+t
        time.sleep(2)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.view.View[3]/android.widget.EditText").send_keys(m)

        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[3]/android.view.View[3]/android.widget.EditText").send_keys(t)
        '''
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[4]/android.view.View[3]/android.widget.EditText").send_keys(i)
        '''

        time.sleep(2)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='请选择商户类型']").click()
        time.sleep(2)

        ele = Sin().driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="新增商家"]/android.view.View/'
            'android.view.View/android.view.View/android.view.View[4]/android.view.View[4]/android.view.View/android.view.View[2]/android.view.View')
        n = 3
        m = fengzhuang()
        m.swipe(ele, n)
        time.sleep(2)
        TouchAction(Sin().driver).tap(x=976, y=1442).perform()
        #self.driver.find_element_by_xpath(
         #   "//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='请选择区域']").click()
        time.sleep(2)
        n = 1
        ele = Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[5]/android.view.View[4]/android.view.View/android.view.View[2]/android.view.View[2]")
        m.swipe(ele, n)
        time.sleep(2)

        n1 = 1
        ele1 = Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[5]/android.view.View[4]/android.view.View/android.view.View[2]/android.view.View[3]")
        m.swipe(ele1, n1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='请选择']").click()
        time.sleep(2)
        n2 = 1
        ele2 = Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[9]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View")
        m.swipe(ele2, n2)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        try:
            Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='新增商家']/android.view.View/"
                                          "android.view.View/android.view.View/android.view.View[6]/android.view.View[3]/android.widget.EditText").send_keys("广东八块钱")
        except NoSuchElementException:
            Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='新增商家']/android.view.View/"
                                               "android.view.View/android.view.View/android.view.View[6]/android.view.View[3]/android.widget.EditText").send_keys("广东八块钱")
        time.sleep(1)

        Sin().driver.find_element_by_xpath(
           "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View[4]").click()
        time.sleep(1)
        
        #定位地点微调
        Sin().driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ImageView").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.SearchView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.SearchView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText").send_keys("威尼斯")
        time.sleep(1.5)
        TouchAction(Sin().driver).tap(x=976, y=2088).perform()
        time.sleep(1)
        TouchAction(Sin().driver).tap(x=599, y=263).perform()
        time.sleep(1)
        TouchAction(Sin().driver).tap(x=1013, y=154).perform()
        time.sleep(1)

        try:
            Sin().driver.find_element_by_xpath(
                "(//android.widget.RadioButton[@content-desc=''])[5]").click()
        except WebDriverException:
            time.sleep(1)
            Sin().driver.find_element_by_xpath(
                "(//android.widget.RadioButton[@content-desc=''])[5]").click()


        time.sleep(2)
        #TouchAction(self.driver).press(x=924, y=2046).move_to(x=946, y=1756).release().perform()
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[11]/android.view.View[2]/android.widget.EditText").send_keys("1")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[10]/android.view.View[2]/android.widget.EditText").send_keys("1")
        time.sleep(1)
        t1 = 1
        element="//android.widget.CheckBox[@content-desc='日式']"
        m.swipe_element(element,t1)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.widget.CheckBox[@content-desc='中式现代']").click()

        time.sleep(2)
        t = 1
        element1="//android.view.View[@content-desc='之前活动参与情况']"
        m.swipe_element(element1,t)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增商家']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[3]/android.view.View[2]/android.widget.EditText").send_keys("自动化测试")
        time.sleep(2)
        Sin().driver.find_element_by_accessibility_id("添加").click()
        time.sleep(1.5)
        try:
            t = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='商家详情']/android.view.View/android.view.View[2]/android.view.View")
            t1 = t.get_attribute(name='content-desc')
            t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动化-商家')]")
            t4 = t2.get_attribute(name='content-desc')
        except NoSuchElementException:
            time.sleep(0.5)
            t = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='商家详情']/android.view.View/android.view.View[2]/android.view.View")
            t1 = t.get_attribute(name='content-desc')
            t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动化-商家')]")
            t4 = t2.get_attribute(name='content-desc')
        print(t1)
        return mobile, t1, t4

    def bianjishangjia(self):

        t1 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动化-商家')]")
        t2 = t1.get_attribute(name='content-desc')
        t3=t2.split('-')[1]
        mobile1 = t3+"(编辑)"
        mobile = "自动化-"+mobile1
        print(mobile)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "(//android.view.View[@content-desc='编辑资料'])").click()
        time.sleep(1)
        ele2=Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='编辑商家']/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[3]/android.widget.EditText")
        ele2.click()
        time.sleep(1)
        ele3=ele2.get_attribute('text')
        t=fengzhuang()
        t.edittextclear(ele3)
        time.sleep(1)
        ele2.send_keys(mobile1)
        time.sleep(1)
        TouchAction(Sin().driver).tap(x=981, y=1442).perform()  # 模拟坐标点击收起键盘
        time.sleep(1)
        TouchAction(Sin().driver).tap(x=986, y=1439).perform()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc=\"编辑商家\"]/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View[2]").click()
        time.sleep(1)
        ele=Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='编辑商家']/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View[3]/android.widget.EditText")
        ele.click()
        time.sleep(1)
        ele1=ele.get_attribute('text')
        t.edittextclear(ele1)
        time.sleep(1)
        ele.send_keys("广东八块钱科技部")
        time.sleep(2)
        Sin().driver.find_element_by_xpath(
            "(//android.view.View[@content-desc='确定'])").click()
        time.sleep(0.5)
        t = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'广东八块钱')]")
        t1 = t.get_attribute(name='content-desc')
        t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动化-商家')]")
        t4 = t2.get_attribute(name='content-desc')
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='跟进情况']").click()
        time.sleep(1)
        t5 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'变更为 自动化-商家')]")
        t6 = t5.get_attribute(name='content-desc')
        t7 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'广东八块钱变更为')]")
        t8 = t7.get_attribute(name='content-desc')
        return mobile, t1, t4, t6, t8

    def xinzengyuangong(self):

        time.sleep(1)
        #i = str(random.randint(1, 10000000))
        mobile = "自动员工"
        t = fengzhuang()
        tel = t.tel()
        print(tel)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='商家员工']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='添加人员']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增员工']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.view.View[3]/android.widget.EditText").send_keys(mobile)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增员工']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[3]/android.view.View[3]/android.widget.EditText").send_keys(tel)
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增员工']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[4]/android.view.View[2]/android.widget.EditText").send_keys("软件测试工程师")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增员工']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[5]/android.view.View[2]/android.widget.EditText").send_keys("广东湛江")
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.widget.RadioButton[@content-desc='未婚']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增员工']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[7]/android.view.View[2]/android.widget.EditText").send_keys("粤A888888")
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.widget.Button[@content-desc='添加']").click()
        time.sleep(1.5)
        t = Sin().driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='员工详情']/android.view.View/android.view.View[2]/android.view.View")
        t1 = t.get_attribute(name='content-desc')
        t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动员工')]")
        t4 = t2.get_attribute(name='content-desc')
        t3 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'手机号码')]")
        t5 = t3.get_attribute(name='content-desc')
        print(t1)
        return mobile, tel, t1, t4, t5

    def yuangongbohao(self):
        Sin().driver.find_element_by_xpath("	//android.widget.TextView[@content-desc='返回']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='商家员工']/android.view.View/android.view.View/android.view.View/" 
            "android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.view.View[6]").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
            "android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]").click()
        time.sleep(2)
        t = Sin().driver.find_element_by_id("android:id/message").text

        Sin().driver.find_element_by_id("android:id/button1").click()

        return t

    def bianjiyuangong(self):
        TouchAction(Sin().driver).tap(x=607, y=981).perform()   #坐标模拟点击商家
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='编辑资料']").click()
        time.sleep(2)
        try:
            ele = Sin().driver.find_element_by_xpath(
                "//android.webkit.WebView[@content-desc='编辑员工']/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.widget.EditText")
        except AssertionError:
            ele = Sin().driver.find_element_by_xpath(
                "//android.webkit.WebView[@content-desc='编辑员工']/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.widget.EditText")

        time.sleep(1)
        ele.click()
        time.sleep(1)
        ele1 = ele.get_attribute('text')
        t = fengzhuang()
        time.sleep(1)
        t.edittextclear(ele1)
        time.sleep(1)
        ele.send_keys("软件测试攻城狮")
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='确定']").click()
        time.sleep(0.5)
        t = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='修改成功']")
        t1 = t.get_attribute(name='content-desc')
        t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'软件测试')]")
        t4 = t2.get_attribute(name='content-desc')
        time.sleep(2)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='跟进情况']").click()
        time.sleep(1)
        t5 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'从 软件测试工程师变更为')]")
        t6 = t5.get_attribute(name='content-desc')
        return t1, t4, t6

    def s_genjinqingkuang(self):
        time.time()
        g_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='跟进情况']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='填写跟进']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("(//android.view.View[@content-desc='请选择'])[1]").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("(//android.view.View[@content-desc='请选择'])[1]").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("(//android.view.View[@content-desc='请选择'])[1]").click()
        time.sleep(2)
        n1 = 1
        t = fengzhuang()
        ele = Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='填写跟进']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[5]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[3]")
        t.swipe(ele, n1)
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.widget.Button[@content-desc='确认']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='填写跟进']/android.view.View/android.view.View/android.view.View/"
            "android.view.View[6]/android.view.View[3]/android.widget.EditText").send_keys("自动化测试")
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='确定']").click()
        time.sleep(1.5)
        t = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='操作成功']")
        t1 = t.get_attribute(name='content-desc')
        t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动化测试')]")
        t4 = t2.get_attribute(name='content-desc')
        return g_time, t1, t4

    def baifangjilu_qiandao(self):
        Sin().driver.find_element_by_xpath("	//android.widget.TextView[@content-desc='返回']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='拜访记录']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='新增拜访']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("	//android.view.View[@content-desc='拜访员工 ']").click()
        time.sleep(1.5)
        Sin().driver.find_element_by_xpath("//android.widget.CheckBox[contains(@content-desc,'自动员工')]").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='确定']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='新增拜访']/android.view.View/android.view.View/android.view.View/" 
            "android.view.View[4]/android.view.View[3]/android.widget.EditText").send_keys("自动化拜访")
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.widget.Button[@content-desc='选择文件']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]").click()
        time.sleep(2)
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/checkbox").click()
        time.sleep(1)
        Sin().driver.find_element_by_id("com.alibaba.android.rimet:id/btn_send").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'签到')]").click()
        time.sleep(0.5)
        t = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='签到成功']")
        t1 = t.get_attribute(name='content-desc')
        t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'未签退')]")
        t4 = t2.get_attribute(name='content-desc')
        return t1, t4

    def baifangjilu_qiantui(self):
        TouchAction(Sin().driver).tap(x=374, y=1338).perform()     #模拟坐标点击签到记录
        time.sleep(1)
        ele=Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='拜访签退']/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[3]/android.widget.EditText")
        ele.click()
        ele1 = ele.get_attribute('text')
        t = fengzhuang()
        t.edittextclear(ele1)
        ele.send_keys("自动化拜访(签退测试)")
        time.sleep(1)
        TouchAction(Sin().driver).tap(x=981, y=1442).perform()   #模拟坐标点击收起键盘
        time.sleep(1)
        TouchAction(Sin().driver).tap(x=986, y=1439).perform()
        time.sleep(50)
        try:

            Sin().driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'签退')]").click()
            time.sleep(0.5)
            t = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='签退成功']")
            t1 = t.get_attribute(name='content-desc')
        except NoSuchElementException:
                time.sleep(5)
                Sin().driver.find_element_by_xpath("//android.widget.CheckBox[contains(@content-desc,'签退')]").click()
                time.sleep(0.5)
                t = Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='签退成功']")
                t1 = t.get_attribute(name='content-desc')
        print(t1)
        time.sleep(0.5)
        t2 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'已签退')]")
        t4 = t2.get_attribute(name='content-desc')
        t3 = Sin().driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动化拜访')]")
        t5 = t3.get_attribute(name='content-desc')

        return t1, t4, t5


    def shaixuan(self):
        #Sin().driver.find_element_by_xpath(
         #   "//android.view.View[contains(@content-desc,'商家 今日新增')]").click()
        Sin().driver.find_element_by_xpath("//android.widget.TextView[@content-desc='返回']").click()
        time.sleep(1)
        ele=Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='商家列表']/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[5]/android.widget.EditText")
        ele.click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='商家列表']/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.widget.EditText").send_keys("自动化-商家")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='搜索']").click()
        time.sleep(1)
        i = 1
        f = 0
        a = 1
        list = []
        while i < 100:  # 筛选商家列表
            try:
                x = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='商家列表']/android.view.View/android.view.View/android.view.View/" 
                    "android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View[%s]/android.view.View[1]" % i)
                time.sleep(1)
                x2 = x.get_attribute(name='content-desc')
                list.append(x2)  # 把数据添加到数组列表
                #print(list)
                i = i + 1
                time.sleep(1)
                if i == 4 and a == 1:
                    b = 1
                    m = fengzhuang()
                    m.swipe_app(b)      #第一次滑动幅度小,滑动半条数据
                    a = a+1
                if i > 4:
                    i = i - 1
                    b = 2
                    m = fengzhuang()
                    m.swipe_app(b)
                    if list[f] == list[f - 1]:
                        print("列表已滑到底部，无更多数据")
                        break
                f = f + 1
                time.sleep(1)
            except NoSuchElementException:
                f = f - 1
                print("我提交的报告列表读取完成，退出")
                break
        return list, f

    def follow_date(self):
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='跟进时间']").click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='以更新时间升序排序']").click()
        time.sleep(1)
        ele = Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='商家列表']/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[5]/android.widget.EditText")
        ele.click()
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.webkit.WebView[@content-desc='商家列表']/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.widget.EditText").send_keys(
            "自动化-商家")
        time.sleep(1)
        Sin().driver.find_element_by_xpath(
            "//android.view.View[@content-desc='搜索']").click()
        time.sleep(1)
        i = 1
        f = 0
        a = 1
        list = []
        while i < 100:  # 筛选商家列表
            try:
                x = Sin().driver.find_element_by_xpath(
                    "//android.webkit.WebView[@content-desc='商家列表']/android.view.View/android.view.View/android.view.View/"
                    "android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[%s]/android.view.View[3]/android.view.View[3]" % i)
                time.sleep(1)
                x2 = x.get_attribute(name='content-desc')
                list.append(x2)  # 把数据添加到数组列表
                print(list)
                i = i + 1
                time.sleep(1)
                if i == 5 and a == 1:
                    b = 1
                    m = fengzhuang()
                    m.swipe_app(b)  # 第一次滑动幅度小,滑动半条数据
                    a = a + 1
                if i > 5:
                    i = i - 1
                    b = 2
                    m = fengzhuang()
                    m.swipe_app(b)
                    if list[f] == list[f - 1]:
                        print("列表已滑到底部，无更多数据")
                        break
                f = f + 1
                time.sleep(1)
            except NoSuchElementException:
                f = f - 1
                print("商家列表列表读取完成，退出")
                break
        return list, f
