from addstatic import *
import os

cname=raw_input("Enter name of Cluster: ")
no_add=raw_input("Enter number of nodes: ")

i=int(no_add)

while i:
	addInstance(cname,no_add)
	i=i-1

fname="floating_"+cname
f=open(fname,"r")
a=f.readlines()
f.close()
length=len(a)
print a
for i in range(length):
	a[i]=a[i].rstrip('\n')
print a

cmd="scp fixed_"+cname+" root@"+a[0]+":/home/student/."
os.system(cmd)

cmd="ssh "+a[0]+" 'cd /home/student/MultiNode;python add_slave.py "+cname+" "+no_add+";'"
os.system(cmd)


