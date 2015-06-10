import threading, Queue
import time

g_que = Queue.Queue()

def thread_func():
	global g_que

	while True:
		msg = g_que.get()
		print 'recvmsg =', msg

if __name__ == "__main__":
	p = threading.Thread(target=thread_func, args=())
	p.setDaemon(True)
	p.start()
	tmp = 0

	while True:
		tmp+=1
		print "send msg=",tmp
		g_que.put(tmp)
#		time.sleep(1)
	p.join()



