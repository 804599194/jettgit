import random
import time
from single import Sin
from appium import webdriver


class fengzhuang():
    def swipe(self,ele,n):
        #封装的滑动选择框方法
        w = ele.size['width']    #获取元素宽
        h = ele.size['height']   #获取元素高
        x = ele.location['x']    #获取元素起点x坐标
        y = ele.location['y']    #获取元素起点y坐标
        print(x, y)
        '''
        if m == 1:
            x1 = int(w / 2)
        if m == 2:
            x1 = int(w)
        if m == 3:
            x1 = int(w * 2)
        '''
        x1 = int(x)
        y1 = int(h / 5 * 1.7 + y)
        y2 = int(h / 5 * 1 + y)
        #print(x1, y1, y2)
        # 连续滑动n次
        for i in range(n):
            Sin().driver.swipe(x1, y1, x1, y2, 1000)
            time.sleep(1)

    def edittextclear(self, text):
        #封装的清除输入框方法
        Sin().driver.keyevent(123)
        for i in range(0, len(text)):
            Sin().driver.keyevent(67)

    def swipe_element(self,element,t):
        #封装的滑动页面寻找元素方法
        width = Sin().driver.get_window_size()['width']
        height = Sin().driver.get_window_size()['height']
        i = 0
        while i < 10:
            try:
                if t == 1:    #点击按钮
                    Sin().driver.find_element_by_xpath(element).click()
                if t == 2:    #输入框
                    Sin().driver.find_element_by_xpath(element).send_keys("自动化测试")
                break
            except Exception as e:
                Sin().driver.swipe(width / 2, height * 0.4, width / 2, height * 0.2)  # 滑动屏幕
                i = i + 1

    def swipe_app(self,i):
        #滑动app方法
        width = Sin().driver.get_window_size()['width']
        height = Sin().driver.get_window_size()['height']
        if i == 1:
            Sin().driver.swipe(width / 2, height * 0.4, width / 2, height * 0.3)
            i = i+1
        else:
            Sin().driver.swipe(width / 2, height * 0.4, width / 2, height * 0.212)



    def tel(self):
        #生成随机手机号
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                   "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                   "186", "187", "188", "189"]
        tel = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
        return tel

    def name(self):
        #生成随机汉字
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x}{body:x}'
        name = bytes.fromhex(val).decode('gb2312')
        return name