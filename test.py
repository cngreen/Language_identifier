import re

def identifyFormattedNumbers(input):
	#finds formatted numbers
	tokens = []
	if '.' not in input and ',' not in input:
		return input, tokens

	match = re.findall(r'\s\d+[[,\d+]*[.\d+]*]*\s', input)
	if match != None:
		for m in match:
			m = m.strip()
			tokens.append(m)

	return input, tokens





def main():
	mylist = []
	test = 'here is a act93B 12a.b test 100?23 100.323 123 10.124.124.01 1000000.23 10,000,000.23 string 10,00 that 10,000,000 contains, 1,000.37 commas,that separate, words 1,100 and numbers'

	test, mylist = identifyFormattedNumbers(test)

	test = "this is a test for th'hs here-is-a-phrase do-i-want 93-thousand contractions 09-38-le9t 99-99-99 jack-in-the-box I'm HERE'RE i'm she's we're they're hasn't can't alex's"

	#test, mylist = identifyPhrases(test)

if __name__ == "__main__": 
	main()