# -*-coding=utf-8-*-
__author__ = 'Rocky'
# 对各种app进行签到
from uiautomator import device as d
import time, subprocess, sys

global displayWidth
global displayHeight
displayWidth_cuizi = 1080
displayHeight_cuizi = 1920


# 启动app
def launch_app(activity_name):
    try:
        cmd = 'adb shell am start -n %s' % activity_name
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print(p.stdout.read())
        time.sleep(15)
    except Exception as e:
        print(e)
        return


def get_info():
    global displayWidth
    global displayHeight
    info = d.info
    displayWidth = info['displayWidth']
    displayHeight = info['displayHeight']
    print("x={}, y={}".format(displayWidth,displayHeight))


def lnsh():
    activity_name = 'com.vpclub.lnyp/.activity.SplashActivity'
    launch_app(activity_name)
    time.sleep(9)
    remove_ad_x = 944
    remove_ad_y = 447
    d.click(remove_ad_x, remove_ad_y)
    time.sleep(2)
    lucky_x = 143
    lucky_y = 678
    d.click(lucky_x, lucky_y)
    time.sleep(8)

    go_x = 545
    go_y = 1033
    d.click(go_x, go_y)
    time.sleep(9)
    print("Ling nan shen huo Done")


def suning_cuizi():
    # 苏宁在6点之后
    global displayWidth
    global displayHeight
    d.screen.on()
    d.press.home()
    '''
    #解锁，没有密码的情况下
    sx=560
    sy=1700
    ex=560
    ey=900
    #d.swipe(sx,sy,ex,ey,steps=2)

    #d(scrollable=True).fling.horiz.forward()
    #d(text=u'苏宁易购').swipe.right()
    home_swipe_sx=950
    home_swipe_sy=1350
    home_swipe_ex=450
    home_swipe_ey=1350
    while not d(text=u"苏宁易购").exists:
        d.swipe(home_swipe_sx,home_swipe_sy,home_swipe_ex,home_swipe_ey,steps=2)
        time.sleep(3)
    d(text=u'苏宁易购').click()
    #time.sleep(10)
    '''
    activity_name = 'com.suning.mobile.ebuy/.base.host.InitialActivity'
    launch_app(activity_name)
    time.sleep(9)
    if not d(text=u'领云钻').wait.exists(timeout=20 * 1000):
        print("Failed to get the page")
        return
    d(text=u'领云钻').click()
    print("Click")
    yun_x = 551
    yun_y = 738

    # glaxy_x=yun_x*gallery*full/cuizi_full
    time.sleep(15)
    d.click(yun_x, yun_y)
    print("Click")
    time.sleep(10)

    daka_x = displayWidth / 2
    daka_y = displayHeight / 2 + 100
    d.click(daka_x, daka_y)
    print("Click")
    time.sleep(20)
    d.click(daka_x, daka_y)
    print("Click")
    d.click(daka_x, daka_y)
    print("Click")
    print("Sunning Done")


def jd_cuizi():
    d.screen.on()
    d.press.home()
    activity_name = 'com.jingdong.app.mall/.main.MainActivity'
    launch_app(activity_name)

    if not d(text=u'领京豆').wait.exists(timeout=20 * 1000):
        print("Failed to get the page")
        return
    d(text=u'领京豆').click()
    dou_x = 915
    dou_y = 300

    # glaxy_x=yun_x*gallery*full/cuizi_full
    time.sleep(15)
    d.click(dou_x, dou_y)
    time.sleep(2)
    d.click(dou_x, dou_y)
    print(u"京豆")
    time.sleep(3)
    get_x, get_y = 505, 900
    d.click(get_x, get_y)
    time.sleep(8)
    d.press.back()
    time.sleep(4)
    liuliang_x, liuliang_y = 731, 574
    d.click(liuliang_x, liuliang_y)
    time.sleep(10)
    ll_x, ll_y = 544, 432
    d.click(ll_x, ll_y)
    time.sleep(8)
    print('京东完成')
    '''
    #点击使用功能
    d.press.back()
    time.sleep(4)
    d.press.back()
    time.sleep(4)
    no_ad_y=775
    ad_y=1250
    d.swipe(990,no_ad_y,100,no_ad_y)
    time.sleep(8)
    #因为这个坐标会改变，所以定义两个变量来操作
    d.click(990,no_ad_y)
    '''
    '''
    if d(text=u'全部').wait.exists(timeout=2000):
        d(text=u'全部').click()
    '''
    '''
    time.sleep(4)
    d(text=u'领流量').click()
    time.sleep(5)
    #这个签到好像找不到
    #d(text=u'签到').click()
    liuliang_x,liuliang_y=529,450
    d.click(liuliang_x,liuliang_y)
    time.sleep(5)
    d.click(liuliang_x,liuliang_y)
    '''

    time.sleep(5)
    print("get liu liang")
    print("JD done")


