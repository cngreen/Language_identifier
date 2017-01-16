import sys
import os
import re

from porterStemmer import *

#--------------------------------------------------------------------
def removeSGML(input):
	#print("input: ", input)
	if '<' in input and '>' in input: #if there are tag characters find the tags
		strlist = []
		for c in input:
			strlist.append(c)


		firstndx = -1
		secondndx = -1
		# find the first < of the line
		for i in range(len(strlist)):
			if strlist[i] == '<':
				firstndx = i
				break

		#print("starting index: ", firstndx)

		# find the first > of the line
		for i in range(len(strlist)):
			if strlist[i] == '>':
				secondndx = i
				break

		#print("ending index: ", secondndx)

		quotendx = -1
		temp = firstndx
		# check if there is attribute quotations in tag (risk for extra >)
		while temp <= secondndx:
			if strlist[temp] == '"':
				quotendx = temp
				break
			temp += 1


		if quotendx != -1: #there is a quotation in the tag
			quotendx2 = -1
			temp = quotendx + 1
			# make sure the quotation ends
			while temp <= secondndx:
				if strlist[temp] == '"':
					quotendx2 = temp
					break
				temp += 1

			if quotendx2 != -1: #the quote ended, remove quoted content:
				while quotendx <= quotendx2:
					strlist[quotendx] = ''
					quotendx += 1
				input = ''.join(strlist)
				return(removeSGML(input)) #rerun the remove SGML without the quote
			
			else: #find end of quote:
				temp = quotendx + 1
				while temp <= len(strlist):
					if strlist[temp] == '"':
						quotendx2 = temp
						break
					temp += 1

				if quotendx2 != -1: #the quote ended, remove quoted content:
					while quotendx <= quotendx2:
						strlist[quotendx] = ''
						quotendx += 1
					input = ''.join(strlist)
					return(removeSGML(input)) #rerun the remove SGML without the quote

				else: #the quote doesn't end on this line
					sys.exit("ERROR: quotation in SGML tag does not end")




	# remove all chars between first < and first > of the line
		#print("remove from: ", firstndx, " to: ", secondndx)
		while firstndx <= secondndx:
			strlist[firstndx] = ''
			firstndx += 1
		input = ''.join(strlist) #check if there are more remaining
		return(removeSGML(input))

	#otherwise output the input
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
	p = PorterStemmer()

	for t in tokens:
		if len(t) == 0:
			continue
		output.append(p.stem(t, 0, len(t)-1))

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