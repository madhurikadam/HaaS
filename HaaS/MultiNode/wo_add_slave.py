import sys
import os

cluster_name=sys.argv[1]
add_no=sys.argv[2]
add_no=int(add_no)
user="student"

############################################################OBTAIN IP###############################
filename="/home/"+user+"/fixed_"+cluster_name
f=open(filename,"r")
b=f.readlines()
f.close()
length=len(b)
start=length-add_no
master=b[0]
print b
for i in range(start):
	b.pop(0)
print b
#length =len(a)
for i in range(add_no):
	b[i]=b[i].rstrip('\n')


f=open(filename,"r")
a=f.readlines()
f.close()

for i in range(length):
	a[i]=a[i].rstrip('\n')
#======================================================================================================================================

execfile("ssh2.py")

#=============================================================================================================================
for i in range(start,length):
	cmd="scp /home/student/MultiNode.tar.gz root@"+a[i]+":/home/student/."
	#os.system(cmd)
	cmd="ssh "+a[i]+" 'cd /home/student/MultiNode;chmod 777 start.sh;./start.sh;'"
	os.system(cmd)

#=========================================================================================================================================
str1=""
for i in range(start,length):
        str1=str1+a[i]+" "+"HadoopSlave"+str(i)+"\n"
str3=a[0]+" HadoopMaster\n"
for i in range(1,length):
        str3=str3+a[i]+" "+"HadoopSlave"+str(i)+"\n"


fo=open("/etc/hosts","a")
fo.write(str1)
fo.close()

cmd="touch tp.txt"
os.system(cmd)

cmd= "echo '%s' >tp" % str1
os.system(cmd)
for i in range(1,start):
        cmd= "cat tp |ssh "+a[i]+" 'cat >> /etc/hosts'"
#       print cmd
        os.system(cmd)


cmd= "echo '%s' >tp" % str3
os.system(cmd)
for i in range(start,length):
        cmd= "cat tp |ssh "+a[i]+" 'cat >> /etc/hosts'"
#       print cmd
        os.system(cmd)

#============================================================================================================================================


str2=""
for i in range(start,length):
        str2=str2+" HadoopSlave"+str(i)+"\n"
fo=open("/usr/local/hadoop/etc/hadoop/slaves","a+")
fo.write(str2)
fo.close()


cmd= "echo '%s' >tp" % str2
os.system(cmd)
for i in range(1,start):
        cmd= "cat tp |ssh "+a[i]+" 'cat >> /usr/local/hadoop/etc/hadoop/slaves'"
        os.system(cmd)

str2=""

for i in range(1,length):
        str2=str2+" HadoopSlave"+str(i)+"\n"
cmd= "echo '%s' >tp" % str2
os.system(cmd)
for i in range(start,length):
        cmd= "cat tp |ssh "+a[i]+" 'cat >> /usr/local/hadoop/etc/hadoop/slaves'"

        os.system(cmd)
#=============================================================================================================================================

for i in range (start,length):
        cmd="rsync -axvP /usr/local/hadoop/ root@"+a[i]+":/usr/local/hadoop/"
        os.system(cmd)
	cmd="ssh "+a[i]+" 'rm -rf /usr/local/hadoop_tmp/;mkdir -p /usr/local/hadoop_tmp/;mkdir -p /usr/local/hadoop_tmp/hdfs/datanode;'"
#       print cmd
        os.system(cmd)

for i in range (start,length):
	cmd="ssh "+a[i]+" /usr/local/hadoop/sbin/hadoop-daemon.sh start datanode"
	os.system(cmd)
	cmd="ssh "+a[i]+" /usr/local/hadoop/sbin/yarn-daemon.sh start nodemanager"
	os.system(cmd)

