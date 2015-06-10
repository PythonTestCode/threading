import threading
import time

tmp = 0

def func():
	global tmp
	for i in range(10, 15):
		tmp = i
		print "befor %s : tmp=%d" % (threading.currentThread().getName(), tmp)
		time.sleep(1)
		print "after %s : tmp=%d" % (threading.currentThread().getName(), tmp)

if __name__ == "__main__":
	p = threading.Thread(target=func, args=())
	p.start()
	for i in range(0,5):
		tmp = i
		print "befor %s : tmp=%d" % (threading.currentThread().getName(), tmp)
		time.sleep(1)
		print "after %s : tmp=%d" % (threading.currentThread().getName(), tmp)
	p.join()



