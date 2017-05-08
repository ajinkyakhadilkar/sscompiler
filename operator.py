from sys import *

tokens=['a','*','5',3,'*',8,'ab','+','cd',4.5,'+',6]
def operator():
	
	l = len(tokens)
#---------* operator----------------
	for i in range(0,l):
		if tokens[i]=='*':
			#print tokens[i+1]
			if is_number(tokens[i-1]):
				print str(tokens[i-1])+tokens[i]+str(tokens[i+1])
				#print"number"
			else:
				#print "string"
				for j in range(0,int(tokens[i+1])):
					print tokens[i-1]
#---------concatenation--------------	
	for i in range(0,l):
		if tokens[i]=='+':
			#print tokens[i+1]
			if is_number(tokens[i-1]):
				print str(tokens[i-1])+tokens[i]+str(tokens[i+1])
				#print"number"
			else:
				#print "string"
				print ("strcat(%s,%s)"%(tokens[i-1],   tokens[i+1]))

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
 
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass
	return False

"""
var1=2
var2=23
var3='a'
is_number('kl')
is_number('2')
is_number('2.3')
"""
"""
def tuples():
	tokens=['(',1,2,56,7')','('hi','this','is','tuple',')']
	#tup1 = ('physics', 'chemistry', 1997, 2000)
	#print is_number(tup1[2])
	#print is_number(tup1[1])
"""
operator()
#tuples()
