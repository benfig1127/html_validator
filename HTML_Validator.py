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

	#checks to see if all brackets are closed properly first
	#par_checker_input=_extract_tags(html,True)
	#print('par_checker_inputs:',par_checker_input)
	
	#boolean_output=_is_closed_properly(par_checker_input)
	#print('boolean_output:',boolean_output)
	
	#print('\n')
	
	
	
	#checks to see if all html tags have matching closing '/' tags 
	par_checker_input=_extract_tags(html)
	#print('inputs:',par_checker_input)
	
	html_checker_output=_closing_html_checker(par_checker_input)
	#print('html_checker_output:',html_checker_output)
	
	return html_checker_output
	
	#if boolean_output and html_checker_output:
		#return True
	#return False
	
	#print(par_checker_input)
	#return parChecker(par_checker_input)

	#print('\n')
	
	
	
def _is_closed_properly(input_list):
	
	output_list=[]
	for html_chunk in input_list:
		output_list.append(_parChecker(html_chunk))
	for output_piece in output_list:
		if not output_piece:
			return False 
	return True
	
def _closing_html_checker(html_tag_list):
	if len(html_tag_list)%2!=0:
		return False
	for index, tag in enumerate(html_tag_list):
		#print(tag)
		if index%2==0:
			#print('expected output:',tag!='<>')
			if tag!='<>':
				return False
		if index%2==1:
			#print('expected output:',tag!='</>')
			if tag!= '</>':
				return False
	return True 
	
def _parChecker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == "<":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()

		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False	
	
	
	
	
	



def _extract_tags(html):
	'''
	This is a helper function for `validate_html`.
	By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

	This function returns a list of all the html tags contained in the input string,
	stripping out all text not contained within angle brackets.


	
	>>> _extract_tags('Python <strong>rocks</strong>!')
	['<strong>', '</strong>']
	'''
	
	switch=0
	output_string=''
	for index, char in enumerate(html):
		#if switch==1:
			#print('switch on, adding char:',char)
			#output_string+=(char)
		if char == '/' and html[index-1]=='<':
			output_string+=char
		if char == '<':
			#print('turning switch on, adding:',char)
			switch=1
			output_string+=char
		if char == '>':
			#print('turning switch off, adding space:')
			switch=0
			output_string+=char
			output_string+=(' ')
	#print('stripping string and outputting', output_string)
	output_string=output_string.split()
	
	return output_string

	#switch=0
	#output_string=''
	#for index, char in enumerate(html):
		##if switch==1:
			##print('switch on, adding char:',char)
			##output_string+=(char)
		#if char == '/' and not only_closing_ops and html[index-1]=='<':
			#output_string+=char
		#if char == '<':
			##print('turning switch on, adding:',char)
			#switch=1
			#output_string+=char
		#if char == '>':
			##print('turning switch off, adding space:')
			#switch=0
			#output_string+=char
			#output_string+=(' ')
	##print('stripping string and outputting', output_string)
	#output_string=output_string.split()
	
	#return output_string

#print(validate_html('<strong>example</strong>'))
#print(validate_html('<strong>example'))
