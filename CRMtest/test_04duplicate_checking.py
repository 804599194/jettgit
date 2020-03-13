import datetime
import time
import warnings

from selenium import webdriver
from crm_duplicate_checking import duplicate_checking
from crm_fengzhuang import fengzhuang
from single import Sin
import unittest
class d_duplicate_checking(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('开始测试客户查重')
        warnings.simplefilter("ignore", ResourceWarning)


    '''
    def test_case01(self):
        t = duplicate_checking()
        t.crm_job()
        time.sleep(2)
    '''

    def test_case22(self):
        "潜客查重"
        t = duplicate_checking()
        mobile, t1, t3, t5, t7 = t.qiankechachong()
        time.sleep(0.5)
        try:
            self.assertEqual(t1, '该潜客已被录入')
            self.assertIn(mobile, t3)
            self.assertEqual(t5, '李和健')
            self.assertEqual(t7, "该潜客尚未被录入")
            print(u"潜客查重功能正常")
        except AssertionError:
            print(u"潜客查重功能异常")
            raise
        time.sleep(2)


    def test_case23(self):
        "商家人员查重"
        t = duplicate_checking()
        mobile, t1, t3, t5, t7 = t.shangjiachachong()
        time.sleep(0.5)
        try:
            self.assertEqual(t1, '该商家员工已被录入')
            self.assertIn(mobile, t3)
            self.assertEqual(t5, '李和健')
            self.assertEqual(t7, "该商家员工尚未被录入")
            print(u"商家员工查重功能正常")
        except AssertionError:
            print(u"商家员工查重功能异常")
            raise
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        print('结束测试客户查重')
        Sin().driver.quit()

if __name__ == '__main__':
    unittest.main()