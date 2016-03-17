import os,sys
import shutil

cname=raw_input("Enter  name of cluster: ")
no_node=raw_input("Enter number of nodes: ")

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


i1=int(no_node)
delete=[""]*i1
for i in range(i1):
        delete[i]=a[count+1]
	count=count+1



shutil.copy2('/usr/local/hadoop/etc/hadoop/dfs.exclude','/home/student/MultiNode/check')
with open('/home/student/MultiNode/check') as oldfile, open('/home/student/MultiNode/check1', 'w') as newfile:
	for line in oldfile:
		if not any(d in line for d in delete):
                        newfile.write(line)

shutil.copy2('/home/student/MultiNode/check1','/usr/local/hadoop/etc/hadoop/dfs.exclude')

i=int(no_node)
count=length-length2
for j in range(i):
	cmd="ssh "+a[count+1]+" /usr/local/hadoop/sbin/hadoop-daemon.sh start datanode"	
	print cmd
	os.system(cmd)
        cmd="ssh "+a[count+1]+" /usr/local/hadoop/sbin/yarn-daemon.sh start nodemanager"
        os.system(cmd)
	count=count+1

cmd="/usr/local/hadoop/bin/hdfs dfsadmin -refreshNodes"
os.system(cmd)
cmd="/usr/local/hadoop/bin/hdfs dfsadmin -report"
os.system(cmd)



