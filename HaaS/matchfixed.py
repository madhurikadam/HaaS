import os
import sys
from fixedip import *
def getcheck():
	file1=open("fixedcheck","a+") 
	file1.seek(0)
	file1.truncate()
	file1.seek(0)
	file1=open("floatingcheck","a+")
        file1.seek(0)
        file1.truncate()
        file1.seek(0)	
	getfixed_ip("fixedcheck")
	getfloating_ip("floatingcheck")
def getmatch(name1):
	file1=open("fixedip","a+")
        file1.seek(0)
        file1.truncate()
        file1.seek(0)
	file1.close()
	file1=open("floatip","a+")
        file1.seek(0)
        file1.truncate()
        file1.seek(0)
	file1.close()
	getfixed_ip("fixedip")
        getfloating_ip("floatip")			
	fixname="fixed_"+name1
	file_diff=open(fixname, 'a+')
	oldlines = set(open('fixedcheck', 'r'))
	for line in open("fixedip", 'r'):
    		if line not in oldlines:
        		file_diff.write(line)
	floatname="floating_"+name1
        file_diff=open(floatname, 'a+')
        #file_diff.seek(0)
        #file_diff.truncate()
        #file_diff.seek(0)
        oldlines = set(open('floatingcheck', 'r'))
        for line in open("floatip", 'r'):
                if line not in oldlines:
                        file_diff.write(line)			
		

#getmatchfloating("myy")

