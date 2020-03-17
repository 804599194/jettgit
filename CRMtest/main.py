
# -*- coding: UTF-8 -*-
import os
import sys
#print(sys.path)
import args as args
import xmlrunner
from test_01crm import merchant_Management


sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\CRMtest')
sys.path.append('C:\\Python37\\python37.zip')
sys.path.append('C:\\Python37\\DLLs')
sys.path.append('C:\\Python37')
sys.path.append('C:\\Users\\Administrator\\AppData\\Roaming\\Python\\Python37\\site-packages')
sys.path.append('C:\\Python37\\lib\\site-packages')
import unittest,time
from BeautifulReport import BeautifulReport


test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__ == '__main__':
    '''
    # 设置报告文件保存路径,theme="theme_cyan"
    report_dir ='D:\\Report'

    # 获取系统当前时间
    #now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    # 设置报告名称格式

    HtmlFile = "CRM自动化测试报告" + now + ".html"

    result = BeautifulReport(discover)
    result.report(filename=HtmlFile, report_dir='C:\\Users\\Administrator\\.jenkins\\workspace\\crm_appium', description='CRM自动化测试用例集',theme="theme_cyan")
     '''
    '''
    suite_tests = unittest.defaultTestLoader.discover(".", pattern="test*.py",top_level_dir=None)
    BeautifulReport(suite_tests).report(filename=HtmlFile, description='CRM自动化测试用例集', log_path="C:\\Users\\Administrator\\.jenkins\\workspace\\crm_appium")
    '''
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(merchant_Management))
    suite_tests = unittest.defaultTestLoader.discover(".", pattern="test*.py")
    # runner=unittest.TextTestRunner(verbosity=2)
    runner = xmlrunner.XMLTestRunner(output='C:\\Users\\Administrator\\.jenkins\\workspace\\crm_appium\\test-reports')  # test-reports为生成报告的目录名
    #runner.run(suite)
    runner.run(suite_tests)




