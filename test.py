import re

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

		#print("starting index: ", firstndx)

		# find the first > of the line
		for i in range(len(strlist)):
			if strlist[i] == '>':
				secondndx = i
				break

		#print("ending index: ", secondndx)

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
			while temp <= secondndx:
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

				else:
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



def main():
	#test = '<tagname attributeone="value one>" attributetwo="<value two>">Child Text</tagname>'
	test = '<typical tag> typical text "" <typical tag>'

	test = removeSGML(test)

	print(test)

if __name__ == "__main__": 
	main()