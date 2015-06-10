import threading
import time

tmp = 0

g_lock = threading.Lock()

def thread_func():
	global g_cond
	global tmp

	while True:
		g_lock.acquire()
		if(tmp >= 0):
			print "sub tmp=",tmp
			tmp = tmp -1
		g_lock.release()

if __name__ == "__main__":
	p = threading.Thread(target=thread_func, args=())
	p.setDaemon(True)
	p.start()

	i = 0
	while True:
		i=i+1
		g_lock.acquire()
		tmp += 1
		print "main tmp=d", tmp
		g_lock.release()
		if(i > 500):
			break

