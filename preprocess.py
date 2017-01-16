import sys
import os
import re

from porterStemmer import *

def removeSGML(input):
	#removes < > & their content
	strlist = []
	for c in input:
		strlist.append(c)
	if '<' in strlist and '>' in strlist:
		for firstndx in range(len(strlist)):
			if strlist[firstndx] == '<':
				break;

		secondndx = -1
		for i in range(len(strlist)):
			if strlist[i] == '>':
				secondndx = i

	while firstndx <= secondndx:
		strlist[firstndx] = ''
		firstndx += 1

	input = ''.join(strlist)
	return input
#--------------------------------------------------------------------
#--------------------------------------------------------------------

def comma(input):
	if ',' not in input:
		return input

def singleCharacter(input):
	# a single character to be a token must be alphanumeric
	if (len(input) == 1):
		input = re.sub('[^a-zA-z0-9]', '', input)
	return input

def removeOdd(input):
	# Removes special characters from a string, does not remove . ' , - 
	if (len(input) == 0):
		return input
	punctuation = '~`!@#$%^&*()_+={}|<>?"'
	input = re.sub('[' + punctuation + ']', '', input)
	input = input.replace('\\', '')
	input = input.replace('/', '')
	input = input.replace('[', '')
	input = input.replace(']', '')
	return input


def tokenizeText(input):
	tokens = []
	words = input.split()
	for w in words:
		w = removeOdd(w)
		w = singleCharacter(w)
		tokens.append(w)
	return tokens

#--------------------------------------------------------------------
#--------------------------------------------------------------------

def getStopwords():
	# read stopwords to list from file
	stopwords = []
	path = os.path.join(os.getcwd(), 'stopwords')
	lines = [line.rstrip('\n') for line in open(path)]
	lines = [line.strip(' ') for line in lines]

	for line in lines:
		stopwords.append(line)

	return stopwords

def removeStopwords(tokens):
	# remove stopwords from tokens
	stopwords = getStopwords()
	output = []
	for t in tokens:
		if t not in stopwords:
			output.append(t)
	
	return output

#--------------------------------------------------------------------
#--------------------------------------------------------------------
def stemWords(tokens):
	output = []
	return output


#--------------------------------------------------------------------
#--------------------------------------------------------------------
def main():
	#print 'Argument List:', str(sys.argv)
	try: 
		foldername = str(sys.argv[1])
	except:
		sys.exit("ERROR: no folder of that name")

	path = os.path.join(os.getcwd(), foldername)

	for filename in os.listdir(path):
		#print str(filename)
		path2file = os.path.join(path, filename)
		lines = [line.rstrip('\n') for line in open(path2file)]

	
		for i in range(len(lines)):
			lines[i] = removeSGML(lines[i])

		while '' in lines:
			lines.remove('')

		#print lines

	myline = lines[5]
	words = tokenizeText(myline)
	print (words)

	words = removeStopwords(words)
	print(words)


if __name__ == "__main__": 
	main()