import datetime
import time
import warnings

from selenium import webdriver
from crm_job_report import d_job_report
from crm_fengzhuang import fengzhuang
from single import Sin
import unittest
class job_report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('开始测试工作汇报')
        warnings.simplefilter("ignore", ResourceWarning)

    '''
    def test_case01(self):
        t = d_job_report()
        t.crm_job()
        time.sleep(2)
    '''

    def test_case16(self):
        "新增日报"
        t = d_job_report()
        t1 = t.add_daily()
        try:
            self.assertEqual(t1, '发布成功')
            print("发送日报成功")
        except AssertionError:
            print("发送日报失败")
            raise
        time.sleep(2)


    def test_case17(self):
        "新增周报"
        t = d_job_report()
        t1 = t.add_weekly()
        try:
            self.assertEqual(t1, '发布成功')
            print("发送周报成功")
        except AssertionError:
            print("发送周报失败")
            raise
        time.sleep(2)

    def test_case18(self):
        "新增月报"
        t = d_job_report()
        t1 = t.add_monthly()
        try:
            self.assertEqual(t1, '发布成功')
            print("发送月报成功")
        except AssertionError:
            print("发送月报失败")
            raise
        time.sleep(2)
    

    def test_case19(self):
        "筛选汇报类型"
        t = d_job_report()
        list,f,list1,k = t.filtrate_type()
        if list:   #判断列表是否为空
            i = 0
            while i <= f:
                try:
                    self.assertIn('周报', list[i])
                    print(list[i])
                    i = i + 1
                except AssertionError:
                    i = i + 1
                    print("筛选周报类型结果不一致")
                    raise
                    break
            print("筛选周报类型结果一致")
        else:
            print("周报列表为空值，可能是获取元素出现了问题")
            self.assertEqual('周报', " ")

        if list1:    #判断列表是否为空
            i = 0
            while i <= k:
                try:
                    self.assertIn('月报', list1[i])
                    print(list1[i])
                    i = i + 1
                except AssertionError:
                    i = i + 1
                    print("筛选月报类型结果不一致")
                    raise
                    break
            print("筛选月报类型结果一致")
        else:
            print("月报列表为空值，可能是获取元素出现了问题")
            self.assertEqual('月报', " ")
        time.sleep(2)

    def test_case20(self):
        "筛选日报日期"
        t = d_job_report()
        list,f = t.filtrate_date()
        #r_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        now_time = datetime.datetime.now()
        r_time = (now_time + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        if list:  # 判断列表是否为空
            i = 0
            while i <= f:
                try:
                    self.assertIn(r_time, list[i])
                    print(list[i])
                    i = i + 1
                except AssertionError:
                    i = i + 1
                    print("筛选汇报时间结果不一致")
                    raise
                    break
            print("筛选汇报时间结果一致")
        else:
            print("日报列表为空值，可能是获取元素出现了问题")
            self.assertEqual('日报', " ")
        time.sleep(2)

    def test_case21(self):
        "筛选我提交的报告"
        t = d_job_report()
        list, f = t.shaixuan()
        if list:  # 判断列表是否为空
            i = 0
            while i <= f:
                try:
                    self.assertIn('我提交的', list[i])
                    print(list[i])
                    i = i + 1
                except AssertionError:
                    i = i + 1
                    print("筛选我提交的报告结果不一致")
                    raise
                    break
            print("筛选我提交的报告结果一致")
        else:
            print("日报列表为空值，可能是获取元素出现了问题")
            self.assertEqual('日报', " ")
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        print('结束测试工作汇报')

if __name__ == '__main__':
    unittest.main()