#!/bin/python3

from pythonds.basic import Stack

def validate_html(html):
	
	'''
	This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

	>>> validate_html('<strong>example</strong>')
	True
	>>> validate_html('<strong>example')
	False
	'''

	# HINT:
	# use the _extract_tags function below to generate a list of html tags without any extra text;
	# then process these html tags using the balanced parentheses algorithm from the book
	# the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
	# but arbitrary text located between the html tags

	return output
	
	
	



def _extract_tags(html):
	'''
	This is a helper function for `validate_html`.
	By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

	This function returns a list of all the html tags contained in the input string,
	stripping out all text not contained within angle brackets.

	>>> _extract_tags('Python <strong>rocks</strong>!')
	['<strong>', '</strong>']
	'''
	output=[]
	
	for index, char in enumerate(html):
		#print('index:',index)
		if char=='<':
			#initilize our string to hold the html tag
			output_string=''
			
			#grab the initial index
			i=index
			
			#grab the initial value
			item=html[i]
			
			#adds '<'
			output_string+=item
			
			#adds the following characters up to the '>', not that this checks the previous item in this while statement 
			while item!='>':
				
				#incriment the index
				i+=1
				
				#incriment to the next item 
				item=html[i]
				
				output_string+=item
				
				#print('Adding item in tag at index:',index)
			
			#saves our html tag to our output list
			#print(output_string)
			output.append(output_string)
			#print(output)
			
	return output






#print(_extract_tags('<strong>example</strong>'))
#print(_extract_tags('<strong>example'))













































