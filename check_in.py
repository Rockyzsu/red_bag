# -*-coding=utf-8-*-
__author__ = 'Rocky'
#对各种app进行签到
from uiautomator import device as d
import time,subprocess

global displayWidth
global displayHeight
displayWidth_cuizi=1080
displayHeight_cuizi=1920
def launch_app(activity_name):
    cmd='adb shell am start -n %s' %activity_name
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    print p.stdout.read()
    time.sleep(15)

def get_info():
    global displayWidth
    global displayHeight
    info=d.info
    displayWidth=info['displayWidth']
    displayHeight=info['displayHeight']
    #print 'x=%s, y=%s ' %(displayWidth,displayHeight)

def suning_cuizi():
    #苏宁在6点之后
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
    activity_name='com.suning.mobile.ebuy/.base.host.InitialActivity'
    launch_app(activity_name)
    if not d(text=u'领云钻').wait.exists(timeout=20*1000):
        print "Failed to get the page"
        return
    d(text=u'领云钻').click()
    print "Click"
    yun_x=372
    yun_y=1524

    #glaxy_x=yun_x*gallery*full/cuizi_full
    time.sleep(15)
    d.click(yun_x,yun_y)
    print "Click"
    time.sleep(10)

    daka_x=displayWidth/2
    daka_y=displayHeight/2+100
    d.click(daka_x,daka_y)
    print "Click"
    time.sleep(20)
    d.click(daka_x,daka_y)
    print "Click"
    d.click(daka_x,daka_y)
    print "Click"
    print "Sunning Done"

def jd_cuizi():
    d.screen.on()
    d.press.home()
    activity_name='com.jingdong.app.mall/.main.MainActivity'
    launch_app(activity_name)

    if not d(text=u'领京豆').wait.exists(timeout=20*1000):
        print "Failed to get the page"
        return
    d(text=u'领京豆').click()
    dou_x=853
    dou_y=400

    #glaxy_x=yun_x*gallery*full/cuizi_full
    time.sleep(15)
    d.click(dou_x,dou_y)
    print "Click"
    time.sleep(2)
    d.click(dou_x,dou_y)
    print "Click"


    print "JD done"

def gdyd_cuizi():
    d.screen.on()
    d.press.home()
    #解锁，没有密码的情况下
    sx=560
    sy=1700
    ex=560
    ey=900
    #d.swipe(sx,sy,ex,ey,steps=2)

    #d(scrollable=True).fling.horiz.forward()
    home_swipe_sx=950
    home_swipe_sy=1350
    home_swipe_ex=450
    home_swipe_ey=1350
    while not d(text=u"广东移动").exists:
        d.swipe(home_swipe_sx,home_swipe_sy,home_swipe_ex,home_swipe_ey,steps=2)
        time.sleep(3)
    d(text=u'广东移动').click()
    if d(text=u'版本更新').wait.exists(timeout=12*1000):
        print "Dismiss update"
        d(text=u'取消').click()
    #登录账号,刷新下即可
    s_x=544
    s_y=367
    e_x=544
    e_y=1438
    time.sleep(8)
    d.swipe(s_x,s_y,e_x,e_y,steps=4)

    while not d(text=u"签到赢话费").exists:
        d.swipe(home_swipe_sx,home_swipe_sy,home_swipe_ex,home_swipe_ey,steps=2)
        time.sleep(3)
    d(text=u'签到赢话费').click()
    time.sleep(10)
    yd_x=540
    yd_y=1100
    d.click(yd_x,yd_y)
    print "GDYD done"


def taobao_cuizi():
    d.screen.on()
    d.press.home()
    #解锁，没有密码的情况下
    '''
    sx=560
    sy=1700
    ex=560
    ey=900
    #d.swipe(sx,sy,ex,ey,steps=2)

    #d(scrollable=True).fling.horiz.forward()
    home_swipe_sx=950
    home_swipe_sy=1350
    home_swipe_ex=450
    home_swipe_ey=1350
    while not d(text=u"手机淘宝").exists:
        d.swipe(home_swipe_sx,home_swipe_sy,home_swipe_ex,home_swipe_ey,steps=2)
        time.sleep(3)
    d(text=u'手机淘宝').click()
    '''
    activity_name='com.taobao.taobao/com.taobao.tao.homepage.MainActivity3'
    launch_app(activity_name)
    if d(text=u'领金币').wait.exists(timeout=12*1000):
        #print "Dismiss update"
        d(text=u'领金币').click()
    #登录账号,刷新下即可

    time.sleep(15)
    jb_x=900
    jb_y=370
    d.click(jb_x,jb_y)
    print "Click"
    time.sleep(5)

