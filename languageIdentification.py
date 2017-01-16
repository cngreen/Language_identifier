import sys
import os
import re
import math

def trainBigramLanguageModel(input):
	charFreq = {}
	bigramFreq = {}

	input = input.lower()

	for i in range (len(input)):
		if input[i] not in charFreq.keys():
			charFreq[input[i]] = 1
		else:
			charFreq[input[i]] += 1

		if ( i + 1 < len(input)):
			bigram = input[i] + input[i + 1]
			if bigram not in bigramFreq.keys():
				bigramFreq[bigram] = 1
			else:
				bigramFreq[bigram] += 1

	return charFreq, bigramFreq


def calculateProbabilityStart(freq, V):
	probability = float(freq + 1)/float(1 + V)
	probability = math.log(probability)
	return probability

def calculateProbBigram(charFreq, bigramFreq, V):
	# print("CF: ", charFreq, " BF: ", bigramFreq, " V: ", V)
	# print (charFreq + V)
	# print (bigramFreq + 1)
	probability = float(bigramFreq + 1)/float(charFreq + V)
	probability = math.log(probability)
	return probability

def identifyLanguage(input, charFreq, bigramFreq):
	englishProb = 0
	frenchProb = 0
	italianProb = 0

	englishV = len(charFreq[0])
	frenchV = len(charFreq[1])
	italianV = len(charFreq[2])

	if (len(input) != 0):
		c = input[0]
		if c not in charFreq[0].keys():
			englishProb += calculateProbabilityStart(0, englishV)
		else:
			englishProb += calculateProbabilityStart(charFreq[0][c], englishV)
		if c not in charFreq[1].keys():
			frenchProb += calculateProbabilityStart(0, frenchV)
		else:
			frenchProb += calculateProbabilityStart(charFreq[1][c], frenchV)
		if c not in charFreq[2].keys():
			italianProb += calculateProbabilityStart(0, italianV)
		else:
			italianProb += calculateProbabilityStart(charFreq[2][c], italianV)
	
	i = 1

	while (i < len(input)):
		b = input[i - 1] + input[i]
		c = input[i]

		if c in charFreq[0].keys() and b in bigramFreq[0].keys(): #character and bigram both in dictionaries
			englishProb += calculateProbBigram(charFreq[0][c], bigramFreq[0][b], englishV)
		if b not in bigramFreq[0].keys(): #bigram not in dictionary
			if c not in charFreq[0].keys(): #neither in dictionary
				englishProb += calculateProbBigram(0, 0, englishV)
			else:
				englishProb += calculateProbBigram(charFreq[0][c], 0, englishV)
		
		if c in charFreq[1].keys() and b in bigramFreq[1].keys():
			frenchProb += calculateProbBigram(charFreq[1][c], bigramFreq[1][b], frenchV)
		if b not in bigramFreq[1].keys():
			if c not in charFreq[1].keys():
				frenchProb += calculateProbBigram(0, 0, frenchV)
			else:
				frenchProb += calculateProbBigram(charFreq[1][c], 0, frenchV)

		if c in charFreq[2].keys() and b in bigramFreq[2].keys():
			italianProb += calculateProbBigram(charFreq[2][c], bigramFreq[2][b], italianV)
		if b not in bigramFreq[2].keys():
			if c not in charFreq[2].keys():
				italianProb += calculateProbBigram(0, 0, italianV)
			else:
				italianProb += calculateProbBigram(charFreq[2][c], 0, italianV)

		i += 1


	output = ''

	if (englishProb >= frenchProb and englishProb >= italianProb):
		output = 'English'
	elif (frenchProb >= englishProb and frenchProb >= italianProb):
		output = 'French'
	else:
		output = 'Italian'

	return output


def main():
	#dictionaries:
	# english_charFreq = {}
	# english_bigramFreq= {}
	# french_charFreq = {}
	# french_bigramFreq = {}
	# italian_charFreq = {}
	# italian_bigramFreq = {}

	charFreq = [{}, {}, {}] 
	#0 = english, 1 = french, 2 = italian
	bigramFreq = [{}, {}, {}]

	#training file location
	foldername = 'languageIdentification.data/training/'
	path = os.path.join(os.getcwd(), foldername)


#train english data--------------------------------------
	path2file = os.path.join(path, 'English')
	lines = [line.rstrip('\n') for line in open(path2file)]

	for line in lines:
		chars, bigrams = trainBigramLanguageModel(line)
		for c in chars:
			if c not in charFreq[0].keys():
				charFreq[0][c] = chars[c]
			else:
				charFreq[0][c] += chars[c]

		for b in bigrams:
			if b not in bigramFreq[0].keys():
				bigramFreq[0][b] = bigrams[b]
			else:
				bigramFreq[0][b] += bigrams[b]

#train french data--------------------------------------
	path2file = os.path.join(path, 'French')
	lines = [line.rstrip('\n') for line in open(path2file)]

	for line in lines:
		chars, bigrams = trainBigramLanguageModel(line)
		for c in chars:
			if c not in charFreq[1].keys():
				charFreq[1][c] = chars[c]
			else:
				charFreq[1][c] += chars[c]

		for b in bigrams:
			if b not in bigramFreq[1].keys():
				bigramFreq[1][b] = bigrams[b]
			else:
				bigramFreq[1][b] += bigrams[b]

#train italian data--------------------------------------
	path2file = os.path.join(path, 'Italian')
	lines = [line.rstrip('\n') for line in open(path2file)]

	for line in lines:
		chars, bigrams = trainBigramLanguageModel(line)
		for c in chars:
			if c not in charFreq[2].keys():
				charFreq[2][c] = chars[c]
			else:
				charFreq[2][c] += chars[c]

		for b in bigrams:
			if b not in bigramFreq[2].keys():
				bigramFreq[2][b] = bigrams[b]
			else:
				bigramFreq[2][b] += bigrams[b]

	
#obtain test data----------------------------------------------
#--------------------------------------------------------------
	#find name of testfile
	filename = str(sys.argv[1])
	path = os.path.join(os.getcwd(), filename)

	lines = [line.rstrip('\n') for line in open(path)]

	i = 0

	targetFile = open('languageIdentification.output', 'w+')

	while (i < len(lines)):
		lines[i] = lines[i].lower()
		language = identifyLanguage(lines[i], charFreq, bigramFreq)
		output = str(i) + ' ' + language + '\n'
		targetFile.write(output)
		i += 1




if __name__ == "__main__": 
	main()