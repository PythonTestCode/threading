import threading
import time

tmp = 0
g_cond = threading.Condition()

def thread_func():
	global g_cond
	global tmp

	print "sub thread acquire lock"
	g_cond.acquire()
	time.sleep(3)
	while True:
		if tmp >= 3:
			tmp = tmp -1
			print "sub tmp=",tmp
		else:
		 	print "wait singnal wake up"
			g_cond.wait()
			print "wake up by another thread"
	g_cond.release()

if __name__ == "__main__":
	p = threading.Thread(target=thread_func, args=())
	p.setDaemon(True)
	p.start()

	time.sleep(1)
	while True:
		g_cond.acquire()
		if tmp >= 3:
			print "notify sub thread"
			g_cond.notify()
		else:
			tmp += 1
			print 'main tmp=', tmp

		time.sleep(1)
		print " release lock"
		g_cond.release()
		time.sleep(1)
	p.join()



