# -*-coding=utf-8-*-
import pickle
import requests
import time

from selenium import webdriver
import json

def jd():
    with open('keys.json','r') as f:
        jsn=json.load(f)
        user=jsn.get('user')
        password=jsn.get('password')
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path=r'C:\OneDrive\Python\selenium\chromedriver.exe',
                               chrome_options=options)

    browser.implicitly_wait(60)
    url = 'https://passport.jd.com/new/login.aspx'
    browser.get(url)
    # time.sleep(10)
    browser.find_element_by_css_selector('div.login-tab.login-tab-r').click()
    # time.sleep(10)
    browser.find_element_by_id('loginname').send_keys(user)
    browser.find_element_by_id('nloginpwd').send_keys(password)
    browser.find_element_by_css_selector('div.login-btn').click()
    # time.sleep(100)
    # browser.find_element_by_css_selector('div.dt').click()
    # browser.find_element_by_css_selector('li.shortcut_btn.fore3.dorpdown').click()
    browser.find_element_by_css_selector('li.shortcut_btn.fore3.dorpdown').click()
    time.sleep(5)
    print browser.find_element_by_css_selector('dl.fore3.dd.fore3_10')
    browser.find_element_by_css_selector('dl.fore3.dd.fore3_10').click()
    browser.find_element_by_css_selector('a.btn-gutter').click()
    time.sleep(10)
    # browser.find_element_by_xpath('//li[@class="fore3 dorpdown"]/div').click()
    # cookie = browser.get_cookies()
    # browser.close()
    # time.sleep(100)
    # browser.get('https://bean.jd.com/myJingBean/list')
    # time.sleep(10)

    # browser.find_elements_by_css_selector('div.dt.cw-icon')[2].click()
    # for i in x:
    #     i.click()
    # cookie = browser.get_cookies()
    # print cookie
    # time.sleep(20)
    # pickle.dump(cookie, open("cookies.pkl", "wb"))
    # browser.get("http://www.baidu.com")
    # browser.find_element_by_id("kw").clear()
    # browser.find_element_by_id("kw").send_keys("selenium")
    # browser.find_element_by_id("su").click()
    # browser.quit()
    # time.sleep(20)
    # cookie = {}
    # 转换dict调用
    # for item in cookie:
    #     cookie[item['name']] = item['value']
    #
    # url = 'https://home.jd.com'
    # header = {
    #     'Host': 'home.jd.com',
    #     'Pragma': 'no-cache',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    # }
    # response = requests.get(url, headers=header, cookies=cookie)
    # print response.text


def check_login():
    import pickle
    import requests

    cookies = pickle.load(open("cookies.pkl", "rb"))

    s = requests.Session()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])
    response = s.get("https://www.jd.com")
    bodyStr = response.text
    print bodyStr


if __name__ == '__main__':
    jd()
    # check_login()
