from sys import *
def lexer():
	tokens=[]
	num_stack=[]
	lines=[]
	tokens=['for','i','in','range(0,1,2)',':','{']
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
				lines.append(line)
				line=""
				continue

			if char=='\t':
				tabcount+=1
				tabState=1
				continue

			if char!='\t' and tabState==1:
				if tabcount > currtab:	# this means an indentation has ocuured w.r.t previous indent
					currtab+=1
					lines.append('{')
		
				elif tabcount < currtab:
					currtab-=1
					lines.append('}')	# an indentation has ended
					
				else: continue
									

				tabState=0
				tabcount=0
				

					
			line=line+char
		# END for
		print lines
		return lines
	# lineDivider() ends
	
	data = open_file(argv[1])
	lines = lineDivider(data)

	
	#def tokenizer():
	
	#tokenizer ends
	
	tokens.append("<EOF>")
	return tokens
	
# lexer() ends
