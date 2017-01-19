import re

def comma(input):
	numbers = []
	if ',' not in input:
		return input, numbers

	match = re.findall(r'^\d{1,3}(,\d{3})*(\.\d+)?$', input)
	if match != None:
		for m in match:
			numbers.append(m)

	print numbers

	return input, numbers


def identifyContractions(input):
	contractions = {} #list of contactions, adapted from https://en.wikipedia.org/wiki/Wikipedia:List_of_English_contractions
	contractions["aren't"] = 'are not'
	contractions["can't"] = 'can not'
	contractions["could've"] = 'could have'
	contractions["couldn't"] = 'could not'
	contractions["didn't"] = 'did not'
	contractions["doesn't"] = 'does not'
	contractions["don't"] = 'do not'
	contractions["hadn't"] = 'had not'
	contractions["hasn't"] = 'has not'
	contractions["he'd"] = 'he had'
	contractions["he'll"] = 'he will'
	contractions["he's"] = 'he is'
	contractions["how'd"] = 'how did'
	contractions["how'll"] = 'how will'
	contractions["how's"] = 'how is'
	contractions["i'd"] = 'i would'
	contractions["i'll"] = 'i will'
	contractions["i'm"] = 'i am'
	contractions["i've"] = 'i have'
	contractions["isn't"] = 'is not'
	contractions["it'll"] = 'it will'
	contractions["it's"] = 'it is'
	contractions["mightn't"] = 'might not'
	contractions["might've"] = 'might have'
	contractions["mustn't"] = 'must not'
	contractions["must've"] = 'must have'
	contractions["she'd"] = 'she had'
	contractions["she'll"] = 'she will'
	contractions["she's"] = 'she is'
	contractions["should’ve"] = 'should have'
	contractions["shouldn't"] = 'should not'
	contractions["something's"] = 'something has'
	contractions["that'll"] = 'that will'
	contractions["that's"] = 'that is'
	contractions["that'd"] = 'that would'
	contractions["there'd"] = 'there had'
	contractions["there're"] = 'there are'
	contractions["there's"] = 'there is'
	contractions["they'd"] = 'they had'
	contractions["they'll"] = 'they will'
	contractions["they're"] = 'they are'
	contractions["they've"] = 'they have'
	contractions["wasn't"] = 'was not'
	contractions["we'd"] = 'we had'
	contractions["we'll"] = 'we will'
	contractions["we're"] = 'we are'
	contractions["we've"] = 'we have'
	contractions["weren't"] = 'were not'
	contractions["what'd"] = 'what did'
	contractions["what'll"] = 'what will'
	contractions["what're"] = 'what are'
	contractions["what's"] = 'what is'
	contractions["what've"] = 'what have'
	contractions["when's"] = 'when is'
	contractions["where'd"] = 'where did'
	contractions["where's"] = 'where is'
	contractions["where've"] = 'where have'
	contractions["who'd"] = 'who did'
	contractions["who'll"] = 'who will'
	contractions["who're"] = 'who are'
	contractions["who's"] = 'who has'
	

who’re	who are
who’s	who has / who is / who does
who’ve	who have
why'd	why did
why’ll	why will
why’re	why are
why’s	why has / why is / why does
won’t	will not
won’t’ve	will not have
would’ve	would have
wouldn’t	would not
wouldn’t’ve	would not have
y’all / ya'll	you all, literally, "ya all"
y’all’d’ve	you all would have
y’all’dn’t’ve	you all would not have
y’all’ll	you all will
y’all’on’t	you all will not
y’all’ll’ve	you all will have
y'all're	you all are
y’all’ll’ven’t	you all will have not
you’d	you had / you would
you’ll	you will
you’re	you are
you’ve	you have
	if "'" not in input:
		return input, contractions

	match = re.findall(r"[a-zA-Z]+'[a-zA-Z]+", input) #things that look like contractions
	
	if match != None:
		for m in match:


	return input, contractions




def main():
	mylist = []
	test = 'here is a test 123 string that 10,000,000 contains, commas,that separate, words 1,100 and numbers'

	#test, mylist = comma(test)

	test = "this is a test for contractions i'm she's we're they're hasn't can't alex's"

	test, mylist = identifyContractions(test)

if __name__ == "__main__": 
	main()