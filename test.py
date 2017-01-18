import re

def indentifyDates(input):
	#finds dates of format 01.01.17 01/01/17 01.01.2017 01/01/2017 01-01-17 01-01-2017 
	# 1.1.17 1/1/17 1.1.2017 1/1/2017 1-1-17 1-1-2017
	# 1, 17 01, 17 1, 2017 01, 2017
	dates = ''
	if not any(char.isdigit() for char in input): #if no digit, no dates
		return input, dates

	strlist = [] #a list of chars in the str
	for c in input:
		strlist.append(c)

	i = 0
	stringLength = len(strlist)
	while i < stringLength:
		if strlist[i].isdigit(): #a number
			i += 1
			if i < stringLength:
				if strlist[i] == '.' or strlist[i] == '/' or strlist[i] == '-': #common date separators
					i += 1
					if i < stringLength:
						if strlist[i].isdigit(): #a number after a common separator
							i += 1
							if i < stringLength:
								i += 1
						else:
							continue #this is not a date (number, separator, non-numeric character)
					else:
						continue #end of string
				elif strlist[i].isdigit(): #two numbers in a row
					i += 1

				elif strlist[i] == ',':
					i += 1
					if i < stringLength:
						if strlist[i] == ' ':
							i += 1
							if i < stringLength:
								if strlist[i].isdigit():
									i += 1
									if i < stringLength:
										if strlist[i].isdigit(): #number, numbernumber (valid date format)
											i +=1
											if i < stringLength:
												if strlist[i].isdigit():
													i += 1
													if i < stringLength:
														if strlist[i].isdigit: #1, 2017 (valid date format)
															i -= 6
															temp = 0
															while temp < 7:
																temp += 1
																dates += strlist[i]
																i += 1

															continue #added date
														else:
															continue #not a date 1, 999
											else: #add 1, 17 to dates
												i -= 4
												temp = 0
												while temp < 5:
													temp += 1
													dates += strlist[i]
													i += 1
												continue #end of string
										else:
											continue #end of string



			else:
				continue #end of string
		else:
			i += 1

	return input, dates



def main():
	test = 'here is a 1/1/2017 string with 1.1.16 a bunch of 1, 2017 dates may 17, 1993 3.3.16 1-1-10 string string'

	dates = ''
	input = ''

	input, dates = indentifyDates(test)
	print(dates)

if __name__ == "__main__": 
	main()