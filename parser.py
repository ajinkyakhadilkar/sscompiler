##
## 30/03/17: Done till the starting { bracket in the for loop. Have to plan something about the closing bracket
## 
##
##

from sys import *
import lexer

tokens=lexer.lexer()
print tokens

output=[]

def parser():

	tokenIndex=0
	
	while tokens[tokenIndex] != '<EOF>':	# while loop was used because it is easier to increment the value of iterator inside the loop
		token=tokens[tokenIndex]	# Just to save us from typing tokens[tokenIndex] in the whole loop
		
		# FOR LOOP
		# for i in range(i,j,k)
		if token == "for":
			output.append('for')
			output.append('(')
			tokenIndex+=1
			
			iterator = tokens[tokenIndex]
			
			output.append(iterator+'=')
			tokenIndex+=2
			
			initValue = tokens[tokenIndex][6]
			
			output.append(initValue)
			output.append(';'+iterator+'<')
			
			finalValue = tokens[tokenIndex][8]
			
			output.append(finalValue)
			output.append(';')
			
			incrValue = tokens[tokenIndex][10]
			
			output.append(iterator+'+='+incrValue)
			
			output.append(')')
			
			tokenIndex+=1
			if tokens[tokenIndex] != ':' :
				print 'Error in for loop'
			
			else:
				tokenIndex+=1
				output.append(tokens[tokenIndex])	#At this position, the tab was replaced by bracket, 
									#this is the starting bracket
			
		tokenIndex+=1
		
	print output
		
