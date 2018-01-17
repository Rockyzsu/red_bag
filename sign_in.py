# -*-coding=utf-8-*-
import requests
import json
with open('setting.json') as f:
    data=json.load(f)
def jd():
    url = 'https://' \
          'vip.jd.com/common/signin.html?token=1024196992'
    headers = data['jd_header']
    r=requests.get(url=url,headers=headers)
    print r.text


def main():
    jd()

if __name__ == '__main__':
    main()
