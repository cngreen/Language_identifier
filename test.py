import re

def testFunc(input):
	tokens = []
	words = input.split()
	for w in words:
		w = re.sub(r'\W+', '', w)
		tokens.append(w)

	return input, tokens





def main():
	mylist = []
	test = 'here is words and $ * th&ey mi*ght ha]]ve ch@$#@!%#^@%aracter*@#s in them.'

	test, mylist = testFunc(test)

if __name__ == "__main__": 
	main()