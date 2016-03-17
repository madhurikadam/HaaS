#!/usr/bin/python
import os,glob
import subprocess
import commands
import pexpect
#import variable

#cmd="id -u -n"
#user = commands.getoutput(cmd)
#print useir
#user="student"



#a=["192.168.0.15","192.168.0.10"]
filevar=open("/home/student/var.txt","r")
var=filevar.readlines()
length=len(var)
for i in range(length):
        var[i]=var[i].rstrip('\n')
name1=var[0]
user=var[2]


filename="/home/"+user+"/fixed_"+name1
f=open(filename,"r")
a=f.readlines()
f.close()
length=len(a)

for i in range(length):
	a[i]=a[i].rstrip('\n')

str1=a[0]+" HadoopMaster\n"
for i in range(1,length):
	str1=str1+a[i]+" "+"HadoopSlave"+str(i)+"\n"

fo=open("/etc/hosts","a")
fo.write(str1)
fo.close()

for i in range(length):

	if i==0:	
		cmd="/home/"+user+"/MultiNode/wo_start.sh"		
		os.system(cmd)
		
	else:
		cmd="scp /home/"+user+"/MultiNode.tar.gz root@"+a[i]+":/home/student/."
		#os.system(cmd)
		cmd="ssh "+a[i]+" 'cd /home/"+user+"MultiNode;sh wo_start.sh;'"

		os.system(cmd) 
	


cmd="echo 'HadoopMaster' >> /usr/local/hadoop/etc/hadoop/masters"
os.system(cmd) 
str2=""
for i in range(1,length):
	str2=str2+" HadoopSlave"+str(i)+"\n"

#cmd="echo '%s' > /usr/local/hadoop/etc/hadoop/slaves" % str2
#print cmd
fo=open("/usr/local/hadoop/etc/hadoop/slaves","wb")
fo.write(str2)
fo.close()
#os.system(cmd)



cmd="touch tp.txt"
os.system(cmd)
#fo.open("tp.txt","w")
#fo.write(str1)
#fo.close()

cmd= "echo '%s' >tp" % str1
os.system(cmd)
for i in range(1,length):
	cmd= "cat tp |ssh "+a[i]+" 'cat >> /etc/hosts'"
#	print cmd
	os.system(cmd)

##############################Configuration File#####################################






######################################################################################

for i in range(1,length):
	cmd="rsync -axvP /usr/local/hadoop/ root@"+a[i]+":/usr/local/hadoop/"
	os.system(cmd)

cmd=" sh set_namenode.sh"
os.system(cmd)

for i in range (1,length):
	cmd="ssh "+a[i]+" 'rm -rf /usr/local/hadoop_tmp/;mkdir -p /usr/local/hadoop_tmp/;mkdir -p /usr/local/hadoop_tmp/hdfs/datanode;'"
#	print cmd
	os.system(cmd)

cmd="/usr/local/hadoop/bin/hdfs namenode -format"
os.system(cmd)


execfile("service_start.py")

print "Running Services:"
cmd ="jps"
os.system(cmd)


'''os.system returns a return value indicating the success or failure of the command. It does not return the output from stdout or stderr. To grab the output from stdout (or stderr), use subprocess.Popen.'''

'''
cat commands-to-execute-remotely.sh | ssh server
'''

'''

import commands
cmd = 'ls'
output = commands.getoutput(cmd)
print output

'''
'''
proc=subprocess.Popen('echo "$str1"', shell=True, stdout=subprocess.PIPE, )
#os.system(echo str1 > p.txt)
output=proc.communicate()[0]
print output
___________________________________________________________________________

import spur

shell = spur.SshShell(hostname="localhost", username="bob", password="password1")
result = shell.run(["echo", "-n", "hello"])
print result.output # prints hello

If you need to run inside a shell:

shell.run(["sh", "-c", "echo -n hello"])



'''
