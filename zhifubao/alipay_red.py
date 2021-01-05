# coding=utf-8
# 公众号：可转债量化分析

import datetime
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
import os
from pathlib import PurePath
import fire


def delay(func):
    # 延时装饰器
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        time.sleep(1)
        return result

    return wrapper


class DriveBase:
    '''
    封装的基类
    '''

    def __init__(self, deviceName, package, activity, resetKB):
        self.desired_caps = {

            'platformName': 'Android',

            'deviceName': deviceName,

            'platformVersion': '9.0',

            # apk包名

            'appPackage': package,

            # apk的launcherActivity

            'appActivity': activity,

            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': resetKB,
            'skipServerInstallation': True,
            # 'autoLaunch':False,
        }
        self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.wait = WebDriverWait(self.driver, 10)

    def start(self):
        raise NotImplementedError('need to instance')

    def root_path(self):
        return PurePath(__file__).parent

    def get_bound_center(self, points):

        left_top, right_bottom = points[0], points[1]
        centerX = (left_top[0] + right_bottom[0]) / 2
        centerY = (left_top[1] + right_bottom[1]) / 2
        return int(centerX), int(centerY)

    @delay
    def click(self, points):
        centerX, centerY = self.get_bound_center(points)
        self.driver.tap([(centerX, centerY)])

    def get_screen_size(self):
        x = self.driver.get_window_size()['width']  # 获取屏幕宽度
        y = self.driver.get_window_size()['height']  # 获取屏幕高度
        return (x, y)

    @delay
    def swipe_scroll_vertical(self,screen=True):
        if screen:
            self.driver.swipe(500, 2000, 500, 400, 3000)
        else:
            self.driver.swipe(500, 1200, 500, 800, 3000)


    def read_histroy(self, filename):
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            return [i.strip() for i in f.readlines()]

    def save_hitory(self, filename, result_list):
        content = '\n'.join(result_list)
        with open(filename, 'w') as f:
            f.write(content)

    def clear_file(self, filename):
        try:
            os.remove(filename)
        except Exception as e:
            print(e)


