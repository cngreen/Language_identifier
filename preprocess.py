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

		# find the first > of the line
		for i in range(len(strlist)):
			if strlist[i] == '>':
				secondndx = i
				break


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
			while temp <= secondndx: #check from just after the quote to the end of the tag
				if strlist[temp] == '"':
					quotendx2 = temp
					break
				temp += 1

			print("quotendx2", quotendx2)

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

def indentifyDates(input):
	#finds numerical dates with years of 4 or two digits separated by - / . or ,
	#returns dates in a list, removes them from the input string
	matches = []

	months = [] #list of common month abbrev.
	months.extend(['january', 'jan', 'jan.'])
	months.extend(['february', 'feb', 'feb.'])
	months.extend(['march', 'mar', 'mar.'])
	months.extend(['april', 'apr', 'apr.'])
	months.extend(['may', 'may.'])
	months.extend(['june', 'jun', 'jun.'])
	months.extend(['july', 'jul', 'jul.'])
	months.extend(['august', 'aug', 'aug.'])
	months.extend(['september', 'sep', 'sep.', 'sept', 'sept.'])
	months.extend(['october', 'oct', 'oct.'])
	months.extend(['november', 'nov', 'nov.'])
	months.extend(['december', 'dec', 'dec.'])
	#print months
	
	# XXXX-X/X-X/X year(4), month, day sep by - / . or ,
	match = re.findall(r'\d{4}[-/.,]\d{1,2}[-/.,]\d{1,2}', input)
	if match != None:
		for m in match:
			matches.append(m)
		input = re.sub(r'\d{4}[-/.,]\d{1,2}[-/.,]\d{1,2}', '', input)
		
	# X/X-X/X-XXXX day, month, year(4) sep by - / . or ,
	match = re.findall(r'\d{1,2}[-/.,]\d{1,2}[-/.,]\d{4}', input)
	if match != None:
		for m in match:
			matches.append(m)
		input = re.sub(r'\d{1,2}[-/.,]\d{1,2}[-/.,]\d{4}', '', input)

	#XX-X/X-X/X year(2), month, day sep by - / . or ,
	match = re.findall(r'\d{2}[-/.,]\d{1,2}[-/.,]\d{1,2}', input)
	if match != None:
		for m in match:
			matches.append(m)
		input = re.sub(r'\d{2}[-/.,]\d{1,2}[-/.,]\d{1,2}', '', input)
	#X/X-X/X-XX day, month, year(2) sep by - / . or ,
	match = re.findall(r'\d{1,2}[-/.,]\d{1,2}[-/.,]\d{2}', input)
	if match != None:
		for m in match:
			matches.append(m)
		input = re.sub(r'\d{1,2}[-/.,]\d{1,2}[-/.,]\d{2}', '', input)

	#abc-X/X-XX alpha month, day, year(4) 
	match = re.findall(r'[a-zA-z]{3,9}[.]*\s*[-./,]*\d{1,2}[-/.,]*\s*\d{4}', input)
	if match != None:
		input = re.sub(r'[a-zA-z]{3,9}[.]*\s*[-./,]*\d{1,2}[-/.,]*\s*\d{4}', '', input)
		for m in match:
			month = re.findall(r'[a-zA-z]+', m)
			month = str(month[0]).lower()
			if month in months:
				matches.append(m)
			else:
				input += (' ' + str(m)) #don't remove it if it wasn't a date

	#X/X-abc-XXXX day, month, year(4)
	match = re.findall(r'\d{1,2}[-/.,]*\s*[a-zA-z]{3,9}[.]*\s*[-./,]*\d{4}', input)
	if match != None:
		input = re.sub(r'\d{1,2}[-/.,]*\s*[a-zA-z]{3,9}[.]*\s*[-./,]*\d{4}', '', input)
		for m in match:
			month = re.findall(r'[a-zA-z]+', m)
			month = str(month[0]).lower()
			if month in months:
				matches.append(m)
			else:
				input += (' ' + str(m)) #don't remove it if it wasn't a date

	#year(4), month, day
	match = re.findall(r'\d{4}[-/.,]*\s*[a-zA-z]{3,9}[.]*\s*[-./,]*\d{1,2}', input)
	if match != None:
		input = re.sub(r'\d{4}[-/.,]*\s*[a-zA-z]{3,9}[.]*\s*[-./,]*\d{1,2}', '', input)
		for m in match:
			month = re.findall(r'[a-zA-z]+', m)
			month = str(month[0]).lower()
			if month in months:
				matches.append(m)
			else:
				input += (' ' + str(m)) #don't remove it if it wasn't a date

	#abc-X/X-XX alpha month, day, year(2) 
	match = re.findall(r'[a-zA-z]{3,9}[.]*\s*[-./,]*\d{1,2}[-/.,]*\s*\d{2}', input)
	if match != None:
		input = re.sub(r'[a-zA-z]{3,9}[.]*\s*[-./,]*\d{1,2}[-/.,]*\s*\d{2}', '', input)
		for m in match:
			month = re.findall(r'[a-zA-z]+', m)
			month = str(month[0]).lower()
			if month in months:
				matches.append(m)
			else:
				input += (' ' + str(m)) #don't remove it if it wasn't a date

	#X/X-abc-XXXX day, month, year(2)
	match = re.findall(r'\d{1,2}[-/.,]*\s*[a-zA-z]{3,9}[.]*\s*[-./,]*\d{2}', input)
	if match != None:
		input = re.sub(r'\d{1,2}[-/.,]*\s*[a-zA-z]{3,9}[.]*\s*[-./,]*\d{2}', '', input)
		for m in match:
			month = re.findall(r'[a-zA-z]+', m)
			month = str(month[0]).lower()
			if month in months:
				matches.append(m)
			else:
				input += (' ' + str(m)) #don't remove it if it wasn't a date

	#year(2), month, day
	match = re.findall(r'\d{2}[-/.,]*\s*[a-zA-z]{3,9}[.]*\s*[-./,]*\d{1,2}', input)
	if match != None:
		input = re.sub(r'\d{2}[-/.,]*\s*[a-zA-z]{3,9}[.]*\s*[-./,]*\d{1,2}', '', input)
		for m in match:
			month = re.findall(r'[a-zA-z]+', m)
			month = str(month[0]).lower()
			if month in months:
				matches.append(m)
			else:
				input += (' ' + str(m)) #don't remove it if it wasn't a date
				
	return input, matches

def tokenizeText(input):
	tokens = []

	input, dates = indentifyDates(input)
	tokens.extend(dates)

	words = input.split()
	for w in words:
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