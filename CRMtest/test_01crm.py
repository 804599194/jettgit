# -*- coding: utf-8 -*-
import os
import unittest
import warnings
from single import Sin
from crm_shangjia import Login
from crm_fengzhuang import fengzhuang



import time
class merchant_Management(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('开始测试商家管理')
        warnings.simplefilter("ignore", ResourceWarning)
        #test_crm.login = Login()


    @classmethod
    def tearDownClass(cls):
        print('结束测试商家管理模块')
        #test_crm.login.driver.quit()

    '''
    def test_case01(self):
        u"登录钉钉"
        self.login.login()
        time.sleep(1)
        t = self.login.driver.find_element_by_id("com.alibaba.android.rimet:id/menu_current_company").text
        print(t)
        time.sleep(1)
        self.assertEqual(t, u'广东八块钱网络科技有限公司')
    '''

    def test_case01(self):
        u"进入CRM工作台"
        h=Login()
        t2,t = h.crm_job()
        time.sleep(1)
        try:
            self.assertIn('李和健',t2)
            self.assertEqual(t, '工作台')
            print(u"进入CRM工作台成功")
        except AssertionError:
            print(u"进入CRM工作台失败")
            raise
        time.sleep(2)


    def test_case02(self):
        "新增商家"
        h = Login()
        mobile, t1, t4 = h.xinzengshangjia()
        try:
            self.assertEqual(t1, '添加成功')
            self.assertEqual(t4, mobile)
            print(u"新增商家成功")
        except AssertionError:
            print(u"新增商家失败")
            raise
        time.sleep(2)


    def test_case03(self):
        "编辑商家"
        h = Login()
        mobile, t1, t4, t6, t8=h.bianjishangjia()
        time.sleep(0.5)
        try:
            self.assertEqual(t1, '广东八块钱科技部')
            self.assertEqual(t4, mobile)
            print(u"编辑商家成功")
        except AssertionError:
            print(u"编辑商家失败")
            raise

        try:
            self.assertEqual(t8, '从 广东八块钱变更为 广东八块钱科技部')
            self.assertIn(mobile, t6)
            print(u"跟进情况记录正常")
        except AssertionError:
            print(u"跟进情况记录异常")
            raise
        time.sleep(2)

    def test_case04(self):
        "新增商家员工"
        h = Login()
        mobile, tel, t1, t4, t5 = h.xinzengyuangong()
        time.sleep(0.5)
        try:
            self.assertEqual(t1, '添加成功')
            self.assertIn(mobile, t4)
            self.assertIn(tel, t5)
            print(u"新增商家员工成功")
        except AssertionError:
            print(u"新增商家员工失败")
            raise
        time.sleep(2)

    def test_case05(self):
        "商家员工拨号功能"
        h = Login()
        t = h.yuangongbohao()
        time.sleep(0.5)
        try:
            self.assertEqual(t, '无法访问移动网络。')
            print(u"商家员工拨号功能正常")
        except AssertionError:
            print(u"商家员工拨号功能异常")
            raise
        time.sleep(2)

    

    def test_case06(self):
        "编辑商家员工"
        h = Login()
        t1, t4, t6 = h.bianjiyuangong()
        time.sleep(0.5)
        try:
            self.assertEqual(t1, '修改成功')
            self.assertEqual(t4, '自动员工软件测试攻城狮')
            print(u"编辑商家员工成功")
        except AssertionError:
            print(u"编辑商家员工失败")
            raise

        try:
            self.assertEqual(t6, '从 软件测试工程师变更为 软件测试攻城狮')
            print(u"编辑员工后跟进情况记录正常")
        except AssertionError:
            print(u"编辑员工后跟进情况记录异常")
            raise
        time.sleep(2)

    def test_case07(self):
        "填写商家员工跟进情况"
        h = Login()
        g_time, t1, t4 = h.s_genjinqingkuang()

        time.sleep(0.5)
        try:
            self.assertEqual(t1, '操作成功')
            self.assertEqual(t4, '自动化测试')
            Sin().driver.find_element_by_xpath("//android.view.View[@content-desc='%s']" % g_time)
            print(u"商家员工跟进情况保存成功")
        except AssertionError:
            print(u"商家员工跟进情况保存失败")
            raise
        time.sleep(2)

    def test_case08(self):
        "商家拜访记录-签到"
        h = Login()
        t1, t4 = h.baifangjilu_qiandao()
        time.sleep(0.5)
        try:
            self.assertEqual(t1, '签到成功')
            self.assertEqual(t4, '未签退')
            print(u"商家员工拜访签到成功")
        except AssertionError:
            print(u"商家员工拜访签到失败")
            raise
        time.sleep(2)

    def test_case09(self):
        "商家拜访记录-签退"
        h = Login()
        t1, t4, t5 = h.baifangjilu_qiantui()
        time.sleep(0.5)
        try:
            self.assertEqual(t1, '签退成功')
            self.assertEqual(t4, '已签退')
            self.assertEqual(t5, '自动化拜访(签退测试)')
            print(u"商家员工拜访签退成功")
        except AssertionError:
            print(u"商家员工拜访签退失败")
            raise
        time.sleep(2)


    def test_case10(self):
        "筛选商家名称"
        h = Login()
        list, f = h.shaixuan()
        time.sleep(1)
        if list:  # 判断列表是否为空
            i = 0
            while i <= f:
                try:
                    self.assertIn('自动化-商家', list[i])
                    print(list[i])
                    i = i + 1
                except AssertionError:
                    i = i + 1
                    print("筛选商家姓名结果不一致")
                    raise
                    break
            print("筛选商家姓名结果一致")
        else:
            print("商家列表为空值，可能是获取元素出现了问题")
            self.assertEqual('自动化商家', " ")
        time.sleep(2)


    def test_case11(self):
        "筛选跟进时间"
        h = Login()
        list, f = h.follow_date()
        time.sleep(1)
        if list:  # 判断列表是否为空
            i = 0
            while i <= f:
                try:
                    if i < f:
                        date = list[i] <= list[i + 1]
                        self.assertEqual(True, date)
                        print(date)
                    if i == f:
                        pass
                    i = i + 1
                except AssertionError:
                    i = i + 1
                    print("筛选跟进时间排序结果不一致")
                    raise
                    break
            print("筛选跟进时间排序结果一致")
        else:
            print("商家列表为空值，可能是获取元素出现了问题")
            self.assertEqual('跟进时间', " ")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
