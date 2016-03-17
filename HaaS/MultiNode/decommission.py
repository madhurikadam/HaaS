import os
import sys

cname=sys.argv[1]
no_node=sys.argv[2]

fname="/home/student/fixed_"+cname
f=open(fname,"r")
a=f.readlines()
f.close()

length=len(a)

for i in range(length):
	a[i]=a[i].rstrip('\n')

fname="/usr/local/hadoop/etc/hadoop/dfs.exclude"
f=open(fname,"r")
b=f.readlines()
f.close()
length2=len(b)

count=length-length2
count=count-1
i=int(no_node)
f=open(fname,"a+")
while i:
	str1=a[count]+"\n"
	f.write(str1)
	count=count-1
	i=i-1
f.close()

cmd="/usr/local/hadoop/bin/hdfs dfsadmin -refreshNodes"
os.system(cmd)

cmd="/usr/local/hadoop/bin/hdfs dfsadmin -report"
os.system(cmd)



