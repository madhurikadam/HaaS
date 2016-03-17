import os
import sys
import shutil

name=sys.argv[1]
rm_no=sys.argv[2]
rm_no=int(rm_no)

user="student"
filename="/home/"+user+"/fixed_"+name
f=open(filename,"r")
a=f.readlines()
f.close()
length=len(a)
temp=length




for i in range(length):
        a[i]=a[i].rstrip('\n')

delete=[None]*rm_no	
for i in range(rm_no):
	delete[i]="HadoopSlave"+str(length-i-1)

print delete

src=['/etc/hosts','/usr/local/hadoop/etc/hadoop/slaves']
src_l=len(src)

for i in range(src_l):
	shutil.copy2(src[i],'/home/student/MultiNode/check')

	

	with open('check') as oldfile, open('check1', 'w') as newfile:
		for line in oldfile:
        		if not any(d in line for d in delete):
            			newfile.write(line)

	shutil.copy2('/home/student/MultiNode/check1',src[i])

count=length

delete=[""]*rm_no
for i in range(rm_no):
        delete[i]=a[count-1]
        count=count-1



shutil.copy2('/usr/local/hadoop/etc/hadoop/dfs.exclude','/home/student/MultiNode/check')
with open('/home/student/MultiNode/check') as oldfile, open('/home/student/MultiNode/check1', 'w') as newfile:
        for line in oldfile:
                if not any(d in line for d in delete):
                        newfile.write(line)

shutil.copy2('/home/student/MultiNode/check1','/usr/local/hadoop/etc/hadoop/dfs.exclude')



 
for i in range(1,length-rm_no):
	cmd="ssh "+a[i]+" python /home/student/MultiNode/remove_slave.py "+str(length)+" "+str(rm_no)
	print cmd
	os.system(cmd)

for i in range(length-rm_no,length):
	cmd="ssh "+a[i]+" /usr/local/hadoop/sbin/hadoop-daemon.sh stop datanode"
	os.system(cmd)
        cmd="ssh "+a[i]+" /usr/local/hadoop/sbin/yarn-daemon.sh stop nodemanager"
        os.system(cmd)


