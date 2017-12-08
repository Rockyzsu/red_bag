# -*-coding=utf-8-*-
__author__ = 'Rocky'
#对各种app进行签到
from uiautomator import device as d
import time,subprocess,sys

global displayWidth
global displayHeight
displayWidth_cuizi=1080
displayHeight_cuizi=1920
#启动app
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
    time.sleep(9)
    if not d(text=u'领云钻').wait.exists(timeout=20*1000):
        print "Failed to get the page"
        return
    d(text=u'领云钻').click()
    print "Click"
    yun_x=551
    yun_y=738

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
    dou_x=915
    dou_y=300

    #glaxy_x=yun_x*gallery*full/cuizi_full
    time.sleep(15)
    d.click(dou_x,dou_y)
    time.sleep(2)
    d.click(dou_x,dou_y)
    print u"京豆"
    time.sleep(3)
    get_x,get_y=505,900
    d.click(get_x,get_y)
    time.sleep(8)
    d.press.back()
    time.sleep(4)
    liuliang_x,liuliang_y=731,574
    d.click(liuliang_x,liuliang_y)
    time.sleep(10)
    ll_x,ll_y=544,432
    d.click(ll_x,ll_y)
    time.sleep(8)
    print u'京东完成'
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
    print "get liu liang"
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
    d.press.back()
    d(text=u'全部').click()
    time.sleep(8)
    d(text=u'零流量').click()
    time.sleep(8)
    d(text='签到')

def each_dianpu():
    mid_x=displayWidth/2
    #d.click(919,566)
    time.sleep(4)

    d.click(mid_x,1868)
    #点击免费试用
    time.sleep(4)
    d.click(mid_x,1311)
    time.sleep(4)
    d.click(mid_x,1555)
    time.sleep(8)
    d.press.back()
    time.sleep(5)
    d.press.back()
    time.sleep(5)
    #返回到试用列表



def taobao_cuizi():

    d.screen.on()
    d.press.home()

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
    time.sleep(6)


def taobao_shiyong():
    #一天试用 15次
    d.screen.on()
    d.press.home()

    activity_name='com.taobao.taobao/com.taobao.tao.homepage.MainActivity3'
    launch_app(activity_name)
    mid_x=displayWidth/2
    time.sleep(8)
    d.click(980,1863)
    try:

        time.sleep(3)
        d(text='查看全部工具').click()
        time.sleep(3)
        d(scrollable=True).scroll.to(text=u'免费试用')
        time.sleep(2)
        d(text=u'免费试用').click()
        time.sleep(8)


        delta_y=144
        full_y=1920
        full_x=1080
        fix_x=880
        origin_y=222
        d.swipe(fix_x,full_y-delta_y,fix_x,origin_y)
        time.sleep(8)

        #数码科技
        #d.click(614,1185)

        #家用电器
        d.click(890,1185)
        time.sleep(7)


        delta_each=400
        time.sleep(3)

        for dragtime in range(5):
            for i in range(3):
                print "Trial"
                d.click(919,600+i*delta_each)
                time.sleep(8)
                each_dianpu()

            d.swipe(919,1600,919,400)
            time.sleep(5)
    except:
        print "Can't find items"

def manual_shiyong():
    delta_each=400
    time.sleep(3)

    for dragtime in range(20):
        print 'dragtime'
        for i in range(3):
            d.click(919,420+i*delta_each)
            print 'click'
            time.sleep(8)
            each_dianpu()
            time.sleep(8)
        d.swipe(919,420+delta_each*3,919,400)
        time.sleep(5)

def other_func():
    global displayWidth
    global displayHeight
    print displayWidth
    print displayHeight

if __name__=='__main__':
    #print sys.argv[0]
    #print sys.argv[1]
    if len(sys.argv)<2:
        print "input argument"
        print 'python checkin.py 1'
        print 'python checkin.py 2'

        sys.exit(1)
    get_info()
    if sys.argv[1]=='1':

        suning_cuizi()
        jd_cuizi()
        #taobao_cuizi()
        #print "on shi yong"
        #taobao_shiyong()

    elif sys.argv[1]=='2':
        print "put UI on taobao trial\n"
        time.sleep(5)
        manual_shiyong()
    elif sys.argv[1]=='3':
        print "only click jd"
        jd_cuizi()
