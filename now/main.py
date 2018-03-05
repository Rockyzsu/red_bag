from uiautomator import device as d
import time,sys
def now(wait_time):
	x=943
	# y=
	y=742
	while wait_time>0:
		time.sleep(1)
		wait_time-=1
	count=100
	while count>0:
		print "Clicking......."
		d.click(x,y)
		time.sleep(0.001)
		count-=1

def main():
	m=1
	s=35
	wait_time=m*60+s+2
	now(wait_time)

if __name__ == '__main__':
	print 'Start'
	main()