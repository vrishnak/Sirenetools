#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, getopt

def main(argv):
	
	try:
		opts,args=getopt.getopt(argv,"l:f:",["linenumber=","filename="])
	except getopt.GetoptError:
		print u'Usage: SI_readline -l <linenumber> -f <filename>'
	# ------------
	print 'opts',opts
	# ------------
	# Default values
	number=-1
	name=""
	
	
	for option,argument in opts:
	
		if option=='-l':
			# Verification argument must be an integer
			#print ' type:',type(argument)
			number=int(argument)
			#print ' number=',type(number)
		if option=='-f':
			#print argument,' of type :',type(argument)
			name=argument
			
	# ------------
	if (number!=-1 and name!=""):
		fichier=open(name,'r')
		for line,contains in enumerate(fichier,1):
			if line==int(number):
				print contains
			elif line>number:
				break
		fichier.close()
	else:
		print u'Command aborded:not valid line or filename'

# _____________________________
if __name__=="__main__":
	main(sys.argv[1:])
