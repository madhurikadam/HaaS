import pexpect
import sys
import os
import time
#import os_function
#from variable import *
#from shutil import copyfile
#from os_funtion import *
#import launch
#print str(sys.argv[1])

if not os.path.isfile("/root/.ssh/id_rsa"):
	cmd="ssh-keygen -N '' -t rsa -f /root/.ssh/id_rsa"
	os.system(cmd)
	print "SSHKEY generated"
else:
	print "Key is present"
#os.system(cmd)
if not os.path.isdir("/home/student/.ssh"):
	cmd="mkdir /home/student/.ssh"
	os.system(cmd)
	print "/home/student/.ssh directory created"
else:
	print "/home/student/.ssh directory exist"

filevar=open("var.txt","r")
var=filevar.readlines()
length=len(var)
for i in range(length):
        var[i]=var[i].rstrip('\n')
filename="fixed_"+var[0]
print filename
print var[2]
print var[0]

name1=var[0]



file1="floating_"+name1

f=open(file1,"r")
ips=f.readlines()
print ips
f.close()
length=len(ips)

ips[0]=ips[0].rstrip('\n')
#ip=ips[0]
#print ip

ssh_newkey = 'Are you sure you want to continue connecting'
cmd='ssh-copy-id -i /root/.ssh/id_rsa.pub '+ips[0]
print cmd
p=pexpect.spawn(cmd)
time.sleep(5)
j=p.expect([ssh_newkey,'password:',pexpect.EOF])
if j==0:
	print "I say yes"
	p.sendline('yes')
	j=p.expect([ssh_newkey,'password:',pexpect.EOF])
if j==1:
	print "I give password",
	p.sendline("root123")
	p.expect(pexpect.EOF)
elif j==2:
	print "I either got key or connection timeout"
	pass
print p.before

file1="fixed_"+name1

cmd="scp MultiNode.tar.gz root@"+str(ips[0])+":/home/student/."
print cmd
os.system(cmd)
cmd="scp "+file1+" root@"+str(ips[0])+":/home/student/."
os.system(cmd)
cmd="scp var.txt root@"+str(ips[0])+":/home/student/."
os.system(cmd)



cmd="ssh "+str(ips[0])+" 'cd /home/student/;tar -xvzf MultiNode.tar.gz;cd MultiNode;chmod 777 start.sh;chmod 777 set_namenode.sh;python ssh2.py;python host_m.py;'"
os.system(cmd)