def gdyd_cuizi():
    d.screen.on()
    d.press.home()
    # 解锁，没有密码的情况下
    sx = 560
    sy = 1700
    ex = 560
    ey = 900
    # d.swipe(sx,sy,ex,ey,steps=2)

    # d(scrollable=True).fling.horiz.forward()
    home_swipe_sx = 950
    home_swipe_sy = 1350
    home_swipe_ex = 450
    home_swipe_ey = 1350
    while not d(text=u"广东移动").exists:
        d.swipe(home_swipe_sx, home_swipe_sy, home_swipe_ex, home_swipe_ey, steps=2)
        time.sleep(3)
    d(text=u'广东移动').click()
    if d(text=u'版本更新').wait.exists(timeout=12 * 1000):
        print("Dismiss update")
        d(text=u'取消').click()
    # 登录账号,刷新下即可
    s_x = 544
    s_y = 367
    e_x = 544
    e_y = 1438
    time.sleep(8)
    d.swipe(s_x, s_y, e_x, e_y, steps=4)

    while not d(text=u"签到赢话费").exists:
        d.swipe(home_swipe_sx, home_swipe_sy, home_swipe_ex, home_swipe_ey, steps=2)
        time.sleep(3)
    d(text=u'签到赢话费').click()
    time.sleep(10)
    yd_x = 540
    yd_y = 1100
    d.click(yd_x, yd_y)
    print("GDYD done")
    d.press.back()
    d(text=u'全部').click()
    time.sleep(8)
    d(text=u'零流量').click()
    time.sleep(8)
    d(text='签到')


def each_dianpu():
    mid_x = displayWidth / 2
    # d.click(919,566)
    time.sleep(4)

    d.click(mid_x, 1868)
    # 点击免费试用
    time.sleep(4)
    d.click(mid_x, 1311)
    time.sleep(4)
    d.click(mid_x, 1555)
    time.sleep(8)
    d.press.back()
    time.sleep(5)
    d.press.back()
    time.sleep(5)
    # 返回到试用列表


def taobao_cuizi():
    d.screen.on()
    d.press.home()

    activity_name = 'com.taobao.taobao/com.taobao.tao.homepage.MainActivity3'
    launch_app(activity_name)
    if d(text=u'领金币').wait.exists(timeout=12 * 1000):
        # print("Dismiss update")
        d(text=u'领金币').click()
    # 登录账号,刷新下即可

    time.sleep(15)
    jb_x = 900
    jb_y = 370
    d.click(jb_x, jb_y)
    print("Click")
    time.sleep(6)


def taobao_shiyong():
    # 一天试用 15次
    d.screen.on()
    d.press.home()

    activity_name = 'com.taobao.taobao/com.taobao.tao.homepage.MainActivity3'
    launch_app(activity_name)
    mid_x = displayWidth / 2
    time.sleep(8)
    d.click(980, 1863)
    try:

        time.sleep(3)
        d(text='查看全部工具').click()
        time.sleep(3)
        d(scrollable=True).scroll.to(text=u'免费试用')
        time.sleep(2)
        d(text=u'免费试用').click()
        time.sleep(8)

        delta_y = 144
        full_y = 1920
        full_x = 1080
        fix_x = 880
        origin_y = 222
        d.swipe(fix_x, full_y - delta_y, fix_x, origin_y)
        time.sleep(8)

        # 数码科技
        # d.click(614,1185)

        # 家用电器
        d.click(890, 1185)
        time.sleep(7)

        delta_each = 400
        time.sleep(3)

        for dragtime in range(5):
            for i in range(3):
                print("Trial")
                d.click(919, 600 + i * delta_each)
                time.sleep(8)
                each_dianpu()

            d.swipe(919, 1600, 919, 400)
            time.sleep(5)
    except:
        print("Can't find items")


def manual_shiyong():
    delta_each = 400
    time.sleep(3)

    for dragtime in range(20):
        print("dragtime")
        for i in range(3):
            d.click(919, 420 + i * delta_each)
            print('click')
            time.sleep(8)
            each_dianpu()
            time.sleep(8)
        d.swipe(919, 420 + delta_each * 3, 919, 400)
        time.sleep(5)


