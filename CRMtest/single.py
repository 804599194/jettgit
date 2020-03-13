import os
import threading

from appium import webdriver

class Sin(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        if not hasattr(Sin,'_instance'):
            with Sin._instance_lock:
                if not hasattr(Sin, '_instance'):
                    Sin._instance = object.__new__(cls)
                    #chrome_options.add_argument('--disable-gpu')
                    device1 = os.popen('adb devices')
                    device2 = device1.buffer.read().decode(encoding='utf8')
                    devicename1 = device2.split()  # 自动获取设备号
                    devicename = '%s' % devicename1
                    # deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines()) #获取手机版本号
                    # deviceVersion1 = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
                    deviceAndroidVersion1 = os.popen('adb shell getprop ro.build.version.release')
                    deviceVersion1 = deviceAndroidVersion1.buffer.read().decode(encoding='utf8')
                    deviceVersion = '%s' % deviceVersion1
                    desired_caps = {}
                    desired_caps['platformName'] = 'Android'
                    # desired_caps['deviceName'] = '127.0.0.1:62001'
                    desired_caps['platforVersion'] = deviceVersion
                    desired_caps['deviceName'] = devicename
                    desired_caps['appPackage'] = 'com.alibaba.android.rimet'
                    desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.LaunchHomeActivity'
                    desired_caps['noReset'] = 'True'
                    cls.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return Sin._instance