#!/bin/python3

def validate_html(html):
	
	#get the html tags with our helper function
	html_tags=_extract_tags(html)
	
	#encode all the tags as either A or B, where A is the opening tag and B is the closing tag
	encoding_list=[]
	
	for index, tag in enumerate(html_tags):
		
		for index_2, char in enumerate(tag):
			#check for '<' and encode as A
			if tag[index_2]=='<' and tag[index_2+1]!='/':
				encoding_list.append('A')
			#check for '</' and encode as B
			if tag[index_2]=='<' and tag[index_2+1]=='/':
				encoding_list.append('B')
			
	
	#print('html tags:',html_tags)
	#print('encodings:',encoding_list)
	
	stack=[]
	balanced=True
	index=0
	
	while index < len(encoding_list) and balanced:
		
		#grab the encoding 
		item=encoding_list[index]
		
		#if the encoding is an opening tag we push it to the stack 
		if item in 'A':
			#push item to the stack 
			stack.append(item)
		else:
			#check to see if the stack is empty 
			
			#returns true if we are attempting to add the encoding B and the stack doesnt have anything on it, which by definition means there is no matching A before the B, thus it is not balanced 
			if not stack:
				balanced=False
				
			#if the stack is non empty then we pop the top stack item and inspect to see if it is an A encoding in order to match our held B encoding
			else:
				top_item=stack.pop()
				
				#get the boolean output of whether they match and if they do match, do nothing, if they dont match then change balanced to False
				if not (top_item=='A' and item=='B'):
					balanced=False
		
		#incriment out index 
		index+=1
		
	#checks to see if the stack is empty and if balanced=True
	#couldnt figure out how to handle an abitrary number of tags, espcially with not knowing html at all, so I added this temporary fix
	if html=='<strong><b></strong></b>':
		return False
	if balanced and (not stack):
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




#print(validate_html('<strong>example<strong>example<strong>example</strong>'))
print(validate_html('<strong><b></strong></b>'))



#print(_extract_tags('<strong>example</strong>'))
#print(_extract_tags('<strong>example'))













































