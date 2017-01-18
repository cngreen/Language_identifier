import re

def indentifyDates(input):
	matches = []
	#finds dates of format 01.01.17 01/01/17 01.01.2017 01/01/2017 01-01-17 01-01-2017 
	# 1.1.17 1/1/17 1.1.2017 1/1/2017 1-1-17 1-1-2017
	# 1, 17 01, 17 1, 2017 01, 2017


	# XXXX-X/X-X/X
	match = re.search(r'\d{4}[-/.]\d{1,2}[-/.]\d{1,2}', input)
	if match != None:
		matches.append(match.group())
	# X/X-X/X-XXXX
	match = re.search(r'\d{1,2}-\d{1,2}-\d{4}', input)
	if match != None:
		matches.append(match.group())


	print matches
	return



def main():
	test = 'here is a 1031/1/20 string with 1.1.16 a of 1, 2017 dates may 17, 1993 3.3.16 1-1-10 string string'

	indentifyDates(test)

if __name__ == "__main__": 
	main()