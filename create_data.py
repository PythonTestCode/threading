import random
import sys

'''
1:
name_1:90
name_2:80
name_n:nn
'''

def construct_data(f):
	fp = open(f, 'w')
	for i in range(40):
		name = 'name_' + str(i) + ':' + str(random.randint(50, 100)) + '\n'
		fp.writelines(name)
	fp.close()


def create_data(file):
	for f in file:
		construct_data(f)

if __name__ == '__main__':
	print sys.argv[1:]
	create_data(sys.argv[1:])


