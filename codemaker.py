from sys import *
import parser

ptokens = parser.parser()
 
def codemaker():
	fout=open("output.cpp","w")
	for token in ptokens:
		fout.write(str(token))
		fout.write(' ')
	fout.close()