def jd_jr():
    # d.screen.on()
    # d.press.home()

    activity_name = 'com.jd.jrapp/.WelcomeActivity'
    launch_app(activity_name)
    time.sleep(10)

    ME_x = 944
    ME_y = 1868
    print("me")
    d.click(ME_x, ME_y)
    time.sleep(8)

    # 日历
    # rili_x = 677
    # rili_y = 809
    # d.click(rili_x,rili_y)
    # rili_item_x =560
    # rili_item_y = 958
    #
    # d.click(rili_item_x,rili_item_y)
    # time.sleep(5)
    #
    # choujian_x = 523
    # choujian_y = 1265
    #
    # d.click(choujian_x,choujian_y)
    # time.sleep(5)
    #
    # d.press.back()
    # time.sleep(5)
    # d.press.back()
    # time.sleep(5)

    QianDao_x = 126
    QianDao_y = 673
    print("qiandao")
    d.click(QianDao_x, QianDao_y)
    time.sleep(12)
    GangBeng_x = 867
    GangBeng_y = 533
    print("gangben")
    d.click(GangBeng_x, GangBeng_y)
    time.sleep(5)
    print("jd_jr done")
    d.press.back()
    time.sleep(8)
    # QianDao_x=131
    # QianDao_y=767
    d.click(QianDao_x, QianDao_y)
    time.sleep(5)

    # know_x=541
    # know_y=1273
    # d.click(know_x,know_y)
    # time.sleep(3)

    # time.sleep(5)
    GoJD_x = 955
    GoJD_y = 708
    d.click(GoJD_x, GoJD_y)
    time.sleep(10)

    Jindou_x = 860
    Jindou_y = 1046
    d.click(Jindou_x, Jindou_y)
    time.sleep(10)

    qiandao_JD_x = 878
    qiandao_JD_y = 429
    d.click(qiandao_JD_x, qiandao_JD_y)
    time.sleep(8)

    fangpai_x = 548
    fangpai_y = 1004
    d.click(fangpai_x, fangpai_y)
    time.sleep(5)

    shouru_x = 538
    shouru_y = 1623

    d.click(shouru_x, shouru_y)
    time.sleep(9)

    close_x = 939
    close_y = 544
    d.click(close_x, close_y)
    time.sleep(5)

    liuliang_x = 692
    liuliang_y = 997
    d.click(liuliang_x, liuliang_y)
    time.sleep(10)

    liuliang_qiandao_x = 537
    liuliang_qiandao_y = 441

    d.click(liuliang_qiandao_x, liuliang_qiandao_y)
    time.sleep(5)

    d.press.back()
    time.sleep(8)
    d.press.back()
    time.sleep(8)
    d.press.back()
    time.sleep(8)

    finish_x = 870
    finish_y = 1240
    d.click(finish_x, finish_y)
    time.sleep(3)

    print("JD done")


def wjjf():
    activity_name = 'com.hxwj.wjjf/.act.SplashActivity'
    launch_app(activity_name)
    time.sleep(15)

    me_x = 969
    me_y = 1854
    d.click(me_x, me_y)
    time.sleep(9)

    qiandao_x = 371
    qiandao_y = 414
    d.click(qiandao_x, qiandao_y)
    time.sleep(9)


def fxsc():
    activity_name = 'com.phicomm.fxmall/com.phicomm.fxmall.view.MainActivity'
    launch_app(activity_name)
    time.sleep(15)

    me_X = 1002
    me_Y = 1865
    d.click(me_X, me_Y)
    time.sleep(8)

    qiandao_X = 400
    qiandao_Y = 300
    d.click(qiandao_X, qiandao_Y)
    time.sleep(8)

# 中国移动
def cmcc():
    activity_name = 'com.kingpoint.gmcchh/.newui.main.skeleton.view.SkeletonActivity'
    launch_app(activity_name)
    time.sleep(15)

    track_list = [(123,1865),(651,338),(520,957)]
    for step in track_list:
        d.click(step[0],step[1])
        print('click')
        time.sleep(5)


# 支付宝
def alipay():
    activity_name = 'com.eg.android.AlipayGphone/.AlipayLogin'
    launch_app(activity_name)
    time.sleep(10)

    #领取搜索红包
    track_list0 = [(226,163),(188,582),(455,577)]

    for step in track_list0:
        d.click(step[0],step[1])
        print('click')
        time.sleep(5)

    # 点击3次返回到主页
    d.press('back')
    time.sleep(3)
    d.press('back')
    time.sleep(3)
    d.press('back')
    time.sleep(3)

    track_list1 = [(987,1840),(563,491),(155,983),(544,686), # 连续点击
                  (544,686),(544,686),(544,686),(544,686),(544,686),
                  (544,686),(544,686),(544,686),(544,686),(544,686),
                  (544,686),(544,686)]
    for step in track_list1:
        d.click(step[0],step[1])
        print('click')
        time.sleep(5)

# 云闪付
def yunsanfu():
    activity_name = 'com.unionpay/.activity.UPActivityWelcome'
    launch_app(activity_name)
    time.sleep(8)

    track_list = [(981,1389),(541,782)]
    for step in track_list:
        d.click(step[0],step[1])
        time.sleep(5)
    print('云闪付签到完成')

# 华泰 签到
def htzq():
    activity_name ='com.lphtsccft/com.lphtsccft.zhangle.startup.SplashScreenActivity'
    launch_app(activity_name)
    time.sleep(8)

    track_list = [(979, 1855), (950, 296)]
    for step in track_list:
        d.click(step[0], step[1])
        time.sleep(5)

    print('华泰签到完成')

def other_func():
    global displayWidth
    global displayHeight
    print(displayWidth)
    print(displayHeight)


if __name__ == '__main__':
    # 获取基本信息
    get_info()

    yunsanfu()
    alipay()
    cmcc()
    htzq()

