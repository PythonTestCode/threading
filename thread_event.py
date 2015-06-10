import threading
import time

g_event = threading.Event()

def thread_func():
	global g_event

	while True:
		if(g_event.isSet()):
			g_event.clear()

		print "start Wait"
		g_event.wait()
		print "Break Wait"

if __name__ == "__main__":
	p = threading.Thread(target=thread_func, args=())
	p.setDaemon(True)
	p.start()

	while True:
		time.sleep(1)
		g_event.set()
	p.join()



