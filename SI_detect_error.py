#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt
import re

def REPAIR(ligne):
	print u'Detecting field for line:'
	#print ligne
	REG='"{3}.+"{3}'
	U=re.search(REG,ligne)
	if U:
		print '--found triple quote'
		S=re.split(r'"{3}',ligne)
		idx=0
		NewS=''
		for i in S:		
			idx=idx+1
			if idx%2==0:
				print i,
				i=re.sub(r'"";""',';',i)
				i='"'+i+'"'
				print ' replaced by ',i
			NewS=NewS+i
		return NewS
	return False


def main(argv):
	
	try:
		opts,args=getopt.getopt(argv,"N:f:",["NumberOfFields=","--filename="])
	except getopt.GetoptError:
		print u'Usage: SI_detect_error -f <filename> -N <number_of_fields>'
	
	# Default values
	#print opts
	# Arguments
	for option,argument in opts:
		if option in ["-f","--filename"]:
			filename=argument
		if option in ["-N","--NumberOfFields"]:
			NumberOfFields=int(argument)
			print argument
			# Etude de cas NumberOfFields=0
	
	# Start
	if (filename!="" and NumberOfFields>1):
		with open(filename,'rb') as INPUT:
			line=0
			SEPARATOR=r'"\x3b"'
			for row in INPUT:
				line=line+1
				COL=re.split(SEPARATOR,row)
				if len(COL)!=NumberOfFields:
					print u'Error at line',line,u' number of fields differ. Value is',len(COL)
					print u'Trying to repair...'
					r=REPAIR(row)
					if r!=False:
						CC=re.split(SEPARATOR,r)
						if len(CC)==NumberOfFields:
							print u'...Repair succeed'
							row=r
						else:
							print u'...Repair Failed'
					else:
						print u'...Not known error...Repair Failed'
			print u'End of Scan'
	
# _____________________________
if __name__=="__main__":
	main(sys.argv[1:])