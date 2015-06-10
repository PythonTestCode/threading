import threading
import time

def thread_func():
	time.sleep(1)
	print "thread subThread", threading.currentThread()
	print "call thread func"

def test():
	p = threading.Thread(target=thread_func, args=())
	p.setDaemon(True)
	p.start()
	print "thread count=", threading.activeCount()
	print "thread CurThread", threading.currentThread()
	print "thread list", threading.enumerate()
	return p

if __name__ == '__main__':
	p = test()
	p.join()


