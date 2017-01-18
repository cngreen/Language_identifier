import re

def indentifyDates(input):
	#finds numerical dates with years of 4 or two digits separated by - / . or ,
	matches = []

	# XXXX-X/X-X/X
	print(input)
	match = re.findall(r'\d{4}[-/.,]\d{1,2}[-/.,]\d{1,2}', input)
	if match != None:
		for m in match:
			matches.append(m)
		input = re.sub(r'\d{4}[-/.,]\d{1,2}[-/.,]\d{1,2}', '', input)
		
	# X/X-X/X-XXXX
	match = re.search(r'\d{1,2}[-/.,]\d{1,2}[-/.,]\d{4}', input)
	if match != None:
		matches.append(match.group())

	#XX-X/X-X/X
	match = re.search(r'\d{2}[-/.,]\d{1,2}[-/.,]\d{1,2}', input)
	if match != None:
		matches.append(match.group())
	#X/X-X/X-XX
	match = re.search(r'\d{1,2}[-/.,]\d{1,2}[-/.,]\d{2}', input)
	if match != None:
		matches.append(match.group())

	print matches
	return



def main():
	test = 'here is a 1031/1/20 string with 1.1.16 a of 1, 2017 dates 1015/12/1 may 17, 1993 3.3.16 1-1-10 string string'

	indentifyDates(test)

if __name__ == "__main__": 
	main()