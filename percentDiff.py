import sys
import os
import re
import math


def main():
	#print 'Argument List:', str(sys.argv)

	filename = 'languageIdentification.data/solution'
	path = os.path.join(os.getcwd(), filename)
	lines = [line.rstrip('\n') for line in open(path)]

	filename2 = 'languageIdentification.output'
	path2 = os.path.join(os.getcwd(), filename2)
	lines2 = [line.rstrip('\n') for line in open(path2)]


	numIncorrect = 0
	i = 0
	
	while (i < len(lines)):
		if lines[i] != lines2[i]:
			numIncorrect += 1
			print ("Error on line ", (i + 1), "\n   Correct: ", lines[i], " Output: ", lines2[i])
		i += 1

	percent = 100 - (float(numIncorrect)/float(300) * 100)

	print ("Percent correct: ", percent)



if __name__ == "__main__": 
	main()