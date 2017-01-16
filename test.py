import re

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


def main():
	inputA = 'text goes here <OBVIOUS TAG>'
	inputB = 'text before <TRICKY TAG> text after'
	inputD = 'hello <tag attribute=">"></tag> goodbye'

	print (inputA)
	inputA = removeSGML(inputA)
	print ("removed: ", inputA)

	print (inputB)
	inputB = removeSGML(inputB)
	print ("removed: ", inputB)

	# print (inputC)
	# inputC = removeSGML(inputC)
	# print ("removed: ", inputC)

	print (inputD)
	inputD = removeSGML(inputD)
	print ("removed: ", inputD)


if __name__ == "__main__": 
	main()