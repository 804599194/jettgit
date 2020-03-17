import time
import warnings

from selenium import webdriver
from crm_qianke import qianke
from crm_fengzhuang import fengzhuang
from single import Sin
import unittest
class broker_Management(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('开始测试潜客管理')
        warnings.simplefilter("ignore", ResourceWarning)

    '''
    def test_case01(self):
        t = qianke()
        t.crm_job()
        time.sleep(2)
    '''


    def test_case12(self):
        "新增潜客"
        t = qianke()
        t4, t6, tel, qianke_name = t.xinzengqianke()
        time.sleep(0.5)
        try:
            #self.assertEqual(t1, '操作成功')
            self.assertEqual(t4, qianke_name)
            self.assertEqual(t6, tel)
            print(u"新增潜客成功")
        except AssertionError:
            print(u"新增潜客失败")
            raise
        time.sleep(2)

    def test_case13(self):
        "编辑潜客"
        t = qianke()
        t1,t4,t6 = t.bianjiqianke()
        time.sleep(0.5)
        try:
            self.assertEqual(t1, '操作成功')
            self.assertEqual(t4, '自动编辑')
            self.assertIn('变更为 自动编辑',t6)
            print(u"编辑潜客成功")
        except AssertionError:
            print(u"编辑潜客失败")
            raise
        time.sleep(2)

    def test_case14(self):
        "潜客跟进"
        t = qianke()
        t1,t4 = t.q_genjingqingkuang()
        time.sleep(0.5)
        try:
            self.assertEqual(t1, '跟进成功')
            self.assertEqual(t4, '自动化测试(潜客跟进测试)')
            print(u"跟进潜客成功")
        except AssertionError:
            print(u"跟进潜客失败")
            raise
        time.sleep(2)


    def test_case15(self):
        "按名字筛选潜客列表"
        m = qianke()
        list,f = m.shaixuanqianke()
        if list:     #判断列表是否为空
            i = 0
            while i <= f:
                try:
                    self.assertIn('自动', list[i])
                    #print(list[i])
                    i = i + 1
                except AssertionError:
                    i = i + 1
                    print(u"筛选结果不一致")
                    raise
                    break
            print(u"筛选结果一致")
            time.sleep(2)
        else:
            print("潜客列表为空值，可能是获取元素出现了问题")
            self.assertEqual('潜客', " ")


    @classmethod
    def tearDownClass(self):
        print('结束测试潜客管理')


if __name__ == '__main__':
    unittest.main()
