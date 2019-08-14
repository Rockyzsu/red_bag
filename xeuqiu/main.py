# -*- coding: utf-8 -*-
# website: http://30daydo.com
# @Time : 2019/8/15 0:03
# @File : main.py
import json

import requests


def main():
    headers = {
        "Cookie": "xq_a_token=95869b16141799b7bd195f570b3d08510ab25f97;u=1733473480",
        "User-Agent": "Xueqiu Android 11.27.4",
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
        "Host": "api.xueqiu.com",
        "Connection": "Keep-Alive",
    }
    url = 'https://api.xueqiu.com/statuses/bonus/list.json?_t=1SMARTISANeb9a1bf45876f77f6c88828c3b17b5c0.1733473480.1565799111784.1565799125926&_s=387bf0&size=20&x=0.58&user_id=1733473480'
    r = requests.get(
        url=url,
        headers=headers
    )


    # 为了调试
    text = json.dumps(r.json(), ensure_ascii=False, indent=4)
    print(text)
    print(r.status_code)

    js_data = r.json()
    red_bag_list = js_data.get('items')
    result_list =[]
    for rb in red_bag_list:
        _id = rb.get('id')
        user_id=rb.get('user_id')
        created_at=rb.get('created_at')
        screen_name=rb.get('user',{}).get('screen_name','None')
        user_id=rb.get('user_id')



if __name__ == '__main__':
    main()
