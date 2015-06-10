import threading
import time

tmp = 0

g_lock = threading.Lock()

def func():
	global tmp
	global g_lock

	for i in range(20, 40):
		g_lock.acquire()
		tmp -=1
		print "%s : tmp=%d" % (threading.currentThread().getName(), tmp)
		g_lock.release()
#		time.sleep(1)
	

if __name__ == "__main__":
	p = threading.Thread(target=func, args=())
	p.setDaemon(True)
	p.start()


	for i in range(0, 20):
		g_lock.acquire()
		tmp +=1
		print "%s : tmp=%d" % (threading.currentThread().getName(), tmp)
		g_lock.release()
#		time.sleep(1)
	p.join()



