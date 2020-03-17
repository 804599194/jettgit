import datetime
import os
import re

from crm_fengzhuang import fengzhuang

deviceAndroidVersion1 = os.popen('adb shell getprop ro.build.version.release')
deviceAndroidVersion=deviceAndroidVersion1.buffer.read().decode(encoding='utf8')
# 获取手机版本号
deviceVersion1 = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
print(deviceAndroidVersion)
login = fengzhuang()
tel =login.tel()
print(tel)
import subprocess

order='adb devices'        #获取连接设备

pi = subprocess.Popen('adb devices',shell=True,stdout=subprocess.PIPE)

i = pi.stdout.read().split()

print(i)
# 范围时间
d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '6:00', '%Y-%m-%d%H:%M')
d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '8:00', '%Y-%m-%d%H:%M')
print(d_time)
print(d_time1)
# 当前时间
n_time = datetime.datetime.now()
print(n_time)
# 判断当前时间是否在范围时间内
if n_time > d_time and n_time < d_time1:
    print("haha")
else:
    print("wuwu")