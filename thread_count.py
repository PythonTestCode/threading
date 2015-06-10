import sys
import re
import threading

'''
subject: thread
filename 
subjectname
socrelist 
averageScore
run:
'''

class subject(threading.Thread):
	def __init__(self, threadname, filename):
		threading.Thread.__init__(self, name=threadname)
		self.fileName = filename
		self.subjectName = filename[:-4]
		self.scoreList = []
		self.averageScore = 0

	def run(self):
#	def count_result(self):
		print self.getName()
		fp = open(self.fileName)
		f_iter = iter(fp)

		for line in f_iter:
			score = re.search(r':(100|[1-9]?[0-9])$', line[:len(line)-1])
			if(score):
				self.scoreList.append(int(score.group()[1:]))
			else:
				print "errorline:", line
		fp.close()
		self.averageScore = sum(self.scoreList)/float(len(self.scoreList))
#		print self.fileName, ":", self.averageScore

	

def main_count(filelist):
	listSubject = []
	for f in filelist:
		s = subject(f[:-4],f)
		s.start()
		listSubject.append(s)

	for obj in listSubject:
		obj.join()
		print obj.subjectName, " average:", obj.averageScore


if __name__ == '__main__':
	print sys.argv[1:]
	main_count(sys.argv[1:])
