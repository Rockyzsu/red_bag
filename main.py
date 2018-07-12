# -*-coding=utf-8-*-
from uiautomator import device as d


# print d.info

def QQ_red_bag():
    i = 0
    while i < 10:
        d.screen.on()
        d(scrollable=True).scroll(steps=3)
        # d(textContains=u'红包').click()
        if d(textContains=u'红包').exists:
            print "Have red bag"
            d(textContains=u'新年快乐').click()

        i = i + 1


def wechat():
    x = 511
    y = 1627
    while 1:
        d.click(x, y)
        d.click(520, 1300)


if __name__ == "__main__":
    QQ_red_bag()
# wechat()