def suning_samsung():
    #苏宁在6点之后
    global displayWidth
    global displayHeight
    #d.screen.on()
    d.press.home()
    #解锁，没有密码的情况下
    sx=560
    sy=1700
    ex=560
    ey=900
    #d.swipe(sx,sy,ex,ey,steps=2)

    #d(scrollable=True).fling.horiz.forward()
    #d(text=u'苏宁易购').swipe.right()
    home_swipe_sx=627
    home_swipe_sy=900
    home_swipe_ex=120
    home_swipe_ey=900
    while not d(text=u"苏宁易购").exists:
        d.swipe(home_swipe_sx,home_swipe_sy,home_swipe_ex,home_swipe_ey,steps=2)
        time.sleep(3)
    d(text=u'苏宁易购').click()
    #time.sleep(10)
    if not d(text=u'领云钻').wait.exists(timeout=30*1000):
        print "Failed to get the page"
        return
    d(text=u'领云钻').click()
    yun_x=256
    yun_y=1019

    #glaxy_x=yun_x*gallery*full/cuizi_full
    time.sleep(15)
    d.click(yun_x,yun_y)
    time.sleep(10)

    daka_x=displayWidth/2
    daka_y=displayHeight/2
    d.click(daka_x,daka_y)
    time.sleep(20)
    print "Sunning Done"

def jd_samsung():
    d.screen.on()
    d.press.home()
    #解锁，没有密码的情况下
    sx=560
    sy=1700
    ex=560
    ey=900
    #d.swipe(sx,sy,ex,ey,steps=2)

    #d(scrollable=True).fling.horiz.forward()
    home_swipe_sx=627
    home_swipe_sy=900
    home_swipe_ex=120
    home_swipe_ey=900
    while not d(text=u"手机京东").exists:
        d.swipe(home_swipe_sx,home_swipe_sy,home_swipe_ex,home_swipe_ey,steps=2)
        time.sleep(3)
    d(text=u'手机京东').click()
    if not d(text=u'领京豆').wait.exists(timeout=20*1000):
        print "Failed to get the page"
        return
    d(text=u'领京豆').click()
    dou_x=853
    dou_y=400

    #glaxy_x=yun_x*gallery*full/cuizi_full
    time.sleep(15)
    d.click(dou_x,dou_y)
    print "JD done"

def gdyd_samsung():
    d.screen.on()
    d.press.home()
    #解锁，没有密码的情况下
    sx=560
    sy=1700
    ex=560
    ey=900
    #d.swipe(sx,sy,ex,ey,steps=2)

    #d(scrollable=True).fling.horiz.forward()
    home_swipe_sx=627
    home_swipe_sy=900
    home_swipe_ex=120
    home_swipe_ey=900
    while not d(text=u"广东移动").exists:
        d.swipe(home_swipe_sx,home_swipe_sy,home_swipe_ex,home_swipe_ey,steps=2)
        time.sleep(3)
    d(text=u'广东移动').click()
    if d(text=u'版本更新').wait.exists(timeout=12*1000):
        print "Dismiss update"
        d(text=u'取消').click()
    #登录账号,刷新下即可
    s_x=544
    s_y=367
    e_x=544
    e_y=1438
    time.sleep(8)
    d.swipe(s_x,s_y,e_x,e_y,steps=4)

    while not d(text=u"签到赢话费").exists:
        d.swipe(home_swipe_sx,home_swipe_sy,home_swipe_ex,home_swipe_ey,steps=2)
        time.sleep(3)
    d(text=u'签到赢话费').click()
    time.sleep(10)
    yd_x=540
    yd_y=1100
    d.click(yd_x,yd_y)
    print "GDYD done"


def taobao_samsung():
    d.screen.on()
    d.press.home()
    #解锁，没有密码的情况下
    sx=560
    sy=1700
    ex=560
    ey=900
    #d.swipe(sx,sy,ex,ey,steps=2)

    #d(scrollable=True).fling.horiz.forward()
    home_swipe_sx=627
    home_swipe_sy=900
    home_swipe_ex=120
    home_swipe_ey=900
    while not d(text=u"手机淘宝").exists:
        d.swipe(home_swipe_sx,home_swipe_sy,home_swipe_ex,home_swipe_ey,steps=2)
        time.sleep(3)
    d(text=u'手机淘宝').click()
    if d(text=u'领金币').wait.exists(timeout=12*1000):
        print "Dismiss update"
        d(text=u'领金币').click()
    #登录账号,刷新下即可

    time.sleep(15)
    jb_x=900
    jb_y=370
    d.click(jb_x,jb_y)

def other_func():
    global displayWidth
    global displayHeight
    print displayWidth
    print displayHeight

if __name__=='__main__':
    get_info()

    suning_cuizi()
    #other_func()
    jd_cuizi()
    #广东移动新版已经没有签到功能
    #gdyd_cuizi()
    taobao_cuizi()
    #suning_samsung()
    #jd_samsung()
    #taobao_samsung()
