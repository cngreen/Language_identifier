import re

def identifyAcronymsAbbrev(input):
	#finds formatted numbers
	tokens = []
	if '.' not in input:
		return input, tokens

	match = re.findall(r'\s\w+[.]+\w*[.\w*]*', input)
	if match != None:
		for m in match:
			m = m.strip()
			tokens.append(m)
		input = re.sub(r'\s\w+[.]+\w*[.\w*]*', '', input)

	return input, tokens





def main():
	mylist = []
	test = 'for vortex generators, the importance is stressed of the vortex paths'

	test, mylist = identifyAcronymsAbbrev(test)

	print test, mylist

if __name__ == "__main__": 
	main()