#!/usr/bin/python
import sys

def on_even(num):
	return num / 2

def on_odd(num):
	#return num * 3 + 1
	return num + 1

def Collatz(argv=None):
	if argv == None:
		argv = sys.argv
	for i,num in enumerate(argv):
		if i == 0:
			continue
		else:
			try:
				num = int(num)
				if num < 0:
					print "%s is not a valid number." % num
					continue
				print str(num)
				while(num != 1):
					if num % 2 == 0:
						num = on_even(num)
					else:
						num = on_odd(num)
					print "\t" + str(num)
			except ValueError:
				print "%s is not a valid number." % num
	return 1

if __name__=="__main__":
	sys.exit(Collatz())
