##
## 30/03/17: Done till the starting { bracket in the for loop. Have to plan something about the closing bracket
## 10/04/17: Completed basic incremental for loop
## 
## 03/05/07: Implemented variables dictionary, calculating expressions, started while loop. Minor changes in checking paranthesis.
##
## Use print statement to print variables

from sys import *
import lexer
import re

def parser():

	tokens=lexer.lexer()
	print '\n\nTOKENS:-\n'
	print tokens
	keywords = ['int','float','double','long','for','while','do','if','else','as','switch','case','break','continue','bool','in']
	output=[]
	variables={} #To store the value of each variable in the code
	
	output.append('#include <iostream>')
	output.append('\n')
	output.append('#include <stdio.h>')
	output.append('\n\n')
	output.append('using namespace std;')
	output.append('\n\n')
	output.append('int main()')
	output.append('\n')
	output.append('{')
	output.append('\n')
	
	tokenIndex=0
	brackets=0	#to keep a track of number of open brackets (the concept used here is simliar to Push Down Automata
	
	while tokens[tokenIndex] != '<EOF>':	# while loop was used because it is easier to increment the value of iterator inside the loop
		token=tokens[tokenIndex]	# Just to save us from typing tokens[tokenIndex] in the whole loop
		
		# FOR LOOP
		# for i in range(i,j,k)
		if token == 'FOR':
			tokenIndex+=1
			token=tokens[tokenIndex]
			
			i=6
			while token[3][i]!=')':
				i=i+1
			parameters=token[3][6:i].split(',')

			output.append(token[0])	#for
			output.append('(')
			
			iterator = token[1] #iterator
			
			output.append(iterator)
			output.append('=')
	
			initValue = int(parameters[0])
			finalValue = int(parameters[1])
			
			if finalValue > initValue:
				symbol='<'
			elif finalValue < initValue:
				symbol='>'
			else: symbol = '=='
		
			output.append(initValue)
			
			output.append(';')
			
			output.append(iterator)
			output.append(symbol)
			output.append(finalValue)
			
			output.append(';')
			
			incrValue = int(parameters[2])
		
			if parameters[2]<0:
				sign='-='
			else:
				sign='+='
			output.append(iterator)
			output.append(sign)
			output.append(incrValue)
			
			output.append(')')
		
			if token[3][i+1] != ':' :
				print 'Error in for loop'
			'''
			else:
				tokenIndex+=1
				brackets+=1
				output.append(tokens[tokenIndex])	#At this position, the tab was replaced by bracket, 
									#this is the starting bracket
			'''						
		
		# While loop
			
		if token == 'WHILE':
			tokenIndex+=1
			token=tokens[tokenIndex]
			
			output.append('while')
			output.append('(')
			
			iterator=token[1]
			
			if iterator not in variables:
				print 'ERROR: ' + iterator + ' is not defined!'
				exit()
			
			symbol=token[2]
			limit=token[3]
			
			output.append(iterator)
			output.append(symbol)
			output.append(limit)
			output.append(')')

			
		
		# print statement to print strings
		
		if token == 'PRINT':
			tokenIndex+=1
			token=tokens[tokenIndex]
			
			output.append('cout')
			output.append('<<')
			output.append('"')
			output.append(token[2])
			output.append('"')
			output.append(';')
		
		# print statement to print variables
		
		if token == 'PRINTVAR':
			tokenIndex+=1
			token=tokens[tokenIndex]
			
			if token[1] not in variables:
				print 'ERROR: ' + token[1] + ' is not defined!'
				exit()
				
			else:

				output.append('cout')
				output.append('<<')
				output.append(token[1])
				output.append(';')
		
		# Variable assignment and initialization		
		
		if token == 'INIT':
			tokenIndex+=1
			token=tokens[tokenIndex]
			
			variables[token[0]]=token[2]
			
			if token[0] in keywords:
				print 'ERROR: ' + str(token[0]) + ' is a keyword!'
				exit()	
			
			output.append('long int')
			output.append(token[0])
			output.append('=')
			output.append(token[2])
			output.append(';')
			print variables
			
		# Arithmetic Expressions
		
		if token == 'EXPR':
			tokenIndex+=1
			token=tokens[tokenIndex]
			
			exprString='' #used to store the expression
			
			exprflag = 0 #used to separate variables and symbols
			for iterator in token[2:]:
				if exprflag==0:
					if iterator.isdigit():		#if operand is a digit
						exprString = exprString + iterator
						exprflag=1	
						
					elif iterator not in variables:	#if operand is not a digit AND it is NOT defined before
						print 'ERROR: ' + iterator + ' not defined!'
						exit()
	
					else:				#if opreand is not a digit and it is defined before
						exprString = exprString + variables[iterator]
						exprflag=1
				else:
					exprString = exprString + iterator
					exprflag=0
			
			print '\n\nEVALUATING EXPRESSION :-\n'
			print exprString

			print variables
			
			for t in token:
				output.append(t)
				
			output.append(';')
		
		#if statement
		
		if token == 'IF':
			tokenIndex+=1
			token=tokens[tokenIndex]
			
			output.append('if')
			output.append('(')
			
			part1 = token[1]
			symbol = token[2]
			part2 = token[3]
			
			output.append(part1)
			output.append(symbol)
			output.append(part2)
			output.append(')')

		
		#Checking for paranthesis
			
		if tokens[tokenIndex]=='{':
			brackets+=1
			output.append(tokens[tokenIndex])
		
		if tokens[tokenIndex] == '}':
			brackets-=1
			output.append(tokens[tokenIndex])
			
		tokenIndex+=1
	

	
	if brackets != 0:
		print "ERROR: Paranthesis do not match!"
		exit()

	output.append('\n')
	output.append('return 0;')
	output.append('}')

	print '\nTRANSLATED C++ TOKENS:- \n'
	print output	
	return output
