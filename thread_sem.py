import threading
import time
tmp = 0

g_sem= threading.Semaphore(1)
g_sem.release()

def func():
	global tmp
	global g_sem
	print "%s start get sem" % (threading.currentThread().getName())
	g_sem.acquire()
	print "%s get sem start sleep" % (threading.currentThread().getName())
	time.sleep(5)
	print "%s release sem " % (threading.currentThread().getName())
	g_sem.release()

if __name__ == "__main__":
	p = threading.Thread(target=func, args=())
	p.setDaemon(True)
	p.start()
	print "%s start get sem" % (threading.currentThread().getName())
	g_sem.acquire()
	print "%s get sem start sleep" % (threading.currentThread().getName())
	time.sleep(5)
	print "%s release sem " % (threading.currentThread().getName())
	g_sem.release()
	p.join()



