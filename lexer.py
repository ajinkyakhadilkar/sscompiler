# 23/04/17: Implemented tokenizer till for loop using regular expressions. Logical error in for loop
# Tokens are splitted on the basis of spaces. Please make use spaces to differentiate tokens in the source code

from sys import *
import re

def lexer():
	tokens=[]
	num_stack=[]		
	lines=[]
	
	#tokens=['for','i','in','range(0,1,20)',':','{','for','j','in','range(0,1,1)',':','{','}','}']
	#tokens=['variable = 10']
	def open_file(filename):
		data=open(filename,"r").read()
		data +="<EOF>"
		return data
	# open_file() ends
	
	def lineDivider(filecontents):		# Divides the data into lines also introducing { and } in place of tab spaces
	
		filecontents=list(filecontents)
		
		tabcount=0
		currtab=0;	#current number of indentation
		tabState=0;	#Used to help us count the number of tabspaces in a line
				#If tabState is 1 i.e. we are counting number of continuous tab spaces
		line=""
		for char in filecontents:
			if char=='\n':
				tabcount=0
				lines.append(line)
				line=""
				continue
			'''
			print 'tabcount : '+ str(tabcount)
			print 'tabState : '+ str(tabState)
			print 'currtab : ' + str(currtab)
			print '\n'	
			'''
			if char=='\t':
				tabcount+=1
				tabState=1
				continue

			if char!='\t' and (tabState==1 or (currtab==1 and tabcount==0)):

				if tabcount > currtab:	# this means an indentation has ocuured w.r.t previous indent
					currtab+=1
					lines.append('{')
	
				elif tabcount < currtab:
					currtab-=1
					lines.append('}')	# an indentation has ended
					
				else: pass
									

				tabState=0
				#tabcount=0
			line=line+char
		# END for
		print '\n\nLINE DIVIDER:- \n'
		print lines
		return lines
	# lineDivider() ends
	
	data = open_file(argv[1])
	lines = lineDivider(data)

	
	def tokenizer():
	
		for line in lines:
		
			#expression (initialization)
			if re.match('[a-zA-Z][a-zA-Z0-9]*[\s]+=[\s]+[0-9]+\Z',line):    #'''[\s]*[[\+|-|\*|/]{1}[\s]*[a-zA-Z0-9]]?'''	 num = 9
			#Matching expressions in the format "variable = n (operand) m " where n and m are numbers.
				'''
				i=0
				var1=''
				num1=''
				while line[i] != '=':
					var1 = var1 + line[i]
					i=i+1
				i=i+1
				
				print var1
				
				for index in line[i:] :
					num1=num1 + line[i]
					i=i+1
				num1 = int(num1)
				'''
				tokens.append('INIT')
				#tokens.append([var1,'=',num1])
				tokens.append(line.split())
				
				
				
			#expression
			
			if re.match('([a-zA-Z][a-zA-Z0-9]*)[\s]+=[\s]+(([a-zA-Z][a-zA-Z0-9]*)|[0-9]*)[\s]+((\+|-|/|\*)[\s]+(([a-zA-Z][a-zA-Z0-9]*)|[0-9]*))+',line):
				tokens.append('EXPR')
				tokens.append(line.split())
			
			#if condition
			
			if re.match('if\s+[a-zA-Z][a-zA-Z0-9]*\s*(>|>=|<|<=|==)\s*(([a-zA-Z][a-zA-Z0-9]*)|[0-9]+)\s*:\Z',line):
				tokens.append('IF')
				tokens.append(line.split())
			
			
			#for loop
			if re.match('for\s[a-zA-Z][a-zA-Z0-9]*\sin\srange\(-?[0-9]+,-?[0-9]+(,-?[0-9]+)?\):',line):
				forv=''
				inv=''
				rangev=''
				index=''
				i=0
				tokens.append('FOR')
			
				tokens.append(line.split())#[forv,index,inv,rangev,line[i]])
					
							

			#while loop
			
			if re.match('while\s*[a-zA-Z][a-zA-Z0-9]*\s*(<|>|<=|>=|==)\s*[0-9]*\s*:',line):
				tokens.append('WHILE')
				tokens.append(line.split())
		
			#print fuction to print strings
			
			if re.match('print\s(\'|\")[\w\W]*(\'|\")',line):
				
				prntstr=[]
				
				tokens.append('PRINT')
	
				prntstr.append(line[0:5])
				prntstr.append(line[6])
				prntstr.append(line[7:-1])
				prntstr.append(line[-1])
				
				tokens.append(prntstr)
					
			#print function to print variables
			
			elif re.match('print[\s]*[\w\W]*',line):
			
				prntstr=[]
				
				tokens.append('PRINTVAR')
				
				prntstr.append(line[0:5])
				prntstr.append(line[6:])
				
				tokens.append(prntstr)
					
			#brackets
			if line=='{':
				tokens.append('{')
			elif line=='}':
				tokens.append('}')
		return
	#tokenizer ends
	tokenizer()
	tokens.append("<EOF>")
	return tokens
	
# lexer() ends
