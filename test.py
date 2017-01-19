import re

def identifyFormattedNumbers(input):
	#finds alphanumeric hypenated phrases
	tokens = []
	if '.' not in input and ',' not in input:
		return input, tokens

	#numbers containing at least a comma, followed by any string of commas, followed by an optional decimal
	#thousandth place comma enforced
	match = re.findall(r'\d+,\d{3}[,\d{3}]*[.]{0,1}[\d+]*', input)
	if match != None:
		for m in match:
			tokens.append(m)
		input = re.sub(r'\d+,\d{3}[,\d{3}]*[.]{0,1}[\d+]*', '', input)

	#numbers and numbers containing optional commas and a decimal point
	match = re.findall(r'\d+[,\d{3}]*[.]\d+', input)
	if match != None:
		for m in match:
			tokens.append(m)

	print tokens
	return input, tokens





def main():
	mylist = []
	test = 'here is a 12a.b test 100?23 100.323 123 1000000.23 10,000,000.23 string 10,00 that 10,000,000 contains, 1,000.37 commas,that separate, words 1,100 and numbers'

	test, mylist = identifyFormattedNumbers(test)

	test = "this is a test for th'hs here-is-a-phrase do-i-want 93-thousand contractions 09-38-le9t 99-99-99 jack-in-the-box I'm HERE'RE i'm she's we're they're hasn't can't alex's"

	#test, mylist = identifyPhrases(test)

if __name__ == "__main__": 
	main()