class Alipay(DriveBase):
    def __init__(self, deviceName, package, activity, resetKB=False):
        super(Alipay, self).__init__(deviceName, package, activity, resetKB)
        self.history_file = os.path.join(self.root_path(), 'redbag.txt')
        self.width, self.height = self.get_screen_size()

    def video_redbag(self):
        '''
        直播红包
        '''
        target = '16:30'
        # self.waiting(self.convert_datetime(target))
    def found_redbag_icon(self):


        redbag_list = self.driver.find_elements_by_xpath('//android.widget.ImageView')

    def fund_redbag(self, clear, new_version):
        '''
        答题红包
        '''

        if clear:
            self.clear_file(self.history_file)

        self.history_result = self.read_histroy(self.history_file)
        self.click_by_text('理财')
        time.sleep(1)
        delta_x = 0
        if new_version:
            delta_x = 90

        search_points = [819 * self.width / 1080 + delta_x, 84 * self.height / 2207], [
            963 * self.width / 1080 + delta_x,

            228 * self.height / 2207]
        self.click(search_points)

        # 输入
        input_btn = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(
            (By.XPATH, '//android.widget.EditText[@text="搜索"]')))
        input_btn.send_keys(u'财富号')
        time.sleep(1)

        self.click_by_text('搜索')
        time.sleep(1)

        # 向右滑动到最后
        self.move_right_to_end()
        self.click_by_text('查看更多')

        while True:
            # 出现一个列表
            # self.slow_method()
            self.found_icon()

    def slow_method(self):
        item_list = self.driver.find_elements_by_xpath(
            '//android.widget.TextView[contains(@text, "财富号")]')

        item_list = item_list[1:]


        for item in item_list:
            text = item.text
            #
            if text in self.history_result:
                continue

            if re.search('信用卡财富号|储蓄卡财富号', text):
                self.history_result.append(text)
                self.save_hitory(self.history_file, self.history_result)
                # self.driver.back()
                continue

            try:
                item.click()
                time.sleep(3)
            except Exception as e:
                pass
            else:
                # 基金详情页面
                try:
                    self.swipe_scroll_vertical(screen=False)
                    has_redbag = self.driver.find_element_by_xpath(
                        '//android.view.View[@text="答题领取"]')

                except Exception as e:
                    print(f'{text} ==>没有红包')
                    self.history_result.append(text)
                    self.save_hitory(
                        self.history_file, self.history_result)
                    time.sleep(1)
                else:
                    self.going_redbag_page(text, has_redbag)
                    time.sleep(1)

                self.driver.back()
                print('点击返回')

            time.sleep(1)

        # 向下滑动
        self.scroll_down_next_page_fund_list()

    def found_icon(self):
        '''
        根据图标更新
        '''

        layouts = self.driver.find_elements_by_xpath('//android.widget.ListView/android.widget.FrameLayout')
        for layout in layouts:

            redbag_icon = layout.find_elements_by_xpath('.//android.widget.ImageView')
            if len(redbag_icon)==2:
                name = layout.find_element_by_xpath('.//android.widget.TextView[contains(@text, "财富号")]')
                text = name.text
                redbag_icon[1].click()
                time.sleep(3)

                try:
                    self.swipe_scroll_vertical(screen=False)
                    time.sleep(2)
                    has_redbag = self.driver.find_element_by_xpath(
                        '//android.view.View[@text="答题领取"]')

                except Exception as e:
                    time.sleep(1)
                else:
                    self.going_redbag_page(text, has_redbag)
                    time.sleep(2)

                self.driver.back()
                print('点击返回')
                time.sleep(2)

        self.scroll_down_next_page_fund_list()

    def scroll_down_next_page_fund_list(self):
        time.sleep(1)
        self.driver.swipe(219, 1909, 219, 100, 3000)
        time.sleep(1)

    def move_right_to_end(self):
        self.driver.swipe(1000, 520, 200, 520, 1000)
        time.sleep(1)
        self.driver.swipe(1000, 520, 200, 520, 1000)
        time.sleep(1)

    def going_redbag_page(self, text, has_redbag):
        time.sleep(2)
        print(f'{text} ==>红包')
        has_redbag.click()
        time.sleep(2)

        answer_list = self.driver.find_elements_by_xpath(
            '//android.view.View[@clickable="true"]')
        found = False
        button_number = 0

        while not found and button_number < 2:

            try:
                answer_list[button_number].click()  # 点击第一个答案

            except Exception as e:
                # print(e)
                time.sleep(1)
            else:

                if self.check_answer_right():  # 判断是否正确
                    self.driver.back()
                    time.sleep(1)
                    break
                button_number += 1

    def check_answer_right(self):
        is_right = False

        try:
            answer_right = WebDriverWait(self.driver,
                                         3).until(EC.presence_of_element_located((By.XPATH,
                                                                                  f'//android.view.View[@text="恭喜获得财运红包"]')))
        except:
            pass
        else:
            return True

        try:
            answer_right = WebDriverWait(self.driver,
                                         3).until(EC.presence_of_element_located((By.XPATH,
                                                                                  f'//android.view.View[@text="距离红包失效还有"]')))
        except:
            pass
        else:
            return True

        return is_right

    @delay
    def click_by_text(self, text):
        broadcast_btn = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@text="{text}"]')))
        broadcast_btn.click()

    def convert_datetime(self, tarret):
        today = datetime.date.today()
        return datetime.datetime.strptime(f'{today.year}-{today.month}-{today.day} ' + tarret, '%Y-%m-%d %H:%M')

    def waiting(self, target):

        # 阻塞程序
        while True:
            if datetime.datetime.now() - datetime.timedelta(seconds=5) > target:
                break
            else:
                time.sleep(1)


    def find_redbag_except_bond(self):
        '''
        寻找债基
        '''
        self.click_by_text('卡包')

        result = set()
        self.swipe_scroll_vertical(screen=True)

        while True:

            redbags = self.driver.find_elements_by_xpath('//android.widget.TextView[@text="去使用"]')
            fund_num = len(redbags)
            time.sleep(1)
            print(f'fund_num {fund_num}')
            for redbag_num in range(fund_num):
                try:

                    redbag_list = self.driver.find_elements_by_xpath('//android.widget.TextView[@text="去使用"]/parent::android.widget.FrameLayout/preceding-sibling::android.widget.LinearLayout')

                except Exception as e:
                    continue

                if len(redbag_list) - 1 < redbag_num:
                    break

                redbag_list[redbag_num].click()
                time.sleep(2)

                try:
                    name = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "财富号")]')
                except Exception as e:
                    time.sleep(1)
                    self.driver.back()
                    time.sleep(1)
                    # print('return back')
                    continue

                try:
                    is_bond = self.driver.find_element_by_xpath(
                        '//android.widget.TextView[contains(@text, "债") or contains(@text, "理财") or contains(@text, "货币") or contains(@text, "所有")]')
                except Exception as e:
                    # self.driver.find_element_by_xpath('//')
                    delete_img = [972, 84], [1044, 228]
                    self.click(delete_img)
                    delete_name = self.driver.find_element_by_xpath('//android.widget.TextView[@text="删除"]')
                    delete_name.click()
                    time.sleep(2)
                    delete_btn = self.driver.find_element_by_xpath('//android.widget.Button[@text="确定"]')
                    delete_btn.click()
                    time.sleep(2)

                else:
                    print(f'{name.text}   可用标的债/货币:  \n{is_bond.text}\n')
                    result.add(name.text)
                    self.driver.back()
                    time.sleep(1)

            self.swipe_scroll_vertical(screen=True)
            self.save_hitory('used_bond.txt', list(result))


z3 = 'cf828af'
z1 = 'ab7cded6'


def alipy_fund_redbag(clear=False, resetKB=False, search=True, new_version=False, device='z3'):
    '''阿里云红包'''

    package = 'com.eg.android.AlipayGphone'
    activity = 'com.eg.android.AlipayGphone.AlipayLogin'

    # if device=='z1':
    deviceName = device
    # deviceName = z1

    app = Alipay(deviceName, package, activity, resetKB)
    if search:
        app.fund_redbag(clear, new_version)
    else:
        app.find_redbag_except_bond()


if __name__ == '__main__':
    fire.Fire(alipy_fund_redbag)
