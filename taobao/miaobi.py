# -*-coding=utf-8-*-

# @Time : 2019/11/4 16:03
# @File : miaobi.py

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Taobao():
    def __init__(self):
        desired_caps = {
            "appActivity": "com.taobao.tao.TBMainActivity",
            "platformName": "Android",
            "deviceName": "b47b38e4",
            "platformVersion": "5.1.1",
            "appPackage": "com.taobao.taobao",
            "noReset": True
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def get_coin(self):
        time.sleep(3)
        # 进入页面
        self.driver.tap([(550, 1576), (1054, 1776)], 500)
        time.sleep(9) # 等待挺久的

        # 点击领取喵币按钮
        self.driver.tap([(905, 1707), (910, 1776)], 500)



    def start(self):
        time.sleep(5)
        count = 2
        current = 0

        while current < count:
            self.get_coin()
            count += 1

obj = Taobao()
obj.start()
