from terminatedI import *
import sys
import os

cname=raw_input("Enter cluster name: ")
no_node=raw_input("Enter number of nodes: ")


fname="floating_"+cname
f=open(fname,"r")
a=f.readlines()
f.close()

length=len(a)
for i in range(length):
	a[i]=a[i].rstrip('\n')

cmd="ssh "+a[0]+" 'cd /home/student/MultiNode;python rm_updatem.py "+cname+" "+no_node+";'"
os.system(cmd)

i=int(no_node)

count=int(length)
while i:
        count=count-1
        iname=cname+"-"+str(count)
        terminateInstance(iname,cname)
        i=i-1

